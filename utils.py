# """
# utils.py
# Helper functions: input cleaning, pattern matching, intent detection.
# """

# import re
# from responses import FAQ_DATA, GREETINGS, FAREWELLS, THANKS


# def clean_input(text: str) -> str:
#     """Lowercase, strip whitespace, and remove punctuation from user input."""
#     text = text.lower().strip()
#     text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
#     text = re.sub(r"\s+", " ", text)      # collapse multiple spaces
#     return text


# def detect_intent(user_input: str) -> str:
#     """
#     Detect the type of intent: greeting / farewell / thanks / faq / unknown.
#     """
#     cleaned = clean_input(user_input)

#     words_in_input = set(cleaned.split())

#     # Check greetings (word-boundary match)
#     for word in GREETINGS:
#         if word in words_in_input:
#             return "greeting"

#     # Check farewells (word-boundary match)
#     for word in FAREWELLS:
#         if word in words_in_input:
#             return "farewell"

#     # Check thanks (phrase or word match)
#     for phrase in THANKS:
#         phrase_words = phrase.split()
#         if len(phrase_words) == 1:
#             if phrase in words_in_input:
#                 return "thanks"
#         else:
#             if phrase in cleaned:
#                 return "thanks"

#     # Check FAQ patterns
#     match = find_best_match(cleaned)
#     if match:
#         return "faq"

#     return "unknown"


# def find_best_match(cleaned_input: str):
#     """
#     Find the best matching FAQ entry using keyword matching with scoring.
#     Returns the matched FAQ dict or None.

#     Scoring rules:
#     - Full phrase match in input  → high score (phrase_len * 4)
#     - All words of a pattern found → medium score (phrase_len * 2)
#     - Partial word overlap         → low score (matching_words only)

#     A match is only returned if:
#     1. Score is above a minimum absolute threshold (3), AND
#     2. At least 50% of the best-matching pattern's words are present
#        (prevents single generic words like 'college' from triggering).
#     """
#     # Stop words that should never count as meaningful matches alone
#     STOP_WORDS = {"how", "is", "the", "a", "an", "what", "are", "tell",
#                   "me", "about", "i", "my", "do", "can", "please", "any",
#                   "give", "show", "explain", "college"}

#     input_words = set(cleaned_input.split()) - STOP_WORDS

#     best_score = 0
#     best_faq = None
#     best_coverage = 0.0

#     for faq in FAQ_DATA:
#         faq_best_score = 0
#         faq_best_coverage = 0.0

#         for pattern in faq["patterns"]:
#             pattern_clean = re.sub(r"[^\w\s]", "", pattern.lower())
#             pattern_words = pattern_clean.split()
#             meaningful_words = [w for w in pattern_words if w not in STOP_WORDS]

#             if not meaningful_words:
#                 continue

#             # Full phrase match
#             if pattern_clean in cleaned_input:
#                 s = len(meaningful_words) * 4
#                 cov = 1.0
#             else:
#                 matched = [w for w in meaningful_words if w in input_words]
#                 s = len(matched) * 2
#                 cov = len(matched) / len(meaningful_words)

#             if s > faq_best_score:
#                 faq_best_score = s
#                 faq_best_coverage = cov

#         if faq_best_score > best_score:
#             best_score = faq_best_score
#             best_faq = faq
#             best_coverage = faq_best_coverage

#     # Must meet BOTH: minimum score AND at least 50% keyword coverage
#     if best_score >= 3 and best_coverage >= 0.5:
#         return best_faq
#     return None


# def get_response(user_input: str) -> tuple[str, str | None]:
#     """
#     Main response dispatcher.
#     Returns (response_text, category_or_None).
#     """
#     if not user_input.strip():
#         return "Please type something so I can help you! 😊", None

#     intent = detect_intent(user_input)
#     cleaned = clean_input(user_input)

#     if intent == "greeting":
#         return (
#             "👋 Hello! Welcome to the **College Help Desk**.\n\n"
#             "I can help you with:\n"
#             "🎓 Admissions  💰 Fees  📚 Courses  🏠 Hostel\n"
#             "📝 Exams  💼 Placements  📶 WiFi  🎉 Events\n\n"
#             "What would you like to know?",
#             "General",
#         )

#     if intent == "farewell":
#         return (
#             "👋 Goodbye! Have a great day.\n"
#             "Feel free to come back if you have more questions! 😊",
#             "General",
#         )

#     if intent == "thanks":
#         return (
#             "You're welcome! 😊 Is there anything else I can help you with?",
#             "General",
#         )

#     if intent == "faq":
#         match = find_best_match(cleaned)
#         if match:
#             return match["response"], match["category"]

#     # Unknown
#     return (
#         "🤔 I'm sorry, I didn't quite understand that.\n\n"
#         "Here are some things I can help with:\n"
#         "- Admissions & Application Process\n"
#         "- Fee Structure & Scholarships\n"
#         "- Courses & Departments\n"
#         "- Hostel & Transport\n"
#         "- Exams & Results\n"
#         "- Placement & Careers\n"
#         "- Library, WiFi & Events\n\n"
#         "Try asking something like: *'How do I apply?'* or *'What is the fee?'*",
#         None,
#     )


# def is_unknown_response(response_text: str) -> bool:
#     """Returns True if the response is the 'unknown' fallback."""
#     return "didn't quite understand" in response_text


# def get_all_categories() -> list[str]:
#     """Return unique list of FAQ categories."""
#     cats = list({faq["category"] for faq in FAQ_DATA})
#     return sorted(cats)


