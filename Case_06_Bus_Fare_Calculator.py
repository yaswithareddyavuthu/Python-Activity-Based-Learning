"""Python Programming Case Study 6: Bus Fare Calculator"""

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

if __name__ == '__main__':
    case_study_06_bus_fare_calculator()
