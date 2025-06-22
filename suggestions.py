# suggestions.py

COMMON_PASSWORDS = {"password", "123456", "admin", "letmein", "qwerty"}


def get_suggestions(password, checks, entropy):
    suggestions = []

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid using common passwords.")
    if not checks["length"]:
        suggestions.append("Use at least 12 characters.")
    if not checks["uppercase"]:
        suggestions.append("Add at least one uppercase letter.")
    if not checks["lowercase"]:
        suggestions.append("Add at least one lowercase letter.")
    if not checks["digit"]:
        suggestions.append("Include at least one number.")
    if not checks["special"]:
        suggestions.append("Include at least one special character.")
    if entropy < 50:
        suggestions.append("Increase character variety to boost entropy.")

    return suggestions