# def get_faqs_by_category(category: str) -> list[dict]:
#     """Return all FAQs for a given category."""
#     return [faq for faq in FAQ_DATA if faq["category"] == category]



"""
utils.py
Helper functions: input cleaning, pattern matching, intent detection.
"""

import re
from responses import FAQ_DATA, GREETINGS, FAREWELLS, THANKS


def clean_input(text: str) -> str:
    """Lowercase, strip whitespace, and remove punctuation from user input."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text)      # collapse multiple spaces
    return text


def detect_intent(user_input: str) -> str:
    """
    Detect the type of intent: greeting / farewell / thanks / faq / unknown.
    """
    cleaned = clean_input(user_input)

    words_in_input = set(cleaned.split())

    # Check greetings (word-boundary match)
    for word in GREETINGS:
        if word in words_in_input:
            return "greeting"

    # Check farewells (word-boundary match)
    for word in FAREWELLS:
        if word in words_in_input:
            return "farewell"

    # Check thanks (phrase or word match)
    for phrase in THANKS:
        phrase_words = phrase.split()
        if len(phrase_words) == 1:
            if phrase in words_in_input:
                return "thanks"
        else:
            if phrase in cleaned:
                return "thanks"

    # Check FAQ patterns
    match = find_best_match(cleaned)
    if match:
        return "faq"

    return "unknown"


def find_best_match(cleaned_input: str):
    """
    Find the best matching FAQ entry using keyword matching with scoring.
    Returns the matched FAQ dict or None.

    Scoring rules:
    - Full phrase match in input  → high score (phrase_len * 4)
    - All words of a pattern found → medium score (phrase_len * 2)
    - Partial word overlap         → low score (matching_words only)

    A match is only returned if:
    1. Score is above a minimum absolute threshold (3), AND
    2. At least 50% of the best-matching pattern's words are present
       (prevents single generic words like 'college' from triggering).
    """
    # Stop words that should never count as meaningful matches alone
    STOP_WORDS = {"how", "is", "the", "a", "an", "what", "are", "tell",
                  "me", "about", "i", "my", "do", "can", "please", "any",
                  "give", "show", "explain", "college"}

    input_words = set(cleaned_input.split()) - STOP_WORDS

    best_score = 0
    best_faq = None
    best_coverage = 0.0

    for faq in FAQ_DATA:
        faq_best_score = 0
        faq_best_coverage = 0.0

        for pattern in faq["patterns"]:
            pattern_clean = re.sub(r"[^\w\s]", "", pattern.lower())
            pattern_words = pattern_clean.split()
            meaningful_words = [w for w in pattern_words if w not in STOP_WORDS]

            if not meaningful_words:
                continue

            # Full phrase match
            if pattern_clean in cleaned_input:
                s = len(meaningful_words) * 4
                cov = 1.0
            else:
                matched = [w for w in meaningful_words if w in input_words]
                s = len(matched) * 2
                cov = len(matched) / len(meaningful_words)

            if s > faq_best_score:
                faq_best_score = s
                faq_best_coverage = cov

        if faq_best_score > best_score:
            best_score = faq_best_score
            best_faq = faq
            best_coverage = faq_best_coverage

    # Must meet BOTH: minimum score AND at least 50% keyword coverage
    # Exception: if only 1 meaningful word in input but it scores well (>=4), allow it
    if best_score >= 3 and (best_coverage >= 0.5 or best_score >= 4):
        return best_faq
    return None


def get_response(user_input: str) -> tuple[str, str | None]:
    """
    Main response dispatcher.
    Returns (response_text, category_or_None).
    """
    if not user_input.strip():
        return "Please type something so I can help you! 😊", None

    intent = detect_intent(user_input)
    cleaned = clean_input(user_input)

    if intent == "greeting":
        return (
            "👋 Hello! Welcome to the **College Help Desk**.\n\n"
            "I can help you with:\n"
            "🎓 Admissions  💰 Fees  📚 Courses  🏠 Hostel\n"
            "📝 Exams  💼 Placements  📶 WiFi  🎉 Events\n\n"
            "What would you like to know?",
            "General",
        )

    if intent == "farewell":
        return (
            "👋 Goodbye! Have a great day.\n"
            "Feel free to come back if you have more questions! 😊",
            "General",
        )

    if intent == "thanks":
        return (
            "You're welcome! 😊 Is there anything else I can help you with?",
            "General",
        )

    if intent == "faq":
        match = find_best_match(cleaned)
        if match:
            return match["response"], match["category"]

    # Unknown
    return (
        "🤔 I'm sorry, I didn't quite understand that.\n\n"
        "Here are some things I can help with:\n"
        "- Admissions & Application Process\n"
        "- Fee Structure & Scholarships\n"
        "- Courses & Departments\n"
        "- Hostel & Transport\n"
        "- Exams & Results\n"
        "- Placement & Careers\n"
        "- Library, WiFi & Events\n\n"
        "Try asking something like: *'How do I apply?'* or *'What is the fee?'*",
        None,
    )


def is_unknown_response(response_text: str) -> bool:
    """Returns True if the response is the 'unknown' fallback."""
    return "didn't quite understand" in response_text


def get_all_categories() -> list[str]:
    """Return unique list of FAQ categories."""
    cats = list({faq["category"] for faq in FAQ_DATA})
    return sorted(cats)


def get_faqs_by_category(category: str) -> list[dict]:
    """Return all FAQs for a given category."""
    return [faq for faq in FAQ_DATA if faq["category"] == category]