import os
import csv
import asyncio
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from slugify import slugify
from datetime import datetime

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    # We will prompt the user if key is missing, but for now let's just warn or exit gracefully if run
    print("Warning: OPENAI_API_KEY not found in environment.")

client = OpenAI(api_key=api_key)

OUTPUT_DIR = "src/content/blog"
CSV_FILE = "errors.csv"

def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_tutorial(error_code, context, hint):
    prompt = f"""
    You are a Senior Python Developer writing for SudoFix, a technical documentation site.
    Write a comprehensive, technical tutorial about the following Python error:
    
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
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful expert Python technical writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content for {error_code}: {e}")
        return None

def main():
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} not found.")
        return

    ensure_dir_exists(OUTPUT_DIR)
    
    df = pd.read_csv(CSV_FILE)
    print(f"Found {len(df)} errors to process.")

    for index, row in df.iterrows():
        error_code = row['error_code']
        context = row['context']
        hint = row['solution_hint']
        
        # Create a unique slug
        slug_base = f"{error_code} {context}"
        slug = slugify(slug_base, max_length=50)
        
        filename = f"{OUTPUT_DIR}/{slug}.md"
        
        if os.path.exists(filename):
            print(f"Skipping {slug}, already exists.")
            continue
            
        print(f"Generating tutorial for: {error_code} ({slug})...")
        content = generate_tutorial(error_code, context, hint)
        
        if content:
            pub_date = datetime.now().strftime("%Y-%m-%d")
            frontmatter = f"""---
title: "Fix {error_code}: {context[:30]}..."
description: "Learn how to resolve the {error_code} in Python. {hint[:50]}..."
pubDate: "{pub_date}"
tags: ["python", "{error_code.lower()}", "debugging"]
---

"""
            full_content = frontmatter + content
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(full_content)
            
            print(f"Saved {filename}")
        else:
            print(f"Failed to generate {slug}")

if __name__ == "__main__":
    main()
