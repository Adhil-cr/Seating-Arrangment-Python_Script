import os
import pandas as pd
from collections import defaultdict, deque


# ============================================================
# Public Orchestrator
# ============================================================

def allocate_seating(
    prepared_csv_path: str,
    output_dir: str,
    seating_config: dict
) -> str:

    # ----------------------------
    # Step 1: Load prepared data
    # ----------------------------
    df = pd.read_csv(prepared_csv_path)

    required_cols = {
        "register_no",
        "student_name",
        "department",
        "subject_code",
        "exam_date",
        "session"
    }
    if not required_cols.issubset(df.columns):
        raise ValueError("Prepared CSV schema mismatch.")

    df["register_no"] = df["register_no"].astype(int)
    df["subject_code"] = df["subject_code"].astype(str)

    # ----------------------------
    # Step 2: Read configuration
    # ----------------------------
    number_of_halls = seating_config["number_of_halls"]
    hall_capacity = seating_config["hall_capacity"]
    max_subject_per_hall = seating_config["max_subject_per_hall"]

    if hall_capacity % 2 != 0:
        raise ValueError("Hall capacity must be even.")

    # ----------------------------
    # Step 3: Allocate students (HYBRID + SUBJECT SPREAD)
    # ----------------------------
    halls = _allocate_students_to_halls_hybrid(
        df,
        number_of_halls,
        hall_capacity,
        max_subject_per_hall
    )

    # ----------------------------
    # Step 4: Sort by department & register_no (FIX 1)
    # ----------------------------
    for hall in halls:
        hall["seats"] = _sort_hall_seats_by_department_and_register(hall["seats"])

    # ----------------------------
    # Step 5: Bench reordering (FIX 1 continued)
    # ----------------------------
    for hall in halls:
        hall["seats"] = _reorder_hall_seats_by_bench(hall["seats"])

    # ----------------------------
    # Step 6: Generate output
    # ----------------------------
    output_rows = _generate_output_rows(halls)
    output_df = pd.DataFrame(output_rows)

    os.makedirs(output_dir, exist_ok=True)
    exam_date = df.iloc[0]["exam_date"]
    session = df.iloc[0]["session"]

    filename = f"seat_allocated_exam_session_{exam_date}_{session}.csv"
    output_path = os.path.join(output_dir, filename)
    output_df.to_csv(output_path, index=False)

    return output_path


# ============================================================
# Allocation Logic (FIX 2)
# ============================================================

def _allocate_students_to_halls_hybrid(
    df,
    number_of_halls,
    hall_capacity,
    max_subject_per_hall
):
    halls = []
    for hid in range(1, number_of_halls + 1):
        halls.append({
            "hall_id": hid,
            "occupied": 0,
            "subject_counts": defaultdict(int),
            "seats": []
        })

    # Group & sort students per subject
    subject_groups = defaultdict(list)
    for _, row in df.iterrows():
        subject_groups[row["subject_code"]].append(row)

    for subject in subject_groups:
        subject_groups[subject].sort(
            key=lambda r: (r["department"], r["register_no"])
        )

    subject_queues = {
        s: deque(students)
        for s, students in subject_groups.items()
    }

    hall_index = 0

    while any(subject_queues.values()):
        for subject, queue in subject_queues.items():
            if not queue:
                continue

            student = queue[0]
            placed = False

            for attempt in range(number_of_halls):
                hall = halls[(hall_index + attempt) % number_of_halls]

                if hall["occupied"] >= hall_capacity:
                    continue

                if hall["subject_counts"][subject] >= max_subject_per_hall:
                    continue

                hall["seats"].append({
                    "register_no": student["register_no"],
                    "student_name": student["student_name"],
                    "department": student["department"],
                    "subject_code": subject
                })

                hall["occupied"] += 1
                hall["subject_counts"][subject] += 1
                queue.popleft()

                if hall["occupied"] >= hall_capacity:
                    hall_index = (halls.index(hall) + 1) % number_of_halls

                placed = True
                break

            if not placed:
                raise ValueError(
                    f"Cannot allocate subject {subject}; constraints too strict."
                )

    return halls


# ============================================================
# Seating Helpers
# ============================================================

def _sort_hall_seats_by_department_and_register(seats):
    return sorted(seats, key=lambda s: (s["department"], s["register_no"]))


def _reorder_hall_seats_by_bench(seats):
    if not seats:
        return seats

    dept_queues = defaultdict(deque)
    for s in seats:
        dept_queues[s["department"]].append(s)

    reordered = []

    while dept_queues:
        for d in list(dept_queues):
            if not dept_queues[d]:
                del dept_queues[d]

        if not dept_queues:
            break

        depts = sorted(dept_queues, key=lambda d: len(dept_queues[d]), reverse=True)

        if len(depts) >= 2:
            reordered.append(dept_queues[depts[0]].popleft())
            reordered.append(dept_queues[depts[1]].popleft())
        else:
            d = depts[0]
            reordered.append(dept_queues[d].popleft())
            if dept_queues[d]:
                reordered.append(dept_queues[d].popleft())

    return reordered


def _generate_output_rows(halls):
    rows = []
    for hall in halls:
        seat_no = 1
        for seat in hall["seats"]:
            rows.append({
                "register_no": seat["register_no"],
                "student_name": seat["student_name"],
                "department": seat["department"],
                "subject_code": seat["subject_code"],
                "hall_id": hall["hall_id"],
                "seat_number": seat_no
            })
            seat_no += 1
    return rows


# ============================================================
# CLI / Test Execution
# ============================================================

if __name__ == "__main__":

    PREPARED_CSV = (
        "/home/adhil-cr/Desktop/Seating arrangment/"
        "seating_system/output_data/"
        "prepared_exam_session_2026-03-10_FN.csv"
    )

    OUTPUT_DIR = (
        "/home/adhil-cr/Desktop/Seating arrangment/"
        "seating_system/output_data"
    )

    seating_config = {
        "number_of_halls": 26,
        "hall_capacity": 20,
        "max_subject_per_hall": 12,
    }

    result = allocate_seating(
        prepared_csv_path=PREPARED_CSV,
        output_dir=OUTPUT_DIR,
        seating_config=seating_config
    )

    print("Seat allocation completed successfully:")
    print(result)
