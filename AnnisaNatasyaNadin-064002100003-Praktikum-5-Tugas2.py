total = 0
while True:
    try:
        age = int(input("Enter your age : "))
    except ValueError:
        break
    if age <= 2:
            print("Free")
    elif age in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            total += 14.00
            print("Fee : $14.00")
            print("Running total : $", total)
    elif age >= 65:
            total += 18.00
            print("Fee : $18.00")
            print("Running total : $", total)
    else:
            total += 23.00
            print("Fee : $23.00")
            print("Running total : $", total)
            
money = int(input("Enter your money : "))
if money > total:
    pay = money - total
    print("Change : $", pay)
elif money < total:
    pay = total - money
    print(f"Sorry, you don't have enough money, you must pay ${pay} more")
else:
    print("That's an exact amount of money, thank you!")
