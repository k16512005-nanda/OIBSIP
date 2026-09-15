# BMI Calculator
# Oasis Infobyte - Python Programming Internship
# Task 2

def calculate_bmi():
    print("\n===== BMI CALCULATOR =====")

    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))

            # Validate input
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than 0.")
                continue

            # Calculate BMI
            bmi = weight / (height ** 2)

            print(f"\nYour BMI is: {bmi:.2f}")

            # BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            print(f"Category: {category}")

            # Ask if the user wants another calculation
            again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()

            if again not in ("yes", "y"):
                print("\nThank you for using the BMI Calculator!")
                break

        except ValueError:
            print("Error: Please enter numbers only.")


# Start the program
if __name__ == "__main__":
    calculate_bmi()