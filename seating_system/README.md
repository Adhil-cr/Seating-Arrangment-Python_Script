Seating Arrangement – Data Normalization & Algorithm Prototype
Overview

This repository is a prototype and testing ground for the Seating Arrangement Management System being developed as our final year college project.

The purpose of this module is not to deliver the full application, but to:
-Analyze real exam registration data used in our college
-Normalize unsorted student–subject data into a system-friendly format
-Verify data integrity rigorously
-Lay the foundation for the seating arrangement algorithm
This repository represents the algorithm design and data preparation phase of the main project.

Problem Statement :

In our college, exam seating arrangements are prepared manually using raw exam registration data where:
-Each student appears once
-Multiple subject codes are stored across columns (Sub1, Sub2, …)
-Data is unsorted and not directly usable for automation
-However, automated seating arrangements require:
-One record per student per subject
-Clean, validated, and structured data
-Confidence that no student or subject is lost during processing
This repository solves that exact problem.

What This Repository Does
1. Data Normalization
-Converts multi-subject-per-row CSV data into:
-One row = one student writing one subject
-Removes ambiguity caused by wide CSV formats

Produces data ready for:
-Seating allocation
-Constraint checks
-Hall distribution

2. Data Verification
-Verifies correctness using engineering-grade checks:
-Per-student subject count matching
-Student coverage validation
-Ensures zero data loss before algorithm execution

3. Algorithm Preparation
-Sorts normalized data by subject code
-Creates a reliable base for:
    -Seating algorithms
    -Constraint satisfaction logic
    -Future database integration

Project Structure
seating_system/
│
├── data_processing/
│   ├── __init__.py
│   ├── csv_normalizer.py        # Core normalization logic
│   └── verify_normalization.py # Data integrity verification
│
├── Input_data/                 # Raw exam registration CSV (ignored by Git)
│
├── output_data/                # Generated normalized CSV (ignored by Git)
│
├── venv/                       # Python virtual environment (ignored by Git)
│
├── .gitignore
└── README.md

Scripts Explained

csv_normalizer.py

-Reads raw exam registration CSV
-Detects subject columns dynamically
-Normalizes data into one record per student per subject
-Sorts output by subject code
-Writes clean, seating-ready CSV
This script represents the data preparation stage of the seating system.

verify_normalization.py

-Verifies normalization correctness using:
-Per-student subject count comparison
-Student coverage checks
-Ensures output data is a faithful transformation of input data
This script ensures algorithm safety before proceeding to seating logic.

How This Fits into the Main Project
This repository is a preparatory and experimental phase of the main Seating Arrangement Management System.

In the full project:

This logic will be integrated into the backend

Normalized data will be stored in a database

Seating algorithms will:

Apply department and semester separation

Respect hall capacities

Assign invigilators

Generate seating charts and reports

Think of this repo as:

“The engine testing lab before building the full vehicle.”

Technologies Used

Python 3

Pandas

Git & GitHub

Why This Approach

Separates data engineering from application logic

Prevents algorithm errors caused by dirty input

Makes the seating algorithm:

Simpler

Safer

Easier to explain in reviews and viva

Academic Context

This work is part of our Final Year College Project and focuses specifically on:

Algorithm design

Data normalization

Validation strategies

Real-world exam data handling

Future Work

Database schema design

Seating arrangement algorithm with constraints

Web-based UI for exam cell usage

PDF/Excel report generation

Deployment as a complete system

Author

Adhil CR
Final Year Student
Seating Arrangement Management System – College Project