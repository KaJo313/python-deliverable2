#Step 1: Prompt shopper for their name, and initialize key program elements:
# create dictionaries containing fruit prices and purchase(s);
# initialize flag used for the 'while' loop
shopper_name = input("Welcome to Fruit Market! What is your name? ")

fruit_prices = {'apple': 2, 'grape': 1, 'orange':3}
fruit_quantity = {'apple': 0, 'grape': 0, 'orange':0}
buy_more_flag = "y"

#Step 2: Display fruits, enumerated with prices; prompt shopper for purchase selection
while buy_more_flag == "y":
    print("\n"f"Welcome {shopper_name}. Which Fruit would you like to buy?")
    for i, (fruit, price) in enumerate(fruit_prices.items(), start = 1):
        print(f" {i}. {fruit.title()} ${price}")

    fruit_selection = int(input())

    #Step 3: Display quantity of fruit purchased and its price;
    # add quantity purchased to fruit_quantity dictionary
    if int(fruit_selection) == 1:
        print(f"You bought 1 apple at ${fruit_prices['apple']}")
        fruit_quantity['apple'] += 1
    elif int(fruit_selection) == 2:
        print(f"You bought 1 grape at ${fruit_prices['grape']}")
        fruit_quantity['grape'] += 1
    elif int(fruit_selection) == 3:
        print(f"You bought 1 orange at ${fruit_prices['orange']}")
        fruit_quantity['orange'] += 1
    else:
        print("You did not enter a valid number. Please try again.")

    #Step 4: Prompt shopper about whether they want to buy more fruit
    buy_more_flag = input("Would you like to buy another piece of fruit? y/n ")

#Step 5: Final Order Tally
print("\n"f"Receipt for {shopper_name}")
print(f"You bought {fruit_quantity['apple']} apple(s) at ${fruit_prices['apple']} apiece")
print(f"You bought {fruit_quantity['grape']} grape(s) at ${fruit_prices['grape']} apiece")
print(f"You bought {fruit_quantity['orange']} orange(s) at ${fruit_prices['orange']} apiece")
sub_total = ((fruit_quantity['apple'] * fruit_prices['apple']) +
             (fruit_quantity['grape'] * fruit_prices['grape']) +
             (fruit_quantity['orange'] * fruit_prices['orange']))
print(f"Sub Total: ${sub_total}")
tax = sub_total * .05
print(f"5% Tax: ${tax}")
total = sub_total + tax
print(f"Total: ${total}")

