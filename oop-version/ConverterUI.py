from temperatureconverter import TemperatureConverter
from prettytable import PrettyTable
history = []

def user_temp():
    while True:
        try:
            user_input = float(input("Let me know the temperature that you want to convert.\n"))
            break
        except ValueError:
            print("Invalid input. Please enter the number.")
    return user_input

def valid_input(prompt_message):
    while True:
        unit = input(prompt_message).lower()
        if unit not in ["c", "f", "k"] :
            print("Error: Please enter a valid unit (C or F or K)")
        else:
            return unit

while True:
    print("\n------Welcome to the Temperature Converter.------")
    value = user_temp()
    table = PrettyTable()

    current_u = valid_input("What's the unit of it? type 'C' for Celsius, "
                                  "'F' for Fahrenheit, 'K' for Kelvin \n").lower()
    desired_u = valid_input("To which unit do you want to convert this Temperature?\n").lower()
    if current_u == desired_u:
        print("The units are the same! Let's try again.")
        continue

    converter_main = TemperatureConverter(value, current_u, desired_u)

    result = converter_main.converter()
    output_message = f"{value}°{current_u.title()} is equal to {result:.2f}°{desired_u.title()}"
    print(output_message)
    history.append(output_message)

    user_choice = input("Do you want to convert another number? (y/n)").lower()
    if user_choice != "y":
        print("---History---")
        table.align = "l"
        table.field_names = ["No.", "Result"]
        for i , sentence in enumerate(history, start=1):
            table.add_row([i, sentence])

        print(table)
        print("Thanks for using Temperature Converter. Goodbye!")
        break

