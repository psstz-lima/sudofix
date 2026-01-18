import os
import re

CONTENT_DIR = "src/content/blog"


def fix_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure it starts with ---
    if not content.strip().startswith("---"):
        print(f"Skipping {filepath}: No frontmatter detected")
        return

    # Fix unquoted dates or invalid YAML format if necessary
    # Common issue in translation: pubDate: 2023-10-27 10:00:00+00:00 might need quotes or be valid
    # But let's check for broken lines.

    # Fix: Sometimes "description" has colons that aren't quoted.
    # Simple regex replace for pubDate if it looks weird?
    # Actually, let's just ensure pubDate is quoted if it's not.

    lines = content.split("\n")
    new_lines = []
    in_frontmatter = False

    for i, line in enumerate(lines):
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            new_lines.append(line)
            continue

        if in_frontmatter:
            # Check for pubDate
            if line.strip().startswith("pubDate:"):
                key, val = line.split(":", 1)
                val = val.strip()
                # valid astro date usually ISO string
                # If it's 2023-10-10 10:00:00+00:00, yaml handles it mostly.
                # But let's quote it to be safe.
                if not (val.startswith("'") or val.startswith('"')):
                    new_lines.append(f'{key}: "{val}"')
                    continue
            new_lines.append(line)
        else:
            new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))


def main():
    print(f"Scanning {CONTENT_DIR}...")
    count = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                fix_frontmatter(os.path.join(root, file))
                count += 1
    print(f"Scanned and potentially fixed {count} files.")


if __name__ == "__main__":
    main()
