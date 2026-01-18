import os
import time
import glob
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Setup Groq Client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not found.")
    exit(1)

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)
MODEL = "llama-3.3-70b-versatile"

DIRS = {
    "pt": {"path": "src/content/blog/pt", "lang": "Portuguese (Brazil)"},
    "es": {"path": "src/content/blog/es", "lang": "Spanish"},
}


def translate_safe(content, target_lang):
    max_retries = 8
    base_delay = 5

    for attempt in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a technical translator. Translate the markdown content to {target_lang}. Preserve frontmatter exactly (do NOT translate keys like 'title:', 'description:', 'tags:'). Translate the values of 'title' and 'description'. Preserve code blocks exactly. Output ONLY the translated result.",
                    },
                    {"role": "user", "content": content},
                ],
                model=MODEL,
                temperature=0.3,
            )
            return chat_completion.choices[0].message.content.strip()

        except Exception as e:
            error_str = str(e).lower()
            if "429" in error_str or "rate limit" in error_str:
                wait_time = base_delay * (2**attempt)
                print(
                    f"    [429 Rate Limit] Attempt {attempt+1}/{max_retries}. Waiting {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                print(f"    [Error] Unknown error: {e}")
                break

    return None


def main():
    for code, info in DIRS.items():
        path = info["path"]
        lang = info["lang"]
        print(f"Processing {lang} in {path}...")

        files = glob.glob(f"{path}/*.md")
        files.sort()

        for i, file in enumerate(files):
            filename = os.path.basename(file)
            print(f"[{i+1}/{len(files)}] Translating {filename}...")

            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            if len(content) < 50:
                print(f"    [Skip] Content too short.")
                continue

            translated = translate_safe(content, lang)

            if translated:
                if not translated.startswith("---"):
                    print(
                        f"    [Warn] Malformed translation (no frontmatter). Saving anyway."
                    )

                with open(file, "w", encoding="utf-8") as f:
                    f.write(translated)
                print(f"    [Success] Updated.")
            else:
                print(f"    [Fail] Skipping after max retries.")

            # Safety delay for Groq
            time.sleep(5)


if __name__ == "__main__":
    main()
