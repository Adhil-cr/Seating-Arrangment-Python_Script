import pandas as pd

INPUT_FILE = "/home/adhil-cr/Desktop/Seating arrangment/seating_system/Input_data/StudentExamCenterCourses (7).csv"
OUTPUT_FILE = "/home/adhil-cr/Desktop/Seating arrangment/seating_system/output_data/normalized_sorted_exam_registrations.csv"

print("Starting verification...\n")

# Load data
df_input = pd.read_csv(INPUT_FILE)
df_output = pd.read_csv(OUTPUT_FILE)

subject_columns = [c for c in df_input.columns if c.startswith("Sub")]

# ----------------------------
# 1.1 PER-STUDENT SUBJECT COUNT VERIFICATION
# ----------------------------
print("1.1 Verifying per-student subject counts...")

failed_students = []

for _, row in df_input.iterrows():
    reg_no = row["Register No"]

    input_subject_count = sum(
        pd.notna(row[col]) and str(row[col]).strip() != ""
        for col in subject_columns
    )

    output_subject_count = len(
        df_output[df_output["register_no"] == reg_no]
    )

    if input_subject_count != output_subject_count:
        failed_students.append(
            (reg_no, input_subject_count, output_subject_count)
        )

if not failed_students:
    print("✅ Per-student subject count verification PASSED\n")
else:
    print("❌ Per-student subject count verification FAILED")
    print("Sample mismatches:")
    for item in failed_students[:10]:
        print(item)
    print(f"Total mismatched students: {len(failed_students)}\n")

# ----------------------------
# 1.2 STUDENT COVERAGE
# ----------------------------
print("1.2 Verifying student coverage...")

input_students = set(df_input["Register No"])
output_students = set(df_output["register_no"])

missing_students = input_students - output_students

if not missing_students:
    print("✅ Student coverage verification PASSED\n")
else:
    print("❌ Student coverage verification FAILED")
    print("Missing students:", missing_students)
