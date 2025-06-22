# password_analyzer.py

import re
import math
from getpass import getpass
from suggestions import get_suggestions
from rich import print


def calculate_entropy(password):
    unique_chars = len(set(password))
    if unique_chars == 0:
        return 0
    entropy = len(password) * math.log2(unique_chars)
    return round(entropy, 2)


def basic_checks(password):
    checks = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    return checks


def analyze(password):
    print("\n[bold cyan]Analyzing Password...[/bold cyan]")
    entropy = calculate_entropy(password)
    checks = basic_checks(password)

    print(f"\n[bold]Entropy Score:[/bold] {entropy} bits")

    for name, passed in checks.items():
        status = "[green]✔[/green]" if passed else "[red]✘[/red]"
        print(f"{status} {name.capitalize()} requirement")

    suggestions = get_suggestions(password, checks, entropy)
    if suggestions:
        print("\n[bold yellow]Suggestions:[/bold yellow]")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\n[bold green]Your password looks strong![/bold green]")


if __name__ == "__main__":
    password = getpass("Enter password to analyze: ")
    analyze(password)
