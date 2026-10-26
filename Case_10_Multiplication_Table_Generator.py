"""Python Programming Case Study 10: Multiplication Table Generator"""

def case_study_10_multiplication_table_generator():
    """
    CASE STUDY 10: Multiplication Table Generator

    1. QUESTION / PROBLEM STATEMENT:
       Generate the multiplication table of a number up to a user-selected limit.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read number and limit from user.
       Step 2: Validate table limit (must be between 1 and 20).
               If limit < 1 or limit > 20, print error message.
       Step 3: Use a for loop with range(1, limit + 1).
       Step 4: In each iteration, print: number x i = (number * i).
       Step 5: Stop.

    3. PSEUDOCODE:
       START
       INPUT number, limit
       IF limit < 1 OR limit > 20:
           PRINT error
       ELSE:
           FOR i from 1 to limit:
               PRINT number, '*', i, '=', number * i
       STOP

    4. TEST CASES:
       - Normal:      Number = 3, Limit = 5 -> Expected: 3 x 1 = 3 through 3 x 5 = 15
       - Boundary:    Number = 7, Limit = 1 -> Expected: 7 x 1 = 7
       - Invalid:     Limit = 0             -> Expected: Invalid limit message
    """
    number = int(input("Enter a number: "))
    limit = int(input("Enter table limit (1 to 20): "))

    if limit < 1 or limit > 20:
        print("Invalid limit. Enter a value from 1 to 20.")
    else:
        for i in range(1, limit + 1):
            print(number, "x", i, "=", number * i)

if __name__ == '__main__':
    case_study_10_multiplication_table_generator()
