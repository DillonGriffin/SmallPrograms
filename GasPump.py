# define a FuelType class to represent the available fuel types
class FuelType:
    def __init__(self, name, price_per_gallon):
        self.name = name
        self.price_per_gallon = price_per_gallon

# define a GasPump class to represent the gas pump
class GasPump:
    def __init__(self):
        # initialize the available fuel types and their prices
        self.fuel_types = [
            FuelType("Regular", 2.50),
            FuelType("Midgrade", 2.75),
            FuelType("Premium", 3.00)
        ]

        # initialize the fuel dispenser to an empty list
        self.dispenser = []

    def display_fuel_types(self):
        # display the available fuel types and their prices
        print("Available fuel types:")
        for fuel_type in self.fuel_types:
            print(f"{fuel_type.name}: ${fuel_type.price_per_gallon:.2f}/gallon")

    def select_fuel_type(self, fuel_type_name):
        # loop over the available fuel types and return the one with the specified name
        for fuel_type in self.fuel_types:
            if fuel_type.name.lower() == fuel_type_name.lower():
                return fuel_type
        # if no fuel type is found, return None
        return None

    def select_fuel_quantity(self, fuel_type, fuel_quantity):
        # calculate the total cost of the selected fuel
        total_cost = fuel_type.price_per_gallon * fuel_quantity

        # prompt the user to confirm the purchase
        print(f"Selected fuel type: {fuel_type.name}")
        print(f"Selected fuel quantity: {fuel_quantity:.2f} gallons")
        print(f"Total cost: ${total_cost:.2f}")
        confirmation = input("Confirm purchase (y/n)? ")

        # if the user confirms the purchase, add the fuel to the dispenser and return the total cost
        if confirmation.lower() == "y":
            self.dispenser.append((fuel_type, fuel_quantity))
            return total_cost
        else:
            # if the user does not confirm the purchase, return None
            return None

    def dispense_fuel(self):
        # if there is fuel in the dispenser, dispense the fuel and return True
        if self.dispenser:
            fuel_type, fuel_quantity = self.dispenser.pop()
            print(f"Dispensing {fuel_quantity:.2f} gallons of {fuel_type.name} fuel.")
            return True
        else:
            # if there is no fuel in the dispenser, return False
            print("No fuel available to dispense.")
