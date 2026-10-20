"""
PYTHON PROGRAMMING: ACTIVITY-BASED LEARNING
Case Studies with Questions, Step-by-Step Solutions, and Source Code

This module contains all 10 case studies from the course document in their original order.
Each case study includes:
  - Question / Problem Statement
  - Complete Step-by-Step Solution / Algorithm
  - Pseudocode
  - Complete Executable Python Solution
  - Test Cases and Expected Results
  - Sample Output
"""

import sys


# ==============================================================================
# CASE STUDY 1: Simple Interest Calculator
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 2: Temperature Converter
# ==============================================================================

def case_study_02_temperature_converter():
    """
    CASE STUDY 2: Temperature Converter

    1. QUESTION / PROBLEM STATEMENT:
       Create a program that converts a temperature from Celsius to Fahrenheit or
       Fahrenheit to Celsius based on the user's choice.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start.
       Step 2: Display conversion choices (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius).
       Step 3: Read user choice and the temperature value.
       Step 4: Apply conversion formula based on selected choice:
               - If choice is "1": result = (temperature * 9 / 5) + 32
               - If choice is "2": result = (temperature - 32) * 5 / 9
               - Otherwise: Display invalid choice error message.
       Step 5: Display converted temperature value rounded to 2 decimal places.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       PRINT conversion menu
       INPUT choice, temperature
       IF choice = 1:
           result = temperature * 9 / 5 + 32
       ELSE IF choice = 2:
           result = (temperature - 32) * 5 / 9
       ELSE:
           PRINT invalid choice
       PRINT result
       STOP

    4. TEST CASES:
       - Normal:      Choice = 1, Temperature = 0    -> Expected: 32.0°F
       - Alternate:   Choice = 2, Temperature = 98.6 -> Expected: 37.0°C approximately
       - Invalid:     Choice = 3, Temperature = 25   -> Expected: Invalid choice
    """
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ")
    temperature = float(input("Enter temperature: "))

    if choice == "1":
        result = temperature * 9 / 5 + 32
        print("Temperature in Fahrenheit:", round(result, 2))
    elif choice == "2":
        result = (temperature - 32) * 5 / 9
        print("Temperature in Celsius:", round(result, 2))
    else:
        print("Invalid choice.")


# ==============================================================================
# CASE STUDY 3: Shopping Discount Calculator
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 4: Student Grade Calculator
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 5: Library Late-Fee Calculator
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 6: Bus Fare Calculator
# ==============================================================================

def case_study_06_bus_fare_calculator():
    """
    CASE STUDY 6: Bus Fare Calculator

    1. QUESTION / PROBLEM STATEMENT:
       Calculate a passenger's bus fare based on travel distance, with a minimum fare and a per-kilometre rate.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read distance in kilometres from user.
       Step 2: Reject negative distance values with an error message.
       Step 3: If distance <= 1 km, fare is minimum charge of Rs. 10.
       Step 4: If distance > 1 km, fare = 10 + (distance - 1) * 5.
       Step 5: Display total fare rounded to 2 decimal places.
       Step 6: Stop.

    3. PSEUDOCODE:
       START
       INPUT distance
       IF distance < 0:
           PRINT error
       ELSE IF distance <= 1:
           fare = 10
       ELSE:
           fare = 10 + (distance - 1) * 5
       PRINT fare
       STOP

    4. TEST CASES:
       - Short Trip:   Distance = 0.5 km -> Expected: Fare Rs. 10
       - Boundary:     Distance = 1 km   -> Expected: Fare Rs. 10
       - Longer Trip:  Distance = 5 km   -> Expected: Fare Rs. 30.0
    """
    distance = float(input("Enter distance in kilometres: "))

    if distance < 0:
        print("Invalid distance.")
    elif distance <= 1:
        fare = 10
        print("Bus fare: Rs.", fare)
    else:
        fare = 10 + (distance - 1) * 5
        print("Bus fare: Rs.", round(fare, 2))


# ==============================================================================
# CASE STUDY 7: Daily Expense Tracker
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 8: Number Property Checker
# ==============================================================================

def case_study_08_number_property_checker():
    """
    CASE STUDY 8: Number Property Checker

    1. QUESTION / PROBLEM STATEMENT:
       Check whether an integer is positive, negative, or zero, and determine whether it is even or odd.

    2. STEP-BY-STEP SOLUTION / ALGORITHM:
       Step 1: Start and read an integer from user.
       Step 2: Check sign:
               - If number > 0: print "The number is positive."
               - Elif number < 0: print "The number is negative."
               - Else: print "The number is zero."
       Step 3: Check parity using modulus operator:
               - If number % 2 == 0: print "The number is even."
               - Else: print "The number is odd."
       Step 4: Stop.

    3. PSEUDOCODE:
       START
       INPUT n
       IF n > 0:
           PRINT positive
       ELSE IF n < 0:
           PRINT negative
       ELSE:
           PRINT zero
       IF n % 2 = 0:
           PRINT even
       ELSE:
           PRINT odd
       STOP

    4. TEST CASES:
       - Positive Odd:   Number = 7  -> Expected: Positive; odd
       - Negative Even:  Number = -4 -> Expected: Negative; even
       - Zero:           Number = 0  -> Expected: Zero; even
    """
    number = int(input("Enter an integer: "))

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


# ==============================================================================
# CASE STUDY 9: Water Usage Bill
# ==============================================================================

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


# ==============================================================================
# CASE STUDY 10: Multiplication Table Generator
# ==============================================================================

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


# ==============================================================================
# MAIN INTERACTIVE RUNNER (Optional Execution Interface)
# ==============================================================================

CASE_STUDIES = [
    ("Simple Interest Calculator", case_study_01_simple_interest_calculator),
    ("Temperature Converter", case_study_02_temperature_converter),
    ("Shopping Discount Calculator", case_study_03_shopping_discount_calculator),
    ("Student Grade Calculator", case_study_04_student_grade_calculator),
    ("Library Late-Fee Calculator", case_study_05_library_late_fee_calculator),
    ("Bus Fare Calculator", case_study_06_bus_fare_calculator),
    ("Daily Expense Tracker", case_study_07_daily_expense_tracker),
    ("Number Property Checker", case_study_08_number_property_checker),
    ("Water Usage Bill", case_study_09_water_usage_bill),
    ("Multiplication Table Generator", case_study_10_multiplication_table_generator),
]


def display_menu():
    print("\n" + "=" * 60)
    print("PYTHON PROGRAMMING - 10 CASE STUDIES & STEP-BY-STEP SOLUTIONS")
    print("=" * 60)
    for idx, (title, _) in enumerate(CASE_STUDIES, start=1):
        print(f" {idx:2d}. {title}")
    print("  0. Exit")
    print("=" * 60)


def main():
    while True:
        display_menu()
        choice = input("Enter case study number to run (0-10): ").strip()
        if choice == "0":
            print("Exiting program.")
            break
        try:
            case_num = int(choice)
            if 1 <= case_num <= len(CASE_STUDIES):
                title, func = CASE_STUDIES[case_num - 1]
                print("\n" + "-" * 60)
                print(f"RUNNING CASE STUDY {case_num}: {title}")
                print("-" * 60)
                func()
            else:
                print("Please enter a valid number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()
