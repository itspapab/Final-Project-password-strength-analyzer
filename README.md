#  Password Strength Analyzer

My final project is a command-line tool that analyzes the strength of user passwords based on entropy, common attack patterns, and security policy checks. It provides clear, colorful feedback using the `rich` library and offers suggestions for improving weak passwords.

---

## Features 

- Checks for:
  - Minimum length (12+ characters)
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
-  Calculates password entropy
- Provides actionable suggestions
- Includes automated unit tests using `unittest`
- Terminal output is color-coded with `rich`

---

## Requirements

- Python 3.6+
- `rich` package

Install with:

```bash
pip install -r requirements.txt
