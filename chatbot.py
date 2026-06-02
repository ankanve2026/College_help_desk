"""
chatbot.py
Terminal-based FAQ chatbot for College Help Desk.
Run this file directly for a console-only experience.
"""

from utils import get_response, clean_input
from responses import FAREWELLS


def print_banner():
    print("\n" + "=" * 55)
    print("   🎓  COLLEGE HELP DESK — FAQ CHATBOT  🎓")
    print("=" * 55)
    print("  Type your question and press Enter.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 55 + "\n")


def run_chatbot():
    print_banner()
    print("Bot: 👋 Hello! Welcome to the College Help Desk. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! 👋")
            break

        if not user_input:
            continue

        # Check for exit commands
        cleaned = user_input.lower()
        if any(word in cleaned for word in FAREWELLS):
            response, _ = get_response(user_input)
            print(f"\nBot: {response}\n")
            break

        response, category = get_response(user_input)

        if category:
            print(f"\n[Category: {category}]")
        print(f"\nBot: {response}\n")
        print("-" * 50)


if __name__ == "__main__":
    run_chatbot()