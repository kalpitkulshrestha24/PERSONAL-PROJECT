import pandas as pd

# --- 1️⃣ Input Layer (Now from CSV) ---
def get_student_data(filename):
    """Read student data from CSV file"""
    df = pd.read_csv(filename)
    return df

# --- 2️⃣ Processing Layer ---
def calculate_average(df):
    """Compute average across all subjects"""
    df['Average'] = df.iloc[:, 1:].mean(axis=1)
    return df

def calculate_grade(avg):
    """Assign grades"""
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

def assign_grades(df):
    """Apply grading to DataFrame"""
    df['Grade'] = df['Average'].apply(calculate_grade)
    return df

# --- 3️⃣ Output Layer ---
def display_results(df):
    print("\n--- Student Report ---")
    print(df[['Name', 'Average', 'Grade']])

# --- 4️⃣ Main Function ---
def main():
    df = get_student_data("students.csv")
    df = calculate_average(df)
    df = assign_grades(df)
    display_results(df)

if __name__ == "__main__":
    main()
