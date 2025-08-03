import os
import re
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)

def is_valid_persona_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Find first non-blank line
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i == len(lines):
        return False, "File is empty"
    first_line = lines[i].strip()
    if not re.match(r"^###\s+Persona:\s+.+", first_line):
        return False, "First non-blank line is not '### Persona: (name)'"
    num_h4 = sum(1 for line in lines if re.match(r"^####\s+", line.strip()))
    if num_h4 < 12:
        return False, f"Only {num_h4} level-4 headings found (need at least 12)"
    return True, ""

def main():
    files = [f for f in os.listdir('.') if f.lower().endswith('.md') and os.path.isfile(f)]
    passed = 0
    failed = 0
    for fname in files:
        ok, reason = is_valid_persona_file(fname)
        if not ok:
            logging.warning(f"{fname}: {reason}")
            failed += 1
        else:
            passed += 1
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
