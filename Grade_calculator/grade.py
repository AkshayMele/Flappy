def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid Score'

def student_grade_calculator():
    num_subjects = int(input("Enter the number of subjects: "))
    total_score = 0

    for i in range(1, num_subjects + 1):
        try:
            subject_name = input(f"Enter the name of Subject {i}: ")
            subject_score = float(input(f"Enter the score for {subject_name}: "))
            
            if 0 <= subject_score <= 100:
                total_score += subject_score
            else:
                print("Invalid score. Score should be between 0 and 100.")
                return

        except ValueError:
            print("Invalid input. Please enter a numeric score.")
            return

    average_score = total_score / num_subjects
    overall_grade = calculate_grade(average_score)

    print("\nStudent Grade Report:")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Overall Grade: {overall_grade}")

if __name__ == "__main__":
    student_grade_calculator()
