# Seating Arrangement – Data Normalization & Algorithm Prototype

> A data preparation and validation module for automating college exam seating arrangements

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

## About

This prototype module transforms raw exam registration data into a clean, algorithm-ready format for automated seating arrangements. Developed as part of a final year college project, it focuses on **data normalization** and **integrity verification** before seating allocation.

**Key Goal:** Convert unsorted, multi-subject student records into a structured format where each row represents one student taking one subject—eliminating ambiguity and ensuring zero data loss.

---

## Problem Statement

Manual exam seating arrangements at our college face these challenges:

**Current Data Format:**
- One row per student with multiple subjects in columns (Sub1, Sub2, Sub3...)
- Unsorted and not automation-friendly
- Difficult to validate completeness

**Required Format for Automation:**
- One row per student per subject
- Clean, validated, and structured
- Sortable by subject code for hall allocation

**This module bridges that gap.**

---

## Features

### 1. **Data Normalization**
- Converts wide-format CSV (multiple subjects per row) to long-format (one subject per row)
- Dynamically detects subject columns
- Sorts output by subject code for efficient processing

### 2. **Data Verification**
- **Per-student subject count matching:** Ensures each student's subjects are preserved
- **Student coverage validation:** Confirms no students are lost during transformation
- **Engineering-grade checks** before algorithm execution

### 3. **Algorithm Preparation**
- Produces seating-ready data for:
  - Hall distribution algorithms
  - Constraint satisfaction (department/semester separation)
  - Future database integration

---

## Project Structure

```
seating_system/
│
├── data_processing/
│   ├── __init__.py
│   ├── csv_normalizer.py          # Core normalization logic
│   └── verify_normalization.py    # Data integrity verification
│
├── Input_data/                    # Place raw CSV files here
│   └── exam_registration.csv      # (gitignored)
│
├── output_data/                   # Generated normalized CSV
│   └── normalized_output.csv      # (gitignored)
│
├── venv/                          # Virtual environment (gitignored)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/seating-arrangement-prototype.git
cd seating-arrangement-prototype
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Prepare Input Data
Place your raw exam registration CSV file in the `Input_data/` folder. The CSV should have:
- Student identification columns (e.g., Roll No, Name, Department)
- Subject columns (e.g., Sub1, Sub2, Sub3, etc.)

**Example input format:**
```
Roll No,Name,Department,Sub1,Sub2,Sub3
101,John Doe,CSE,CS501,CS502,CS503
102,Jane Smith,ECE,EC401,EC402,
```

### Step 2: Run Normalization
```bash
python data_processing/csv_normalizer.py
```

**What happens:**
- Reads the CSV from `Input_data/`
- Normalizes data (one student-subject pair per row)
- Saves output to `output_data/normalized_output.csv`
- Displays summary statistics

### Step 3: Verify Data Integrity
```bash
python data_processing/verify_normalization.py
```

**What happens:**
- Compares original and normalized data
- Validates subject counts per student
- Confirms zero data loss
- Displays verification report

### Expected Output
```
✓ Normalization successful
✓ Total students: 150
✓ Total subject entries: 450
✓ Verification passed: All students accounted for
```

---

## Technologies Used

- **Python 3.8+** – Core programming language
- **Pandas** – Data manipulation and CSV processing
- **Git/GitHub** – Version control

---

## How This Fits the Main Project

This repository is the **data engineering foundation** for the complete Seating Arrangement Management System.

**Current Phase (This Repo):**
- ✅ Data normalization
- ✅ Integrity verification
- ✅ Algorithm-ready output

**Future Integration:**
- Database storage (PostgreSQL/MySQL)
- Seating allocation algorithm with constraints:
  - Department/semester separation
  - Hall capacity management
  - Invigilator assignment
- Web-based UI for exam cell administrators
- PDF/Excel report generation
- Full system deployment

> **Analogy:** This repo is the "engine testing lab" before building the full vehicle.

---

## Why This Approach?

1. **Separation of Concerns:** Data engineering is isolated from application logic
2. **Algorithm Safety:** Clean input prevents downstream errors
3. **Verifiable:** Engineering-grade checks ensure confidence
4. **Academic Clarity:** Easier to explain during project reviews and viva
5. **Scalable Foundation:** Designed for future database integration

---

## Future Enhancements

- [ ] Database schema design and migration
- [ ] Constraint-based seating algorithm implementation
- [ ] Hall capacity and room allocation logic
- [ ] Invigilator assignment module
- [ ] Web UI for exam cell operations
- [ ] Automated report generation (PDF/Excel)
- [ ] Deployment as a production-ready system

---

## Contributing

This is an academic project, but suggestions and feedback are welcome! Feel free to:
- Open issues for bugs or improvements
- Submit pull requests with enhancements
- Share ideas for better algorithms

---


## Author

**Adhil CR**  
Final Year Student  
Seating Arrangement Management System – College Project

📧 Contact: [m.adhilcr7@gmail.com)  
🔗 GitHub: (https://github.com/Adhil-cr)

---

## Acknowledgments

- College Exam Cell for providing real-world data requirements
- Faculty advisors for project guidance
- Open-source community for Python and Pandas

---

**⭐ If you find this helpful, please star the repository!**
