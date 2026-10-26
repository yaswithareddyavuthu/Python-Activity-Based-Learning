"""Python Programming Case Study 1: Simple Interest Calculator"""

def case_study_01_simple_interest_calculator():
    """
    CASE STUDY 1: Simple Interest Calculator

    1. QUESTION / PROBLEM STATEMENT:
       Write a Python program to calculate simple interest and the total amount payable
       from principal, annual rate, and time.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start.
       Step 2: Read principal, rate, and time from user.
       Step 3: Validate that all three values are non-negative.
               If any value is negative, display an error message.
       Step 4: Calculate simple interest and total amount:
               - Simple Interest = (Principal * Rate * Time) / 100
               - Total Amount = Principal + Simple Interest
       Step 5: Display the calculated interest and total amount rounded to 2 decimal places.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT principal, rate, time
       IF any value is negative:
           PRINT error
       ELSE:
           interest = principal * rate * time / 100
           total = principal + interest
           PRINT interest, total
       STOP

    4. TEST CASES:
       - Normal:      Principal = 10000, Rate = 5, Time = 2 -> Expected: Interest Rs. 1000, Total Rs. 11000
       - Alternate:   Principal = 5000, Rate = 4, Time = 1  -> Expected: Interest Rs. 200, Total Rs. 5200
       - Invalid:     Principal = -100, Rate = 5, Time = 2  -> Expected: Invalid input message
    """
    principal = float(input("Enter principal amount (Rs.): "))
    rate = float(input("Enter annual rate (%): "))
    time = float(input("Enter time (years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Invalid input: values cannot be negative.")
    else:
        interest = principal * rate * time / 100
        total = principal + interest
        print("Simple interest: Rs.", round(interest, 2))
        print("Total amount: Rs.", round(total, 2))

if __name__ == '__main__':
    case_study_01_simple_interest_calculator()
