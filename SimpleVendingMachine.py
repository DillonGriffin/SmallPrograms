# define a VendingMachine class
class VendingMachine:
    def __init__(self):
        # initialize the available snacks and their prices
        self.snacks = {
            "chips": 1.50,
            "candy": 0.75,
            "water": 1.00,
            "soda": 1.25
        }

        # initialize the user's balance to 0
        self.balance = 0

    def deposit(self, amount):
        # add the amount to the user's balance
        self.balance += amount

    def purchase(self, snack):
        # check if the snack is available and the user has enough money
        if snack in self.snacks and self.balance >= self.snacks[snack]:
            # subtract the price of the snack from the user's balance
            self.balance -= self.snacks[snack]

            # return the snack
            return snack

        # if the snack is not available or the user does not have enough money, return None
        return None

# create a new VendingMachine object
vm = VendingMachine()

# deposit some money into the vending machine
vm.deposit(2.00)

# purchase a snack
snack = vm.purchase("chips")
if snack:
    print("Enjoy your", snack)
else:
    print("Sorry, that snack is not available or you do not have enough money.")
