"""Python Programming Case Study 7: Daily Expense Tracker"""

def case_study_07_daily_expense_tracker():
    """
    CASE STUDY 7: Daily Expense Tracker

    1. QUESTION / PROBLEM STATEMENT:
       Record expenses for a day, calculate the total spent, and compare the total with a daily budget.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read daily budget and number of expenses.
       Step 2: Validate that budget >= 0 and count >= 0. If negative, display error.
       Step 3: Initialize total = 0.
       Step 4: Use a loop from 1 to count to read each expense amount.
               - If any expense < 0, print error, set total = None, and break out of loop.
               - Otherwise, add expense to running total.
       Step 5: If total is not None:
               - Display total spending rounded to 2 decimal places.
               - If total > budget, print "Status: Budget exceeded."
               - Otherwise, print "Status: Within budget."
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT budget, count
       IF budget < 0 OR count < 0:
           PRINT error
       ELSE:
           total = 0
           REPEAT count times:
               INPUT expense
               total = total + expense
           PRINT total
           IF total > budget:
               PRINT over budget
           ELSE:
               PRINT within budget
       STOP

    4. TEST CASES:
       - Normal:       Budget = 500, Expenses = [100, 150] -> Expected: Total Rs. 250; Status: Within budget.
       - Over Budget:  Budget = 300, Expenses = [200, 150] -> Expected: Total Rs. 350; Status: Budget exceeded.
       - Invalid:      Negative expense entered             -> Expected: Expense cannot be negative.
    """
    budget = float(input("Enter daily budget (Rs.): "))
    count = int(input("How many expenses? "))

    if budget < 0 or count < 0:
        print("Invalid budget or number of expenses.")
    else:
        total = 0
        for i in range(count):
            expense = float(input("Enter expense amount (Rs.): "))
            if expense < 0:
                print("Expense cannot be negative.")
                total = None
                break
            total += expense

        if total is not None:
            print("Total spending: Rs.", round(total, 2))
            if total > budget:
                print("Status: Budget exceeded.")
            else:
                print("Status: Within budget.")

if __name__ == '__main__':
    case_study_07_daily_expense_tracker()
