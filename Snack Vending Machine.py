# Snack Vending Machine
# PART 1: A Function that works out change and sends it back with return
def calculate_change(paid, price):
    change = paid - price
    return change

# PART 2: See the snack price and greet the customer
snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"The price of the snack is: {snack_price} units")
print("Accepted Coins: 1,5,10,25\n")

total_inserted = 0
coins_inserted = 0

# PART 3: Keep Accepting Coins Until Enough Money is Inserted
while True:
    coin = int(input("Insert Coin (1, 5, 10, 25): "))
    
    # PART 4: Reject any coin that isn't a Valid Value
    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("Invalid Coin, try again\n")
        continue
    
    # PART 5: Add the Valid Coin to the running total
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")
    
    # PART 6: Stop asking for the coins once enough has been inserted
    if total_inserted >= snack_price:
        print("Enough Money Inserted!\n")
        print("Processing...")
        break
    
# PART 7: Work out the change using the value retuirned by calculate_change
change_due = calculate_change(total_inserted, snack_price)

print("Dispensing Your Snack...")

# PART 8: Nothing Extra to do when the change is exactly zero
if change_due == 0:
    pass
else:
    print(f"Here is your Change: {change_due} units")
    
# PART 9: Print a Short Summary of the Purchase
print("\n===== PURCHASE SUMMARY =====")
print("Snack Price:", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("==============================")
print("Thanks for your Pruchase")
# END OF MY PROGRAM. BYES!!