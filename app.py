# """
# app.py
# Simple Streamlit College Help Desk Chatbot
# Rule-based FAQ matching + Groq AI fallback
# """

# import streamlit as st
# import os
# from groq import Groq
# from utils import get_response, is_unknown_response

# st.set_page_config(page_title="College Help Desk", page_icon="🎓")

# st.title("🎓 College Help Desk")
# st.caption("Ask me anything about admissions, fees, courses, hostel, exams, placements, and more.")

# # ── Session state ──────────────────────────────────────────────────────────────
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # ── Groq client ────────────────────────────────────────────────────────────────
# @st.cache_resource
# def get_groq_client():
#     # Try secrets first, then environment variable
#     try:
#         api_key = st.secrets["GROQ_API_KEY"]
#     except Exception:
#         api_key = os.getenv("GROQ_API_KEY", "")

#     api_key = api_key.strip()
#     if api_key and not api_key.startswith("gsk_YOUR"):
#         try:
#             return Groq(api_key=api_key)
#         except Exception:
#             return None
#     return None


# def ask_groq(user_message: str, history: list) -> str | None:
#     client = get_groq_client()
#     if not client:
#         return None

#     system_prompt = (
#         "You are EduBot, a friendly College Help Desk Assistant for a university in India. "
#         "Help students with admissions, fees, courses, hostel, exams, results, placements, "
#         "library, transport, WiFi, events, and general college life. "
#         "Be concise, warm, and helpful. Keep replies under 200 words."
#     )

#     messages = [{"role": "system", "content": system_prompt}]
#     for m in history[-10:]:
#         messages.append({"role": m["role"], "content": m["content"]})
#     messages.append({"role": "user", "content": user_message})

#     try:
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=0.7,
#             max_tokens=400,
#         )
#         return completion.choices[0].message.content
#     except Exception as e:
#         st.error(f"Groq error: {e}")
#         return None


# def get_final_response(user_input: str, history: list) -> str:
#     """Get rule-based response, fall back to Groq if no match."""
#     response_text, _ = get_response(user_input)

#     if is_unknown_response(response_text):
#         # Try Groq
#         client = get_groq_client()
#         if client:
#             with st.spinner("Thinking..."):
#                 ai_response = ask_groq(user_input, history)
#             if ai_response:
#                 return ai_response
#         # No Groq — return a cleaner fallback
#         return (
#             "🤔 I don't have specific information about that.\n\n"
#             "You can contact the college directly:\n"
#             "📞 +91-33-1234-5678 · 📧 info@college.edu\n\n"
#             "Or ask me about: Admissions, Fees, Courses, Hostel, Exams, Placements, WiFi, Events."
#         )

#     return response_text


# # ── Display chat history ───────────────────────────────────────────────────────
# if not st.session_state.messages:
#     with st.chat_message("assistant"):
#         st.markdown(
#             "👋 **Hello! Welcome to the College Help Desk.**\n\n"
#             "I can answer questions about:\n"
#             "🎓 Admissions · 💰 Fees · 📚 Courses · 🏠 Hostel · "
#             "📝 Exams · 💼 Placements · 📶 WiFi · 🎉 Events\n\n"
#             "Type your question below!"
#         )
# else:
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

# # ── Chat input ─────────────────────────────────────────────────────────────────
# user_input = st.chat_input("Ask me anything about the college...")

# if user_input and user_input.strip():
#     with st.chat_message("user"):
#         st.markdown(user_input)
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     history = [m for m in st.session_state.messages[:-1] if m["role"] in ("user", "assistant")]
#     response_text = get_final_response(user_input, history)

#     with st.chat_message("assistant"):
#         st.markdown(response_text)
#     st.session_state.messages.append({"role": "assistant", "content": response_text})

# # ── Sidebar ────────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("### ⚡ Quick Questions")
#     quick_qs = [
#         "How do I apply for admission?",
#         "What is the fee structure?",
#         "Are scholarships available?",
#         "What courses are offered?",
#         "Tell me about the hostel",
#         "When are the exams?",
#         "What is the placement record?",
#         "How to check my results?",
#         "Library timings?",
#         "Campus WiFi details?",
#     ]
#     for q in quick_qs:
#         if st.button(q, key=f"qq_{q}", use_container_width=True):
#             resp, _ = get_response(q)
#             st.session_state.messages.append({"role": "user", "content": q})
#             st.session_state.messages.append({"role": "assistant", "content": resp})
#             st.rerun()

