"""Python Programming Case Study 9: Water Usage Bill"""

def case_study_09_water_usage_bill():
    """
    CASE STUDY 9: Water Usage Bill

    1. QUESTION / PROBLEM STATEMENT:
       Calculate a sample household water bill using a basic per-unit charge and a fixed service fee.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read water units consumed.
       Step 2: Validate that units >= 0. If negative, print error message.
       Step 3: Calculate usage charge using slabs:
               - If units <= 20: usage_charge = units * 3
               - Else: usage_charge = (20 * 3) + ((units - 20) * 5)
       Step 4: Add fixed service fee of Rs. 30:
               - fixed_fee = 30
               - total_bill = usage_charge + fixed_fee
       Step 5: Display usage charge, fixed service fee, and total water bill.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT units
       IF units < 0:
           PRINT error
       ELSE IF units <= 20:
           usage = units * 3
       ELSE:
           usage = 20 * 3 + (units - 20) * 5
       bill = usage + 30
       PRINT usage, bill
       STOP

    4. TEST CASES:
       - Normal (within slab):  Units = 10 -> Expected: Usage Rs. 30; Total Rs. 60
       - Above first slab:      Units = 25 -> Expected: Usage Rs. 85; Total Rs. 115
       - Invalid input:         Units = -1 -> Expected: Invalid input message
    """
    units = int(input("Enter water units consumed: "))

    if units < 0:
        print("Invalid input: units cannot be negative.")
    else:
        if units <= 20:
            usage_charge = units * 3
        else:
            usage_charge = 20 * 3 + (units - 20) * 5

        fixed_fee = 30
        total_bill = usage_charge + fixed_fee

        print("Usage charge: Rs.", usage_charge)
        print("Fixed service fee: Rs.", fixed_fee)
        print("Total water bill: Rs.", total_bill)

if __name__ == '__main__':
    case_study_09_water_usage_bill()
