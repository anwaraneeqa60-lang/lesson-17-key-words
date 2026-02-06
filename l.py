bill_amount = float(input("enter the bill amount: "))
amount_paid = float(input("enter the amount paid by the customer: "))
due_amount = bill_amount - amount_paid
if due_amount > 0:
    print(f"the customer still owes ${due_amount:.2f}")
elif due_amount < 0:
    print(f"change to return: ${abs(due_amount):.2f}")
else:
    print("bill fully paid. no due amount")