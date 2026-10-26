"""Python Programming Case Study 5: Library Late-Fee Calculator"""

def case_study_05_library_late_fee_calculator():
    """
    CASE STUDY 5: Library Late-Fee Calculator

    1. QUESTION / PROBLEM STATEMENT:
       Calculate a library late fee based on the number of days a book is returned after its due date.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read number of late days from user.
       Step 2: If late days < 0, show invalid input error.
       Step 3: If late days == 0, fee is Rs. 0 (returned on time).
       Step 4: If late days is between 1 and 5 (inclusive), fee = days * 2.
       Step 5: If late days > 5, fee = (5 * 2) + (days - 5) * 5.
       Step 6: Display total late fee.
       Step 7: Stop.

    3. PSEUDOCODE:
       START
       INPUT days
       IF days < 0:
           PRINT error
       ELSE IF days = 0:
           fee = 0
       ELSE IF days <= 5:
           fee = days * 2
       ELSE:
           fee = 5 * 2 + (days - 5) * 5
       PRINT fee
       STOP

    4. TEST CASES:
       - On Time:     Late days = 0  -> Expected: Fee Rs. 0
       - Normal:      Late days = 4  -> Expected: Fee Rs. 8
       - Late Return: Late days = 8  -> Expected: Fee Rs. 25
       - Invalid:     Late days = -2 -> Expected: Invalid input message
    """
    days = int(input("Enter number of late days: "))

    if days < 0:
        print("Invalid input: days cannot be negative.")
    elif days == 0:
        fee = 0
    elif days <= 5:
        fee = days * 2
    else:
        fee = 5 * 2 + (days - 5) * 5

    if days >= 0:
        print("Library late fee: Rs.", fee)

if __name__ == '__main__':
    case_study_05_library_late_fee_calculator()