#     st.divider()

#     client = get_groq_client()
#     if client:
#         st.success("🤖 Groq AI: Connected")
#     else:
#         st.warning("⚠️ Groq AI: Not configured\nAdd your key to `.streamlit/secrets.toml`")

#     if st.button("🗑️ Clear Chat", use_container_width=True):
#         st.session_state.messages = []
#         st.rerun()




"""
app.py
Simple Streamlit College Help Desk Chatbot
Rule-based FAQ matching + Groq AI fallback
"""

import streamlit as st
import os
from groq import Groq
from utils import get_response, is_unknown_response

st.set_page_config(page_title="MCKVIE Help Desk", page_icon="🎓")

st.title("🎓 MCKVIE Help Desk")
st.caption("Ask me anything about admissions, fees, courses, hostel, exams, placements, and more.")

# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Groq client ────────────────────────────────────────────────────────────────
@st.cache_resource
def get_groq_client():
    # Try secrets first, then environment variable
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.getenv("GROQ_API_KEY", "")

    api_key = api_key.strip()
    if api_key and not api_key.startswith("gsk_YOUR"):
        try:
            return Groq(api_key=api_key)
        except Exception:
            return None
    return None


def ask_groq(user_message: str, history: list) -> str | None:
    client = get_groq_client()
    if not client:
        return None

    system_prompt = (
        "You are EduBot, a friendly Help Desk Assistant for MCKV Institute of Engineering (MCKVIE), "
        "located at 243 G.T. Road (North), Liluah, Howrah, West Bengal. "
        "Help students with questions about admissions, fees, courses, hostel, exams, results, placements, "
        "library, transport, WiFi, events, campus life and general college topics. "
        "Be concise, warm, and helpful. Keep replies under 200 words. "
        "If asked about very specific internal details you are unsure about, direct them to www.mckvie.edu.in or call 033-2654-9315."
    )

    messages = [{"role": "system", "content": system_prompt}]
    for m in history[-10:]:
        messages.append({"role": m["role"], "content": m["content"]})
    messages.append({"role": "user", "content": user_message})

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=400,
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"Groq error: {e}")
        return None


def get_final_response(user_input: str, history: list) -> str:
    """Get rule-based response, fall back to Groq if no match."""
    response_text, _ = get_response(user_input)

    if is_unknown_response(response_text):
        # Try Groq
        client = get_groq_client()
        if client:
            with st.spinner("Thinking..."):
                ai_response = ask_groq(user_input, history)
            if ai_response:
                return ai_response
        # No Groq — return a cleaner fallback
        return (
            "🤔 I don't have specific information about that.\n\n"
            "You can contact the college directly:\n"
            "📞 +91-33-1234-5678 · 📧 info@college.edu\n\n"
            "Or ask me about: Admissions, Fees, Courses, Hostel, Exams, Placements, WiFi, Events."
        )

    return response_text


# ── Display chat history ───────────────────────────────────────────────────────
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(
            "👋 **Hello! Welcome to the College Help Desk.**\n\n"
            # "I can answer questions about:\n"
            # "🎓 Admissions · 💰 Fees · 📚 Courses · 🏠 Hostel · "
            # "📝 Exams · 💼 Placements · 📶 WiFi · 🎉 Events\n\n"
            "Type your question below!"
        )
else:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ── Chat input ─────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything about the college...")

if user_input and user_input.strip():
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    history = [m for m in st.session_state.messages[:-1] if m["role"] in ("user", "assistant")]
    response_text = get_final_response(user_input, history)

    with st.chat_message("assistant"):
        st.markdown(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚡ Quick Questions")
    quick_qs = [
        "How do I apply for admission?",
        "What is the fee structure?",
        "Are scholarships available?",
        "What courses are offered?",
        "Tell me about the hostel",
        "When are the exams?",
        "What is the placement record?",
        "How to check my results?",
        "Library timings?",
        "Campus WiFi details?",
    ]
    for q in quick_qs:
        if st.button(q, key=f"qq_{q}", use_container_width=True):
            resp, _ = get_response(q)
            st.session_state.messages.append({"role": "user", "content": q})
            st.session_state.messages.append({"role": "assistant", "content": resp})
            st.rerun()

    st.divider()

    client = get_groq_client()
    if client:
        st.success("🤖 Groq AI: Connected")
    else:
        st.warning("⚠️ Groq AI: Not configured\nAdd your key to `.streamlit/secrets.toml`")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()