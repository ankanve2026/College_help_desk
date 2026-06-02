# 🎓 College Help Desk — FAQ Chatbot

A rule-based FAQ chatbot for a college help desk, built with Python, Streamlit, and Groq AI fallback.

---

## 📁 Project Structure

```
faq-chatbot/
│
├── app.py              # Streamlit web app (main UI)
├── chatbot.py          # Terminal/console chatbot
├── responses.py        # All Q&A pairs (16 FAQs)
├── utils.py            # Input cleaning & matching logic
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── secrets.toml    # Groq API key (not committed to git)
└── README.md
```

---

## 🚀 How to Run on VS Code

### Step 1 — Prerequisites

Make sure you have Python 3.10+ installed.  
Check: `python --version`

---

### Step 2 — Clone / Download the Project

```bash
# If using Git:
git clone https://github.com/YOUR_USERNAME/faq-chatbot.git
cd faq-chatbot

# OR just open the folder in VS Code:
# File → Open Folder → select faq-chatbot/
```

---

### Step 3 — Create a Virtual Environment

Open the VS Code terminal (`Ctrl + `` ` `` `) and run:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 5 — Add Your Groq API Key (FREE)

1. Go to **https://console.groq.com** and sign up for free.
2. Create an API key.
3. Open `.streamlit/secrets.toml` and replace the placeholder:

```toml
GROQ_API_KEY = "gsk_your_actual_key_here"
```

> ⚠️ **Never commit secrets.toml to GitHub!**  
> Add it to `.gitignore` if you push to a repo.

---

### Step 6 — Run the Streamlit App

```bash
streamlit run app.py
```

Your browser will open automatically at **http://localhost:8501** 🎉

---

### (Optional) Run the Terminal Chatbot

```bash
python chatbot.py
```

---

## 🧠 How It Works

```
User types a question
        │
        ▼
   clean_input()          ← lowercase, strip punctuation
        │
        ▼
  detect_intent()         ← greeting / farewell / thanks / faq / unknown
        │
   ┌────┴─────┐
   │          │
  FAQ?      Unknown?
   │          │
   ▼          ▼
find_best_match()    →  Groq AI (llama3-8b-8192)
keyword scoring           if API key present
   │          │
   └────┬─────┘
        ▼
   Response displayed
```

### Pattern Matching Algorithm

- Each FAQ has a list of **keyword patterns**.
- The input is cleaned and compared against all patterns.
- **Full phrase match** scores `len(words) × 3` points.
- **Partial word matches** score 1 point per word.
- The FAQ with the **highest score ≥ 1** wins.
- If no match → Groq AI is consulted (if configured).

---

## 💬 Sample Questions to Try

| Question | Category |
|---|---|
| How do I apply for admission? | Admissions |
| What is the fee structure? | Fees |
| Are there any scholarships? | Fees |
| What courses do you offer? | Courses |
| Tell me about the hostel | Hostel |
| When are the semester exams? | Exams |
| How do I check my result? | Exams |
| What is the placement record? | Placement |
| Library timings? | Library |
| Campus WiFi password? | WiFi |
| Any upcoming events? | Events |
| How to get a new ID card? | Student ID |
| What are the bus routes? | Transport |
| What is the attendance rule? | Attendance |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Streamlit | Web UI framework |
| Groq SDK | LLM API (llama3-8b-8192) |
| `re` module | Regex input cleaning |

---

## 📝 Assignment Compliance

| Requirement | Status |
|---|---|
| ≥ 15 FAQ pairs | ✅ 16 FAQs across 8 categories |
| Handle unrecognized inputs | ✅ Groq AI fallback + helpful prompt |
| Interactive interface | ✅ Streamlit UI + terminal mode |
| Pattern matching | ✅ Keyword scoring algorithm |
| Modular project structure | ✅ chatbot.py / responses.py / utils.py |
| README documentation | ✅ This file |
