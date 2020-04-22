class CoffeeMachine:

    def __init__(self, cash, water, milk, beans, throw_cups):
        self.cash = cash
        self.water = water
        self.milk = milk
        self.beans = beans
        self.throw_cups = throw_cups

    def main(self):

        action = input("Write action (buy, fill, take, remaining, exit) :" + "\n")

        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()
        elif action == "exit":
            global close
            close = 1
        else:
            return "Write either buy, fill, take, remaining or exit."

    def buy(self):
        """
        Buy an item if possible, then decrease stocks and print them.
        """
        item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:" + "\n")
        if item == "1":
            if self.water >= 250 and self.beans >= 16:
                print("I have enough resources, making you a coffee!")
                self.espresso()
            elif self.water < 250:
                print("Sorry, not enough water")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans")
        elif item == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
                print("I have enough resources, making you a coffee!")
                self.latte()
            elif self.water < 350:
                print("Sorry, not enough water")
            elif self.milk() < 75:
                print("Sorry, not enough milk")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans")
        elif item == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                print("I have enough resources, making you a coffee!")
                self.cappuccino()
            elif self.water < 200:
                print("Sorry, not enough water")
            elif self.milk < 100:
                print("Sorry, not enough milk")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans")
        elif item == "back":
            self.main()
        else:
            print("Write either 1, 2 or 3.")

    def espresso(self):
        self.water -= 250
        self.beans -= 16
        self.throw_cups -= 1
        self.cash += 4

    def latte(self):
        self.water -= 350
        self.milk -= 75
        self.beans -= 20
        self.throw_cups -= 1
        self.cash += 7

    def cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.beans -= 12
        self.throw_cups -= 1
        self.cash += 6

    def fill(self):
        """
        Ask how much of which ingredients to add, then prints current stocks.
        """
        plus_water = input("Write how many ml of water do you want to add:")
        plus_milk = input("Write how many ml of milk do you want to add:")
        plus_beans = input("Write how many grams of coffee beans do you want to add:")
        plus_cups = input("Write how many disposable cups of coffee do you want to add:")
        self.water += int(plus_water)
        self.milk += int(plus_milk)
        self.beans += int(plus_beans)
        self.throw_cups += int(plus_cups)

    def take(self):
        """
        Take all the money, then print how much the user withdrew, with current stocks.
        """
        money = self.cash
        self.cash -= self.cash
        return "\n" + "I gave you $" + str(money)

    def remaining(self):
        """
            Print current stocks.
        """
        print("\n" + "The coffee machine has:" + "\n"
              + str(self.water), "mL of water." + "\n"
              + str(self.milk), "mL of milk." + "\n"
              + str(self.beans), "g of coffee beans." + "\n"
              + str(self.throw_cups), "of disposable cups." + "\n$"
              + str(self.cash), "of money." + "\n"
              )


close = 0
machine = CoffeeMachine(550, 400, 540, 120, 9)
while close == 0:
    machine.main()
