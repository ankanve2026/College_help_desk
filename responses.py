# """
# responses.py
# All FAQ Q&A pairs and response bank for the College Help Desk chatbot.
# """

# FAQ_DATA = [
#     {
#         "id": 1,
#         "category": "Admissions",
#         "patterns": [
#             "how to apply", "admission process", "apply for admission",
#             "how do i get admitted", "application procedure", "enroll"
#         ],
#         "response": (
#             "🎓 **Admission Process**\n\n"
#             "1. Visit our official website and fill out the online application form.\n"
#             "2. Upload required documents: 10th & 12th marksheets, ID proof, passport photo.\n"
#             "3. Pay the application fee (₹500 online).\n"
#             "4. Await confirmation email within 3–5 working days.\n\n"
#             "📞 For help: admissions@college.edu"
#         ),
#     },
#     {
#         "id": 2,
#         "category": "Admissions",
#         "patterns": [
#             "last date", "application deadline", "when is the last date",
#             "deadline for admission", "closing date"
#         ],
#         "response": (
#             "📅 **Application Deadline**\n\n"
#             "The last date to apply for the current academic year is **July 31st**.\n"
#             "Late applications may be considered on a case-by-case basis.\n"
#             "We recommend applying at least 2 weeks before the deadline."
#         ),
#     },
#     {
#         "id": 3,
#         "category": "Fees",
#         "patterns": [
#             "fee structure", "tuition fee", "how much is the fee",
#             "course fee", "fees", "cost of course", "semester fee"
#         ],
#         "response": (
#             "💰 **Fee Structure (Per Semester)**\n\n"
#             "| Programme | Fee (INR) |\n"
#             "|-----------|----------|\n"
#             "| B.Tech     | ₹75,000  |\n"
#             "| BCA        | ₹45,000  |\n"
#             "| MBA        | ₹90,000  |\n"
#             "| B.Sc       | ₹30,000  |\n\n"
#             "Fees include tuition, library, and lab charges.\n"
#             "📧 finance@college.edu for payment plans."
#         ),
#     },
#     {
#         "id": 4,
#         "category": "Fees",
#         "patterns": [
#             "scholarship", "financial aid", "fee waiver",
#             "discount on fees", "merit scholarship", "need based aid"
#         ],
#         "response": (
#             "🏅 **Scholarships & Financial Aid**\n\n"
#             "We offer the following scholarships:\n"
#             "- **Merit Scholarship**: 50% fee waiver for students with 90%+ in board exams.\n"
#             "- **Sports Quota**: 25% waiver for state/national level athletes.\n"
#             "- **Need-Based Aid**: Apply with family income certificate at the finance office.\n\n"
#             "Deadline: Apply within 30 days of admission."
#         ),
#     },
#     {
#         "id": 5,
#         "category": "Courses",
#         "patterns": [
#             "courses offered", "programmes available", "what courses",
#             "list of courses", "departments", "which subjects"
#         ],
#         "response": (
#             "📚 **Courses Offered**\n\n"
#             "**Undergraduate:**\n"
#             "- B.Tech (CS, IT, ECE, Mechanical, Civil)\n"
#             "- BCA, B.Sc (Physics, Chemistry, Maths)\n"
#             "- BBA, B.Com\n\n"
#             "**Postgraduate:**\n"
#             "- MBA, MCA, M.Tech, M.Sc\n\n"
#             "Visit /academics on our website for full syllabus details."
#         ),
#     },
#     {
#         "id": 6,
#         "category": "Hostel",
#         "patterns": [
#             "hostel", "accommodation", "hostel facility", "boarding",
#             "hostel fees", "staying on campus", "dorm"
#         ],
#         "response": (
#             "🏠 **Hostel Facilities**\n\n"
#             "We provide separate hostels for boys and girls.\n"
#             "- **Capacity**: 500 students\n"
#             "- **Facilities**: WiFi, mess, laundry, gym, 24/7 security\n"
#             "- **Fee**: ₹40,000/semester (includes mess)\n\n"
#             "Seats are limited — apply early through the hostel office.\n"
#             "📧 hostel@college.edu"
#         ),
#     },
#     {
#         "id": 7,
#         "category": "Exams",
#         "patterns": [
#             "exam schedule", "when are exams", "exam timetable",
#             "semester exam", "exam date", "when is the exam"
#         ],
#         "response": (
#             "📝 **Exam Schedule**\n\n"
#             "- **Mid-Semester Exams**: October (Sem 1) / March (Sem 2)\n"
#             "- **End-Semester Exams**: December (Sem 1) / May (Sem 2)\n\n"
#             "Timetables are published on the student portal 3 weeks in advance.\n"
#             "🔗 portal.college.edu → Academics → Timetable"
#         ),
#     },
#     {
#         "id": 8,
#         "category": "Exams",
#         "patterns": [
#             "result", "how to check result", "marks", "grade",
#             "scorecard", "result portal", "check my result"
#         ],
#         "response": (
#             "📊 **Checking Your Results**\n\n"
#             "1. Visit **portal.college.edu**\n"
#             "2. Login with your Student ID and password.\n"
#             "3. Navigate to **Results → Semester Results**.\n"
#             "4. Download your marksheet (PDF).\n\n"
#             "Results are typically published within 3 weeks of the last exam."
#         ),
#     },
#     {
#         "id": 9,
#         "category": "Library",
#         "patterns": [
#             "library", "library hours", "library timing",
#             "books", "library access", "library facilities"
#         ],
#         "response": (
#             "📖 **Library Information**\n\n"
#             "- **Location**: Block C, Ground Floor\n"
#             "- **Timings**: Mon–Sat, 8:00 AM – 8:00 PM\n"
#             "- **Collection**: 50,000+ books, 200+ journals, e-library access\n"
#             "- **Borrowing**: Up to 3 books for 14 days\n\n"
#             "Use your Student ID card to borrow books."
#         ),
#     },
#     {
#         "id": 10,
#         "category": "Placement",
#         "patterns": [
#             "placement", "job", "campus recruitment", "placement cell",
#             "companies", "internship", "career", "placement record"
#         ],
#         "response": (
#             "💼 **Placement & Careers**\n\n"
#             "- **Average Package**: ₹6.5 LPA (2024 batch)\n"
#             "- **Highest Package**: ₹28 LPA\n"
#             "- **Top Recruiters**: TCS, Infosys, Wipro, Amazon, Deloitte\n"
#             "- **Placement Rate**: 92% (2024)\n\n"
#             "The Placement Cell conducts pre-placement training, mock interviews, and resume workshops.\n"
#             "📧 placements@college.edu"
#         ),
#     },
#     {
#         "id": 11,
#         "category": "Transport",
#         "patterns": [
#             "bus", "transport", "college bus", "how to reach",
#             "bus route", "shuttle", "commute", "transportation"
#         ],
#         "response": (
#             "🚌 **College Transport**\n\n"
#             "We operate 15 bus routes covering major city areas.\n"
#             "- **Fee**: ₹8,000/semester\n"
#             "- **Timings**: Pickup 7:30 AM | Drop 5:30 PM\n\n"
#             "Check full route list on the Transport Office notice board or website."
#         ),
#     },
#     {
#         "id": 12,
#         "category": "Attendance",
#         "patterns": [
#             "attendance", "attendance requirement", "minimum attendance",
#             "attendance shortage", "attendance rule", "proxy"
#         ],
#         "response": (
#             "✅ **Attendance Policy**\n\n"
#             "- **Minimum Required**: 75% per subject per semester.\n"
#             "- Below 75% → Detained from semester exams.\n"
#             "- Medical leave must be supported with a doctor's certificate.\n"
#             "- Attendance is updated daily on the student portal.\n\n"
#             "Talk to your class advisor if you have an attendance shortage."
#         ),
#     },
#     {
#         "id": 13,
#         "category": "Contact",
#         "patterns": [
#             "contact", "phone number", "email", "address",
#             "how to contact", "reach the college", "office number", "helpdesk"
#         ],
#         "response": (
#             "📞 **Contact Information**\n\n"
#             "- **Address**: 123 Knowledge Park, Tech City – 700001\n"
#             "- **Phone**: +91-33-1234-5678\n"
#             "- **Email**: info@college.edu\n"
#             "- **Admissions**: admissions@college.edu\n"
#             "- **Portal**: portal.college.edu\n\n"
#             "Office Hours: Mon–Fri, 9:00 AM – 5:00 PM"
#         ),
#     },
#     {
#         "id": 14,
#         "category": "Student ID",
#         "patterns": [
#             "student id", "id card", "lost id card", "id card process",
#             "reissue id", "new id card", "how to get id card"
#         ],
#         "response": (
#             "🪪 **Student ID Card**\n\n"
#             "- New students receive their ID within 2 weeks of admission.\n"
#             "- **Lost card?** Submit a written application + ₹200 fee at the Admin Office.\n"
#             "- Replacement takes 3–5 working days.\n"
#             "- Your ID is required for exams, library, and hostel access."
#         ),
#     },
#     {
#         "id": 15,
#         "category": "WiFi",
#         "patterns": [
#             "wifi", "internet", "campus wifi", "wi-fi",
#             "internet access", "network", "broadband"
#         ],
#         "response": (
#             "📶 **Campus WiFi**\n\n"
#             "- Free high-speed WiFi (100 Mbps) across all campus buildings.\n"
#             "- **SSID**: CollegeCampus\n"
#             "- Login with your student email ID and portal password.\n"
#             "- IT Helpdesk: it@college.edu | Ext: 1050 (9 AM – 6 PM)"
#         ),
#     },
#     {
#         "id": 16,
#         "category": "Events",
#         "patterns": [
#             "events", "fest", "cultural", "techfest", "annual fest",
#             "college events", "activities", "extracurricular", "clubs"
#         ],
#         "response": (
#             "🎉 **Events & Extracurriculars**\n\n"
#             "- **TechFest** (January): National-level tech competition\n"
#             "- **Culturals** (February): Dance, music, drama, art\n"
#             "- **Sports Week** (November): Inter-college tournaments\n\n"
#             "We have 30+ student clubs: Coding, Robotics, Photography, Drama, etc.\n"
#             "Join via the Student Affairs Office or student portal."
#         ),
#     },
#     {
#     "id": 17,
#     "category": "Contact",
#     "patterns": [
#         "exact location", "exact place", "where is the college",
#         "college address", "location of college", "how to reach",
#         "where are you located", "college location"
#     ],
#     "response": (
#         "📍 **College Location**\n\n"
#         "**Address**: YOUR REAL ADDRESS HERE\n"
#         "**City**: Your City\n"
#         "**Landmark**: Near XYZ\n\n"
#         "📞 +91-XXXXXXXXXX"
#         ),
#     },
# ]

