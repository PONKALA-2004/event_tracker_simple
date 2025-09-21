# ------------------------------
# Simple CLI Project
# ------------------------------

events = []
students = []
attendance = []


def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    event = {"id": len(events) + 1, "name": name, "date": date}
    events.append(event)
    print("✅ Event added successfully!")


def view_events():
    if not events:
        print("⚠ No events found.")
        return
    for e in events:
        print(f"[{e['id']}] {e['name']} - {e['date']}")


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    student = {"id": len(students) + 1, "roll_no": roll_no, "name": name}
    students.append(student)
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("⚠ No students found.")
        return
    for s in students:
        print(f"[{s['id']}] {s['roll_no']} - {s['name']}")


def mark_attendance():
    if not events or not students:
        print("⚠ Add events and students first.")
        return

    view_events()
    event_id = int(input("Enter event ID: "))
    view_students()
    student_id = int(input("Enter student ID: "))
    status = input("Enter status (Present/Absent): ")

    record = {
        "event_id": event_id,
        "student_id": student_id,
        "status": status
    }
    attendance.append(record)
    print("✅ Attendance marked!")


def view_report():
    if not attendance:
        print("⚠ No attendance records found.")
        return

    print("\n📋 Attendance Report:")
    for r in attendance:
        event = next((e for e in events if e["id"] == r["event_id"]), None)
        student = next((s for s in students if s["id"] == r["student_id"]), None)
        if event and student:
            print(f"Event: {event['name']} | {student['roll_no']} - {student['name']} | Status: {r['status']}")


# ------------------------------
# Main Menu
# ------------------------------
def main():
    while True:
        print("\n===== Student Event & Attendance Tracker =====")
        print("1. Add Event")
        print("2. View Events")
        print("3. Add Student")
        print("4. View Students")
        print("5. Mark Attendance")
        print("6. View Attendance Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            add_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            mark_attendance()
        elif choice == "6":
            view_report()
        elif choice == "7":
            print("👋 Exiting program...")
            break
        else:
            print("⚠ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
