"""Python Programming Case Study 2: Temperature Converter"""

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

if __name__ == '__main__':
    case_study_02_temperature_converter()
