print("__Welcome to The Bill Calculator__\n")

bill = int(input("Your total bill : Rs."))
tip_percent = float(input("What percent of tip would you like to give?(Do not enter % symbol) \n"))
split = int(input("How many people to split the bill?\n"))

total_amount = bill + bill * (tip_percent / 100)
individual_pay = "{:.2f}".format(round(total_amount / split, 2))

print(f"Each person should pay : Rs.{(individual_pay)}")
