#Deana Akimov, Assingment 2.2, January 15, 2025. Code taken from Google AI
def calculate_bmi(weight_pounds, height_feet):
    """Calculate BMI given weight in pounds and height in feet."""
    weight_kg = weight_pounds * 0.453592  # Convert pounds to kilograms
    height_m = height_feet * 0.3048  # Convert feet to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    """Main function to interact with the user."""
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in feet: "))

    bmi = calculate_bmi(weight, height)

    print(f"{name}, your BMI is {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You are in the healthy weight range.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()