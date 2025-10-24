# student_marks_analyzer.py

# --- 1️⃣ Data Input Layer ---
def get_student_data():
    """Collect student names and marks"""
    students = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = list(map(float, input(f"Enter marks for {name} (space-separated): ").split()))
        students[name] = marks
    return students


# --- 2️⃣ Processing Layer ---
def calculate_average(marks):
    """Calculate average marks"""
    return sum(marks) / len(marks)

def calculate_grade(avg):
    """Assign grade based on average"""
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'


# --- 3️⃣ Output Layer ---
def display_results(students):
    """Display results for all students"""
    print("\n--- Student Report ---")
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = calculate_grade(avg)
        print(f"{name:<10} | Average: {avg:.2f} | Grade: {grade}")


# --- 4️⃣ Main Function (Program Entry Point) ---
def main():
    students = get_student_data()
    display_results(students)

# Run the program
if __name__ == "__main__":
    main()