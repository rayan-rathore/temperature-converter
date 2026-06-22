

class TemperatureConverter:
    def __init__(self, user_temp, current_unit, desired_unit):
        self.user_temp = user_temp
        self.current_unit = current_unit
        self.desired_unit = desired_unit


    """def valid_input(self):
        if self.current_unit not in ["c", "f", "k"] or self.desired_unit not in ["c", "f", "k"]:
            print("Error: Please enter a valid unit (C or F or K)")
            return False

        if self.current_unit == self.desired_unit:
            print("The units are the same!")
            return False

        return True"""


    def converter(self):
        if self.current_unit == "c":
            if self.desired_unit == "f":
                return (self.user_temp * 9 / 5) + 32
            if self.desired_unit == "k":
                return  self.user_temp + 273.15

        elif self.current_unit == "f":
            if self.desired_unit == "c":
                return (self.user_temp - 32) * 5 / 9
            if self.desired_unit == "k":
                return (self.user_temp - 32) * 5 / 9 + 273.15

        elif self.current_unit == "k":
            if self.desired_unit == "c":
                return self.user_temp - 273.15
            if self.desired_unit == "f":
                return (self.user_temp - 273.15) * 9 / 5 + 32
        return None