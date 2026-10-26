"""Python Programming Case Study 3: Shopping Discount Calculator"""

def case_study_03_shopping_discount_calculator():
    """
    CASE STUDY 3: Shopping Discount Calculator

    1. QUESTION / PROBLEM STATEMENT:
       Calculate a customer's discount and final shopping bill according to the total purchase amount.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read purchase amount from user.
       Step 2: Validate amount; reject if amount < 0 with an error message.
       Step 3: Determine discount rate based on slabs:
               - Amount >= 3000: discount rate = 10%
               - Amount >= 1000 and < 3000: discount rate = 5%
               - Amount < 1000: discount rate = 0%
       Step 4: Calculate discount and final bill:
               - discount = amount * rate / 100
               - final_bill = amount - discount
       Step 5: Display discount rate, discount amount, and final bill amount rounded to 2 decimal places.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT amount
       IF amount < 0:
           PRINT error
       ELSE:
           IF amount >= 3000: rate = 10%
           ELSE IF amount >= 1000: rate = 5%
           ELSE: rate = 0%
           discount = amount * rate / 100
           final_bill = amount - discount
           PRINT discount, final_bill
       STOP

    4. TEST CASES:
       - Normal:         Amount = 800  -> Expected: No discount; final Rs. 800
       - Alternate:      Amount = 2000 -> Expected: 5% discount Rs. 100; final Rs. 1900
       - High Purchase:  Amount = 4000 -> Expected: 10% discount Rs. 400; final Rs. 3600
    """
    amount = float(input("Enter shopping amount (Rs.): "))

    if amount < 0:
        print("Invalid amount.")
    else:
        if amount >= 3000:
            rate = 10
        elif amount >= 1000:
            rate = 5
        else:
            rate = 0
        discount = amount * rate / 100
        final_bill = amount - discount
        print("Discount rate:", rate, "%")
        print("Discount: Rs.", round(discount, 2))
        print("Final bill: Rs.", round(final_bill, 2))

if __name__ == '__main__':
    case_study_03_shopping_discount_calculator()
