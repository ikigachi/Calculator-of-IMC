def calculate_bmi(name, weight, height, age, gender):
    # Create a tuple for user info
    user_info = (name, weight, height, age, gender)

    # BMI calculation
    bmi = user_info[1] / (user_info[2] ** 2)  # weight / height^2

    # Responses based on gender and BMI
    messages = {
        "M": (
            (20, "Your category is 'underweight'. You're on the lighter side, take care of yourself!"),
            (25, "You're in the healthy range—great job!"),
            (30, "Looks like you're in the 'overweight' category. Maybe hit the gym?"),
            (float('inf'), "Your category is 'obese '. It's time to focus on your health, buddy.")
        ),
        "F": (
            (18, "Your category is 'underweight'. Stay healthy and eat well!"),
            (24, "You're rocking the healthy range—keep it up!"),
            (29, "Your category is 'overweight'. You're above the healthy range. Nothing a little movement can't fix!"),
            (float('inf'), "Your category is 'obese'. Your health should be a priority. Consider consulting a pro.")
        )
    }

    # Validate gender and get the appropriate message
    if gender not in messages:
        print("Invalid gender. Please restart and enter 'M' or 'F'.")
        return

    for threshold, message in messages[gender]:
        if bmi < threshold:
            feedback = message
            break

    # Display results with a fun twist
    print(f"\n{user_info[0]}, here are your results:")
    print(f"🌟 Your BMI is: {bmi:.2f}")
    print(f"📢 {feedback}")
    print("\nRemember: Your BMI is just a number. Stay happy and healthy! 💪")

# Input data
name = input("What's your name? ")
weight = float(input(f"Alright, {name}, what's your weight in kg? "))
height = float(input(f"And your height in meters? "))
age = int(input("How old are you? "))
gender = input("Lastly, what's your gender? (M/F): ").strip().upper()

#Run the calculator
calculate_bmi(name, weight, height, age, gender)
