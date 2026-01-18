import os
import time
import glob
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Groq Client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not found in environment.")
    exit(1)

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)

SOURCE_DIR = "src/content/blog/en"
TARGET_LANGS = {"pt": "Portuguese (Brazil)", "es": "Spanish"}


def translate_content(content, target_language):
    prompt = f"""
    You are a professional technical translator.
    Translate the following Markdown content to {target_language}.
    
    IMPORTANT RULES:
    1. Keep the Frontmatter (lines between ---) intact, BUT translate the 'title' and 'description' values.
    2. Do NOT translate technical terms, variable names, function names, or code blocks.
    3. Keep the same structure, headers, and formatting.
    4. Return ONLY the translated markdown, no preamble.

    Content to translate:
    {content}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful expert technical translator.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error translating: {e}")
        return None


def main():
    files = glob.glob(f"{SOURCE_DIR}/*.md")
    print(f"Found {len(files)} files to process.")

    for file_path in files:
        filename = os.path.basename(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for lang_code, lang_name in TARGET_LANGS.items():
            target_dir = f"src/content/blog/{lang_code}"
            target_file = f"{target_dir}/{filename}"

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            if os.path.exists(target_file):
                print(f"Skipping {lang_code}/{filename} (already exists)")
                continue

            print(f"Translating {filename} to {lang_name}...")
            translated_content = translate_content(content, lang_name)

            if translated_content:
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(translated_content)
                print(f"Saved {target_file}")
                time.sleep(0.2)  # Be gentle with the API
            else:
                print(f"Failed to translate {filename} to {lang_name}")


if __name__ == "__main__":
    main()
