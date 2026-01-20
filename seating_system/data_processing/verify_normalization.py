import pandas as pd

INPUT_FILE = "/home/adhil-cr/Desktop/Seating arrangment/seating_system/Input_data/StudentExamCenterCourses (7).csv"
OUTPUT_FILE = "/home/adhil-cr/Desktop/Seating arrangment/seating_system/output_data/normalized_sorted_exam_registrations.csv"

print("Starting verification...\n")

df_input = pd.read_csv(INPUT_FILE)
df_output = pd.read_csv(OUTPUT_FILE)

subject_columns = [c for c in df_input.columns if c.startswith("Sub")]

# ----------------------------
# 1.1 AGGREGATED PER-STUDENT SUBJECT COUNT VERIFICATION
# ----------------------------
print("1.1 Verifying aggregated per-student subject counts...")

failed_students = []

# Group input rows by Register No
for reg_no, group in df_input.groupby("Register No"):

    # Count ALL valid subjects across ALL rows for this student
    input_subject_count = 0
    for _, row in group.iterrows():
        input_subject_count += sum(
            pd.notna(row[col]) and str(row[col]).strip() != ""
            for col in subject_columns
        )

    # Count output rows for this student
    output_subject_count = len(
        df_output[df_output["register_no"] == reg_no]
    )

    if input_subject_count != output_subject_count:
        failed_students.append(
            (reg_no, input_subject_count, output_subject_count)
        )

if not failed_students:
    print("✅ Aggregated per-student subject count verification PASSED\n")
else:
    print("❌ Aggregated per-student subject count verification FAILED")
    print("Sample mismatches (Register No, input total, output total):")
    for item in failed_students[:10]:
        print(item)
    print(f"\nTotal mismatched students: {len(failed_students)}\n")

# ----------------------------
# 1.2 STUDENT COVERAGE VERIFICATION
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
