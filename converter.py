from enum import Enum

class MenuResult(Enum):
    SUCCESS = 1
    INVALID = 2
    EXIT = 3

def convert(value, from_unit, to_unit):
    conversions = {
        # Length
        ("km", "mile"): lambda x: x * 0.621371,
        ("mile", "km"): lambda x: x * 1.60934,

        # Temperature
        ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,

        # Volume (US)
        ("gallon_us", "liter"): lambda x: x * 3.78541,
        ("liter", "gallon_us"): lambda x: x / 3.78541,

        # Volume (UK)
        ("gallon_uk", "liter"): lambda x: x * 4.54609,
        ("liter", "gallon_uk"): lambda x: x / 4.54609,
    }

    key = (from_unit, to_unit)
    if key in conversions:
        return conversions[key](value)
    else:
        return None

def main_menu():
    print("\nUNIT CONVERTER")
    print("1. Length (Km - Mile)") 
    print("2. Temperature (Celsius - Fahrenheit)")
    print("3. Volume (Gallon - Liter)")
    print("4. Exit")

    choice = input("Your choice (1-4): ")

    try:
        # LENGTH
        if choice == "1":
            print("\n[Length Conversion]")
            print("1. Kilometer to Mile")
            print("2. Mile to Kilometer")
            
            sub_choice = input("Choose direction (1 or 2): ")
            
            if sub_choice not in ["1", "2"]:
                print("Invalid direction choice! Please enter 1 or 2.")
                return MenuResult.INVALID

            val = float(input("Enter length value: "))

            if sub_choice == "1":
                print(f"{val} km = {convert(val, 'km', 'mile'):.2f} mile")
            elif sub_choice == "2":
                print(f"{val} mile = {convert(val, 'mile', 'km'):.2f} km")
            
            return MenuResult.SUCCESS

        # TEMPERATURE
        elif choice == "2":
            print("\n[Temperature Conversion]")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            
            sub_choice = input("Choose direction (1 or 2): ")

            # UX DÜZELTMESİ:
            if sub_choice not in ["1", "2"]:
                print("Invalid direction choice! Please enter 1 or 2.")
                return MenuResult.INVALID
            
            val = float(input("Enter temperature value: "))

            if sub_choice == "1":
                print(f"{val} °C = {convert(val, 'celsius', 'fahrenheit'):.2f} °F")
            elif sub_choice == "2":
                print(f"{val} °F = {convert(val, 'fahrenheit', 'celsius'):.2f} °C")

            return MenuResult.SUCCESS

        # VOLUME
        elif choice == "3":
            print("\n[Volume Conversion]")
            print("1. Gallon to Liter")
            print("2. Liter to Gallon")
            
            direction = input("Choose direction (1 or 2): ")
            
            if direction not in ["1", "2"]:
                print("Invalid direction choice!")
                return MenuResult.INVALID

            gallon_type = input("Choose gallon type (US / UK): ").lower()
            
            if gallon_type not in ["us", "uk"]:
                print("Invalid gallon type!")
                return MenuResult.INVALID
            
            val = float(input("Enter value: "))

            if direction == "1":
                from_u = f"gallon_{gallon_type}"
                print(f"{val} {gallon_type.upper()} gallons = {convert(val, from_u, 'liter'):.2f} liters")
            
            elif direction == "2":
                to_u = f"gallon_{gallon_type}"
                print(f"{val} liters = {convert(val, 'liter', to_u):.2f} {gallon_type.upper()} gallons")

            return MenuResult.SUCCESS

        elif choice == "4":
            print("Good Bye!")
            return MenuResult.EXIT

        else:
            print("Invalid choice!")
            return MenuResult.INVALID

    except ValueError:
        print("Error: Please enter a valid number.")
        return MenuResult.INVALID

# Main
running = True
while running:
    result = main_menu()

    if result == MenuResult.INVALID:
        input("Press Enter to try again...") 
        continue

    elif result == MenuResult.EXIT:
        break

    elif result == MenuResult.SUCCESS:
        decision = input("\nType 'exit' to quit or Press Enter to continue: ").lower()
        if decision == "exit":
            print("Good Bye.")
            running = False