# Snack Vending Machine

# Part 1:
def calculate_change(paid,price):
    change = paid - price
    return change

# Part 2:
total_price = 25
print(" ====== SNACK VENDING MACHINE ======")
print(f"This snack costs {total_price} units.")
print("Accepted coins -- 1 , 5 , 10 , 25.")

total_inserted = 0
coins_inserted = 0

# Part 3:
while True:
    coin = int(input("Insert a coin -- 1 , 5 , 10 , 25: "))
    
    # Part 4:
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin , please try again")
        continue
    
    # Part 5:
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin} . Total so far{total_inserted}\n")
    
    # Part 6:
    if total_inserted >= total_price:
        print("Enough money inserted.🤗")
        break

# Part 7:
change_due = total_inserted - total_price

print("Dispensing your snack...")

# Part 8:
if change_due == 0:
    pass
else:
    print(f"Here 's your change {change_due} units.🖐️")
    
# Part 9:
print("\n ====== PURCHASE SUMMARY ======")
print("Snack price        : ",total_price)
print("Coins inserted     : ",coins_inserted)
print("Total paid         : ",total_inserted)
print("Change given       :",change_due)
print(" ================================ ")
print("Thank you for your purchase.😊")
# End of program