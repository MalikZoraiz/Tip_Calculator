print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_Percent = tip/100
total_tip_amount = bill * tip_as_Percent
total_bill = bill + total_tip_amount
bill_per_percon = total_bill / people
final_amount = round(bill_per_percon, 2)
final_amount = "{:.2f}".format(bill_per_percon)
print(f"each person should pay: ${final_amount}")
