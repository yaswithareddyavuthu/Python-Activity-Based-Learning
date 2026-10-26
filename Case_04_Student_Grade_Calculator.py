"""Python Programming Case Study 4: Student Grade Calculator"""

def case_study_04_student_grade_calculator():
    """
    CASE STUDY 4: Student Grade Calculator

    1. QUESTION / PROBLEM STATEMENT:
       Read marks in five subjects, calculate the average, and assign a grade based on the average.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read marks for 5 subjects from user.
       Step 2: Check that each mark is within valid range (0 to 100).
               If any mark is invalid, display an error message.
       Step 3: Calculate average of the 5 marks: average = sum(marks) / len(marks).
       Step 4: Assign grade using conditional classification:
               - Average >= 90: Grade 'A'
               - Average >= 75: Grade 'B'
               - Average >= 60: Grade 'C'
               - Average >= 40: Grade 'D'
               - Average < 40:  Grade 'F'
       Step 5: Display calculated average and assigned grade.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT five marks
       IF any mark < 0 OR mark > 100:
           PRINT error
       ELSE:
           average = sum(marks) / 5
           IF average >= 90: grade = A
           ELSE IF average >= 75: grade = B
           ELSE IF average >= 60: grade = C
           ELSE IF average >= 40: grade = D
           ELSE: grade = F
           PRINT average, grade
       STOP

    4. TEST CASES:
       - Normal:      Marks = [95, 90, 92, 88, 95] -> Expected: Average 92.0; Grade A
       - Alternate:   Marks = [70, 65, 75, 60, 80] -> Expected: Average 70.0; Grade C
       - Invalid:     Marks with 105 or negative   -> Expected: Invalid marks message
    """
    marks = []
    for i in range(1, 6):
        mark = float(input("Enter mark for subject " + str(i) + ": "))
        marks.append(mark)

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks: enter values from 0 to 100.")
    else:
        average = sum(marks) / len(marks)
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"
        print("Average:", round(average, 2))
        print("Grade:", grade)

if __name__ == '__main__':
    case_study_04_student_grade_calculator()
