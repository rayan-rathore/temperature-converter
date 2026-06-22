print("------Welcome to the Temperature Converter.------")
#user_temp = int(input("Let me know the temperature that you want to convert.\n"))

while True:
    try:
        user_temp = float(input("Let me know the temperature that you want to convert.\n"))
        break
    except ValueError:
        print("Invalid input. Please enter the number.")


while True:
    current_unit = input("What's the unit of it? type 'C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin \n").lower()
    desired_unit = input("To which unit do you want to convert this Temperature?").lower()

    if current_unit == desired_unit:
        print("The units are the same!")
        continue

    if current_unit not in ["c", "f", "k"] or desired_unit not in ["c", "f", "k"]:
        print("Error: Please enter a valid unit (C or F or K)")
        continue


    if current_unit == "c":
        if desired_unit == "f":
            converted_temp = (user_temp * 9 / 5) + 32
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°F")
        if desired_unit == "k":
            converted_temp = user_temp + 273.15
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°K")
        break

    if current_unit == "k":
        if desired_unit == "c":
            converted_temp = user_temp - 273.15
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°C")
        if desired_unit == "f":
            converted_temp = (user_temp - 273.15) * 9 / 5 + 32
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°F")
        break

    elif current_unit == "f":
        if desired_unit == "c":
            converted_temp = (user_temp -32) * 5 / 9
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°C")
        if desired_unit == "k":
            converted_temp = (user_temp - 32) * 5 / 9 + 273.15
            print(f"{user_temp}°{current_unit.title()} is equal to {converted_temp:.2f}°K")
        break

