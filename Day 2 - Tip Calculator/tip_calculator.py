print("Welcome to the Tip Calculator App!!")

bill = float(input("What was the total bill? $"))

print("The tip is 12%.")

people = float(input("How many people to split the bill? "))

amount_per_person = (bill/people) * 1.12
rounded_amount = round(amount_per_person,2)
rounded_amount = "{:.2f}".format(amount_per_person)
print(f"Each person with pay ${rounded_amount}.")