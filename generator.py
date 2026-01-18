import os
import csv
import time
import sys
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from slugify import slugify
from datetime import datetime

# Load environment variables
load_dotenv()

# Setup Groq Client
# Setup Groq Client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Warning: GROQ_API_KEY not found in environment.")

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)
MODEL = "llama-3.3-70b-versatile"

OUTPUT_DIR = "src/content/blog"


def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def generate_tutorial(error_code, context, hint, language):
    prompt = f"""
    You are a Senior {language} Developer writing for SudoFix, a technical documentation site.
    Write a comprehensive, technical tutorial about the following {language} error:
    
    Error: {error_code}
    Context: {context}
    Solution Hint: {hint}
    
    The article must be in Markdown format.
    Structure:
    1. **The Error**: Explain what the error means technically.
    2. **Why it occurs**: Common causes.
    3. **Example Code**: Show the code that causes it (use detailed examples).
    4. **How to Fix**: Step-by-step solution based on the hint.
    5. **Best Practices**: How to avoid this in the future.
    
    Tone: Professional, concise, MDN-style.
    Do NOT include the Frontmatter in the response, I will add it programmatically.
    Just content.
    """

    retries = 3
    base_delay = 5

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a helpful expert {language} technical writer.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(
                f"Error generating content for {error_code} (Attempt {attempt+1}/{retries}): {e}"
            )
            time.sleep(2)

    print(f"Failed to generate content for {error_code} after {retries} attempts.")
    return None


def main():
    # Default values
    csv_file = "errors.csv"
    language = "Python"

    # Override from command line args: python generator.py [csv_file] [language]
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    if len(sys.argv) > 2:
        language = sys.argv[2]

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    ensure_dir_exists(OUTPUT_DIR)

    df = pd.read_csv(csv_file)
    print(f"Processing {len(df)} errors from {csv_file} for language: {language}")

    for index, row in df.iterrows():
        error_code = row["error_code"]
        context = row["context"]
        hint = row["solution_hint"]

        # Create a unique slug
        slug_base = f"{error_code} {context} {language}"
        slug = slugify(slug_base, max_length=60)

        filename = f"{OUTPUT_DIR}/{slug}.md"

        if os.path.exists(filename):
            print(f"Skipping {slug}, already exists.")
            continue

        print(f"Generating tutorial for: {error_code} ({slug})...")
        content = generate_tutorial(error_code, context, hint, language)

        if content:
            pub_date = datetime.now().strftime("%Y-%m-%d")
            # Sanitize fields for YAML
            safe_title = f"Fix {error_code}: {context[:30]}...".replace(
                '"', "'"
            ).replace("\n", " ")
            safe_desc = f"Learn how to resolve the {error_code} in {language}. {hint[:50]}...".replace(
                '"', "'"
            ).replace(
                "\n", " "
            )

            frontmatter = f"""---
title: "{safe_title}"
description: "{safe_desc}"
pubDate: "{pub_date}"
tags: ["{language.lower()}", "{error_code.lower()}", "debugging"]
---

"""
            full_content = frontmatter + content

            with open(filename, "w", encoding="utf-8") as f:
                f.write(full_content)

            print(f"Saved {filename}")

            # Fast generation with Groq
            time.sleep(2)
        else:
            print(f"Failed to generate {slug}")


if __name__ == "__main__":
    main()
