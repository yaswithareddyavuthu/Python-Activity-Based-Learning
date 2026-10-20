# Python Programming - 10 Case Studies & Step-by-Step Solutions
#
# NOTE:
# The code you sent contains the menu and main() function, but it does not
# include the definitions for the case-study functions or the first part of
# the CASE_STUDIES list. Add those definitions where indicated below.

# Define these functions before adding them to CASE_STUDIES:
# case_study_01_...
# case_study_02_...
# case_study_03_...
# case_study_04_student_grade_calculator
# case_study_05_library_late_fee_calculator
# case_study_06_bus_fare_calculator
# case_study_07_daily_expense_tracker
# case_study_08_number_property_checker
# case_study_09_water_usage_bill
# case_study_10_multiplication_table_generator

# Complete CASE_STUDIES list:
# CASE_STUDIES = [
#     ("Case Study 1 Title", case_study_01_function),
#     ("Case Study 2 Title", case_study_02_function),
#     ("Case Study 3 Title", case_study_03_function),
#     ("Student Grade Calculator", case_study_04_student_grade_calculator),
#     ("Library Late-Fee Calculator", case_study_05_library_late_fee_calculator),
#     ("Bus Fare Calculator", case_study_06_bus_fare_calculator),
#     ("Daily Expense Tracker", case_study_07_daily_expense_tracker),
#     ("Number Property Checker", case_study_08_number_property_checker),
#     ("Water Usage Bill", case_study_09_water_usage_bill),
#     ("Multiplication Table Generator", case_study_10_multiplication_table_generator),
# ]

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
        try:
            choice = input("Enter case study number to run (0-10): ").strip()

            if choice == "0":
                print("Exiting program.")
                break

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
