from day15.Config import Config


class CoffeeMachine:
    def __init__(self):
        self.money = Config.INITIAL_MONEY
        self.water = Config.resources['water']
        self.milk = Config.resources['milk']
        self.coffee = Config.resources['coffee']
        self.state = False
        self.coffee_type = ''

    def run(self):
        self.state = True
        print('beep! machine is running!')
        while True:
            self.get_user_input()
            # Check resources, then insert coins. If enough, make the coffee.
            if not self.check_resources() or not self.insert_coins():
                continue
            else:
                self.make_coffee()

    def turn_off(self):
        self.state = False
        print('Turning off.')
        print('bzzz...')
        quit()

    def make_coffee(self):
        self.reduce_ingredients()
        print('Bzzzzz...')
        print('Pff...')
        print('Bing!')
        print(f"Here's your {self.coffee_type} ☕. Enjoy!")

    def reduce_ingredients(self):
        self.water -= Config.MENU[self.coffee_type]['ingredients']['water']
        self.milk -= Config.MENU[self.coffee_type]['ingredients']['milk']
        self.coffee -= Config.MENU[self.coffee_type]['ingredients']['coffee']

    def get_user_input(self):
        while True:
            self.coffee_type = input('What would you like? (espresso/latte/cappuccino): ')
            if self.coffee_type == 'espresso' or self.coffee_type == 'latte' or self.coffee_type == 'cappuccino':
                return self.coffee_type
            elif self.coffee_type == 'report':
                self.report()
            elif self.coffee_type == 'Off':
                self.turn_off()
            else:
                print('Wrong coffee type!')

    def check_resources(self):
        if Config.MENU[self.coffee_type]['ingredients']['water'] > self.water:
            print('Not enough water!')
            return False
        if Config.MENU[self.coffee_type]['ingredients']['milk'] > self.milk:
            print('Not enough milk!')
            return False
        if Config.MENU[self.coffee_type]['ingredients']['coffee'] > self.coffee:
            print('Not enough coffee!')
            return False
        return True

    def insert_coins(self):
        quarters = int(input('Insert Quarters (0,25$)'))
        dimes = int(input('Insert Dimes (0,10$)'))
        nickles = int(input('Insert Nickles (0,05$)'))
        pennies = int(input('Insert Pennies (0,01$)'))

        inserted_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        if inserted_money < Config.MENU[self.coffee_type]['cost']:
            print('Not enough monies. Monies refunded.')
            return False
        else:
            money_returned = inserted_money - Config.MENU[self.coffee_type]['cost']
            print(f'Here is {money_returned:.2f}$ of change.')
            self.money += Config.MENU[self.coffee_type]['cost']
            return True

    def report(self):
        print(
            f"Water: {self.water}\n"
            f"Milk: {self.milk}\n"
            f"Coffee: {self.coffee}\n"
            f"Money: {self.money}"
        )


if __name__ == "__main__":
    workplace_coffeemaker = CoffeeMachine()
    workplace_coffeemaker.run()