# GREETINGS = ["hi", "hello", "hey", "good morning", "good afternoon",
#              "good evening", "howdy", "greetings", "hii", "helo"]

# FAREWELLS = ["bye", "goodbye", "see you", "later", "exit", "quit",
#              "take care", "farewell", "good night", "thanks bye"]

# THANKS = ["thank you", "thanks", "thank u", "thx", "ty", "great thanks",
#           "awesome thanks", "many thanks"]




"""
responses.py
FAQ Q&A pairs for MCKV Institute of Engineering, Liluah, Howrah.
"""

FAQ_DATA = [
    # ── 1. Admissions ──────────────────────────────────────────────────────────
    {
        "id": 1,
        "category": "Admissions",
        "patterns": [
            "how to apply", "admission process", "apply for admission",
            "how do i get admitted", "application procedure", "enroll",
            "how to take admission", "admission form", "online admission"
        ],
        "response": (
            "🎓 **Admission Process at MCKVIE**\n\n"
            "1. Visit **www.mckvie.edu.in** → Admissions → Online Admission.\n"
            "2. Register and fill out the application form.\n"
            "3. Upload required documents: 10th & 12th marksheets, entrance scorecard, ID proof, passport photo.\n"
            "4. Pay the application fee (₹1,000–₹2,500 depending on course).\n"
            "5. Attend counselling/GD-PI as applicable.\n\n"
            "**Accepted Exams:** WBJEE / JEE Main (B.Tech) · PGET (M.Tech) · CAT / MAT / XAT / JEMAT (MBA)\n\n"
            "📧 admissions@mckvie.edu.in · 📞 033-2654-9315"
        ),
    },
    {
        "id": 2,
        "category": "Admissions",
        "patterns": [
            "last date", "application deadline", "when is the last date",
            "deadline for admission", "closing date", "admission date"
        ],
        "response": (
            "📅 **Admission Deadlines at MCKVIE**\n\n"
            "- **B.Tech**: Follows WBJEE / JEE Main counselling schedule (typically June–August).\n"
            "- **M.Tech**: Based on PGET results (July–August).\n"
            "- **MBA**: Follows CAT / MAT / XAT results (January–March).\n\n"
            "Exact dates are announced on the official website.\n"
            "🌐 www.mckvie.edu.in/admissions"
        ),
    },
    {
        "id": 3,
        "category": "Admissions",
        "patterns": [
            "eligibility", "eligibility criteria", "qualification required",
            "marks required for admission", "cutoff marks", "minimum marks"
        ],
        "response": (
            "✅ **Eligibility Criteria at MCKVIE**\n\n"
            "**B.Tech:**\n"
            "- 10+2 with Physics, Chemistry & Maths — minimum **45%** (40% for reserved categories)\n"
            "- Valid WBJEE or JEE Main rank\n\n"
            "**M.Tech (ECE):**\n"
            "- B.E/B.Tech in ECE or M.Sc in Electronics/Physics\n"
            "- Valid PGET score\n\n"
            "**MBA:**\n"
            "- Any graduation with valid CAT / MAT / XAT / JEMAT score\n\n"
            "**JEE Main Cutoff (2024, General):** 37,194 – 1,09,989"
        ),
    },

    # ── 2. Fees ────────────────────────────────────────────────────────────────
    {
        "id": 4,
        "category": "Fees",
        "patterns": [
            "fee structure", "tuition fee", "how much is the fee",
            "course fee", "fees", "cost of course", "semester fee",
            "how much fees", "btech fees", "fee per semester"
        ],
        "response": (
            "💰 **Fee Structure at MCKVIE (2024–25)**\n\n"
            "| Programme | Per Semester | Total Course |\n"
            "|-----------|-------------|---------------|\n"
            "| B.Tech    | ≈ ₹50,000–59,000 | ≈ ₹5.09 Lakh |\n"
            "| M.Tech    | ≈ ₹63,000 (1st yr) | — |\n"
            "| MBA       | ≈ ₹2.3 Lakh (1st yr) | ≈ ₹3.75 Lakh |\n"
            "| BBA       | — | ≈ ₹3.55 Lakh |\n\n"
            "**One-time charges at admission:**\n"
            "Admission Fee ₹6,000 · Library Fee ₹6,000 · Caution Deposit ₹10,000 (refundable) · Student Activity Fee ₹4,000\n\n"
            "📄 Download exact fee sheet: www.mckvie.edu.in/fees-structure"
        ),
    },
    {
        "id": 5,
        "category": "Fees",
        "patterns": [
            "scholarship", "financial aid", "fee waiver", "tfws",
            "discount on fees", "merit scholarship", "need based aid",
            "swami vivekananda scholarship", "kanyashree", "aikyashree"
        ],
        "response": (
            "🏅 **Scholarships at MCKVIE**\n\n"
            "**Government Schemes:**\n"
            "- Swami Vivekananda Merit-cum-Means Scholarship\n"
            "- Aikyashree Scholarship (minority students)\n"
            "- Kanyashree (girl students)\n"
            "- National Scholarship Portal (NSP)\n"
            "- DWO & MAKAUT Scholarships\n\n"
            "**Institute Schemes:**\n"
            "- Merit-based scholarships for top academic performers\n"
            "- TFWS (Tuition Fee Waiver Scheme) — full tuition waiver for eligible students\n"
            "- Up to 100% scholarship for outstanding students\n\n"
            "📧 Contact the Scholarship Cell via www.mckvie.edu.in"
        ),
    },

    # ── 3. Courses ─────────────────────────────────────────────────────────────
    {
        "id": 6,
        "category": "Courses",
        "patterns": [
            "courses offered", "programmes available", "what courses",
            "list of courses", "departments", "which subjects",
            "btech branches", "specializations", "what can i study"
        ],
        "response": (
            "📚 **Courses Offered at MCKVIE**\n\n"
            "**B.Tech (4 years) — 8 Specialisations:**\n"
            "- Computer Science & Engineering (CSE)\n"
            "- CSE (Data Science)\n"
            "- CSE (AI & ML)\n"
            "- Information Technology (IT)\n"
            "- Electronics & Communication Engineering (ECE)\n"
            "- Electrical Engineering (EE)\n"
            "- Mechanical Engineering (ME)\n"
            "- Automobile Engineering (AUE)\n\n"
            "**Postgraduate:**\n"
            "- M.Tech (ECE)\n"
            "- MBA (Finance, HR, Marketing, Business Analytics, Hospital Admin, Pharma Mgmt)\n\n"
            "**Other:**\n"
            "- BBA · B.Voc (Software Development, Automobile Servicing)\n\n"
            "🌐 www.mckvie.edu.in/academics"
        ),
    },

    # ── 4. Hostel ──────────────────────────────────────────────────────────────
    {
        "id": 7,
        "category": "Hostel",
        "patterns": [
            "hostel", "accommodation", "hostel facility", "boarding",
            "hostel fees", "staying on campus", "dorm", "boys hostel",
            "girls hostel", "pg near college", "hostel rent"
        ],
        "response": (
            "🏠 **Hostel Facilities at MCKVIE**\n\n"
            "- **Boys Hostel**: Located outside the campus\n"
            "- **Girls Hostel**: Located inside the campus\n"
            "- **Hostel Fee**: ₹3,300/month seat rent (increases 10% every year)\n"
            "- **With food**: approx ₹6,000–₹6,500/month\n"
            "- **Facilities**: Mess, clean rooms, security\n\n"
            "**PG options** near college: approx ₹3,500/month\n\n"
            "📧 Contact hostel office via www.mckvie.edu.in\n"
            "Seats are limited — apply early after admission."
        ),
    },

    # ── 5. Exams ───────────────────────────────────────────────────────────────
    {
        "id": 8,
        "category": "Exams",
        "patterns": [
            "exam schedule", "when are exams", "exam timetable",
            "semester exam", "exam date", "when is the exam",
            "exam timing", "university exam"
        ],
        "response": (
            "📝 **Exam Schedule at MCKVIE**\n\n"
            "MCKVIE is affiliated with **MAKAUT** (Maulana Abul Kalam Azad University of Technology).\n"
            "Semester exam dates are set by MAKAUT and published on the student portal.\n\n"
            "- **Class timings**: 9:30 AM – 5:00 PM\n"
            "- **Mid-semester assessments**: conducted by departments\n"
            "- **End-semester exams**: as per MAKAUT schedule\n\n"
            "🌐 Check timetable: www.mckvie.edu.in → Academics → Examination"
        ),
    },
    {
        "id": 9,
        "category": "Exams",
        "patterns": [
            "result", "how to check result", "marks", "grade",
            "scorecard", "result portal", "check my result", "marksheet"
        ],
        "response": (
            "📊 **Checking Your Results**\n\n"
            "Results for MCKVIE students are published by **MAKAUT**.\n\n"
            "1. Visit **makautwb.ac.in** or the MCKVIE student portal.\n"
            "2. Login with your university roll number.\n"
            "3. Select your semester and view/download results.\n\n"
            "Results are typically published 3–4 weeks after the last exam.\n"
            "For internal marks, check with your respective department."
        ),
    },

    # ── 6. Attendance ──────────────────────────────────────────────────────────
    {
        "id": 10,
        "category": "Attendance",
        "patterns": [
            "attendance", "attendance requirement", "minimum attendance",
            "attendance shortage", "attendance rule", "proxy", "attendance percentage"
        ],
        "response": (
            "✅ **Attendance Policy at MCKVIE**\n\n"
            "- **Minimum Required**: 75% per subject per semester.\n"
            "- Below 75% → Detained from end-semester exams (as per MAKAUT rules).\n"
            "- Medical leave must be supported by a valid doctor's certificate.\n"
            "- Attendance is tracked and updated regularly.\n\n"
            "Talk to your class advisor or department HOD if you have a shortage."
        ),
    },

    # ── 7. Placement ───────────────────────────────────────────────────────────
    {
        "id": 11,
        "category": "Placement",
        "patterns": [
            "placement", "job", "campus recruitment", "placement cell",
            "companies", "internship", "career", "placement record",
            "average package", "highest package", "top recruiters"
        ],
        "response": (
            "💼 **Placements at MCKVIE**\n\n"
            "- **Placement Rate (2024)**: ~85–88%\n"
            "- **Median Package (2024)**: ₹5.2 LPA\n"
            "- **Highest Package**: ₹20 LPA\n\n"
            "**Top Recruiters:**\n"
            "TCS · Infosys · Wipro · Cognizant · Capgemini · HCL · Amazon · Bosch · L&T · Hitachi · Ericsson · Toshiba · Tata Steel · Zycus\n\n"
            "The Placement Cell conducts pre-placement training, mock interviews, resume workshops and industry visits.\n"
            "📧 placements@mckvie.edu.in"
        ),
    },

    # ── 8. Library ─────────────────────────────────────────────────────────────
    {
        "id": 12,
        "category": "Library",
        "patterns": [
            "library", "library hours", "library timing",
            "books", "library access", "library facilities", "central library"
        ],
        "response": (
            "📖 **Library at MCKVIE**\n\n"
            "- **Collection**: 39,000+ textbooks and reference books covering all engineering disciplines\n"
            "- Subscribes to national and international journals\n"
            "- Digital library & e-resources access available\n"
            "- Clean, quiet study environment\n\n"
            "Use your Student ID card to borrow books.\n"
            "📍 Located inside the main campus building."
        ),
    },

    # ── 9. Transport ───────────────────────────────────────────────────────────
    {
        "id": 13,
        "category": "Transport",
        "patterns": [
            "bus", "transport", "college bus", "how to reach",
            "bus route", "shuttle", "commute", "transportation",
            "from howrah station", "from kolkata"
        ],
        "response": (
            "🚌 **How to Reach MCKVIE**\n\n"
            "**By Train:**\n"
            "- 1 km from **Liluah Railway Station** (nearest)\n"
            "- 5 km from **Howrah Railway Station**\n\n"
            "**By Bus (from Howrah Station area):**\n"
            "Route No. **51, 54, 54/2, 56**, Howrah–Belurmath mini bus, Ballykhal–Khidderpore mini bus\n\n"
            "**By Auto/Toto:**\n"
            "Direct autos from Howrah, Saalkia–Badhaghat side or from Ballykhal\n\n"
            "**By Cab/Taxi:**\n"
            "Available from anywhere in Kolkata or Howrah (16.4 km from Airport)\n\n"
            "📍 243, G.T. Road (North), Liluah, Howrah – 711204"
        ),
    },

    # ── 10. Location ───────────────────────────────────────────────────────────
    {
        "id": 14,
        "category": "Location",
        "patterns": [
            "exact location", "exact place", "where is the college",
            "college address", "location of college", "where are you located",
            "college location", "address of college", "campus location",
            "find the college", "where is mckvie", "mckvie address"
        ],
        "response": (
            "📍 **MCKV Institute of Engineering**\n\n"
            "**Address**: 243, G.T. Road (North), Liluah, Howrah – 711204\n"
            "**District**: Howrah, West Bengal, India\n"
            "**Landmark**: Near Don Bosco School, Liluah\n\n"
            "🚉 **Distances:**\n"
            "- 1 km from Liluah Railway Station\n"
            "- 5 km from Howrah Railway Station\n"
            "- 16.4 km from Netaji Subhash Chandra Bose International Airport\n\n"
            "📞 +91-33-2654-9315 / 9317\n"
            "🌐 www.mckvie.edu.in"
        ),
    },

    # ── 11. Contact ────────────────────────────────────────────────────────────
    {
        "id": 15,
        "category": "Contact",
        "patterns": [
            "contact", "phone number", "email", "address",
            "how to contact", "reach the college", "office number",
            "helpdesk", "contact details", "official email"
        ],
        "response": (
            "📞 **Contact MCKVIE**\n\n"
            "- **Address**: 243, G.T. Road (North), Liluah, Howrah – 711204\n"
            "- **Phone**: +91-33-2654-9315 / 9317\n"
            "- **Fax**: +91-33-2654-9318\n"
            "- **Principal**: principal@mckvie.edu.in\n"
            "- **General**: mckvie@vsnl.net\n"
            "- **Website**: www.mckvie.edu.in\n\n"
            "🕘 Office Hours: Mon–Sat, 9:30 AM – 5:00 PM"
        ),
    },

    # ── 12. WiFi / Infrastructure ──────────────────────────────────────────────
    {
        "id": 16,
        "category": "Infrastructure",
        "patterns": [
            "wifi", "internet", "campus wifi", "wi-fi",
            "internet access", "network", "labs", "infrastructure",
            "computer lab", "facilities"
        ],
        "response": (
            "📶 **Campus Infrastructure at MCKVIE**\n\n"
            "- **WiFi**: Available in the college library and select areas\n"
            "- **Classrooms**: 47 fully equipped classrooms\n"
            "- **Labs**: 64 well-equipped laboratories\n"
            "- **Computer Labs**: High-spec PCs with latest configurations\n"
            "- **Library**: 39,000+ books + e-resources\n"
            "- **Language & Communication Lab**\n"
            "- **Cafeteria**, **Meditation Hall**, **Healthcare Unit**, **Gym**\n"
            "- **Students' Common Room**\n\n"
            "For IT issues, contact the IT department via the admin office."
        ),
    },

    # ── 13. Events / Fest ──────────────────────────────────────────────────────
    {
        "id": 17,
        "category": "Events",
        "patterns": [
            "events", "fest", "cultural", "techfest", "annual fest",
            "college events", "activities", "extracurricular", "clubs",
            "utopia", "annual function", "college festival"
        ],
        "response": (
            "🎉 **Events & Extracurriculars at MCKVIE**\n\n"
            "- **UTOPIA**: The flagship annual college fest featuring technical and cultural competitions\n"
            "- **Sports Meet**: Inter-college tournaments\n"
            "- **Technical Events**: Workshops, hackathons, seminars by industry experts\n\n"
            "**Clubs & Associations:**\n"
            "- **Rotaract Club of MCKVIE** — 2nd best club in Howrah district\n"
            "- Various departmental clubs (Coding, Robotics, etc.)\n\n"
            "All festivals are celebrated on campus with great enthusiasm!\n"
            "Join via the Student Affairs Office."
        ),
    },

    # ── 14. Student ID ─────────────────────────────────────────────────────────
    {
        "id": 18,
        "category": "Student ID",
        "patterns": [
            "student id", "id card", "lost id card", "id card process",
            "reissue id", "new id card", "how to get id card", "identity card"
        ],
        "response": (
            "🪪 **Student ID Card at MCKVIE**\n\n"
            "- New students receive their ID card within the first few weeks of admission.\n"
            "- **Lost card?** Submit a written application with a fee at the Admin Office.\n"
            "- Replacement takes 3–5 working days.\n"
            "- Your ID is required for exams, library access, and hostel entry.\n\n"
            "📍 Admin Office: Main building, Ground Floor."
        ),
    },

    # ── 15. About MCKVIE ───────────────────────────────────────────────────────
    {
        "id": 19,
        "category": "About",
        "patterns": [
            "about college", "about mckvie", "about mckv",
            "history of college", "when was college established",
            "college info", "tell me about the college",
            "naac", "ranking", "accreditation", "affiliation", "makaut"
        ],
        "response": (
            "🏫 **About MCKV Institute of Engineering (MCKVIE)**\n\n"
            "- **Established**: 1999\n"
            "- **Type**: Private, Self-funded · Autonomous Institute\n"
            "- **Motto**: *Engineering Minds*\n"
            "- **Affiliation**: MAKAUT (Maulana Abul Kalam Azad University of Technology)\n"
            "- **Approvals**: AICTE · Dept. of Higher Education, Govt. of WB\n"
            "- **Accreditation**: NAAC Grade **'A'** · NBA accredited B.Tech programmes\n\n"
            "**Rankings:**\n"
            "- NIRF 2024: Band 201–250 (Engineering)\n"
            "- India Today 2024: #229 among private engineering colleges\n\n"
            "**Students**: ~1,500 · **Faculty**: 150+ · **Campus**: Urban, Liluah, Howrah"
        ),
    },

    # ── 16. Campus Life ────────────────────────────────────────────────────────
    {
        "id": 20,
        "category": "Campus Life",
        "patterns": [
            "campus life", "college life", "campus environment",
            "campus atmosphere", "student life", "how is the campus",
            "campus facilities", "sports", "meditation", "cafeteria", "canteen",
            "campus vibe", "campus infrastructure", "what is campus like",
            "about campus", "campus details"
        ],
        "response": (
            "🌟 **Campus Life at MCKVIE**\n\n"
            "The campus is known for its peaceful, disciplined, and lively atmosphere.\n\n"
            "**Facilities:**\n"
            "- Cafeteria / Canteen with good food\n"
            "- Meditation Hall\n"
            "- Healthcare Unit / Medical Room\n"
            "- Gym & Fitness Centre\n"
            "- Sports facilities\n"
            "- Students' Common Room\n"
            "- Beautiful, clean campus buildings and premises\n\n"
            "All festivals are celebrated with enthusiasm, and students often look back fondly at their time here! 🎓"
        ),
    },
]

GREETINGS = ["hi", "hello", "hey", "good morning", "good afternoon",
             "good evening", "howdy", "greetings", "hii", "helo", "namaskar"]

FAREWELLS = ["bye", "goodbye", "see you", "later", "exit", "quit",
             "take care", "farewell", "good night", "thanks bye"]

THANKS = ["thank you", "thanks", "thank u", "thx", "ty", "great thanks",
          "awesome thanks", "many thanks", "shukriya", "dhanyabad"]