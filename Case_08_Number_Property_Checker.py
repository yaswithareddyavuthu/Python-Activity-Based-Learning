"""Python Programming Case Study 8: Number Property Checker"""

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

if __name__ == '__main__':
    case_study_08_number_property_checker()
