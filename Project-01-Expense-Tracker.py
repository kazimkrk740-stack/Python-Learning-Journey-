# Expense Tracker project

expenseslist=[] # list of expense in from dictionary
print("Welcome to expence tracker")

while True:
  print("===== MENU =====")
  print("1. Add Expenses")
  print("2. View all Expenses")
  print("3. View Total cost")
  print("4. EXIT")
  
  choice=int(input("Please Enter your choice number :"))

# Add Expenses
  if choice==1:
    date=(input("What was the expense on this date?"))
    categroy=(input("What's type on you spent on money?"))
    discripation=(input("Datils about:"))
    amount=float(input("Enter Your amount:"))

    expense={
      "date": date,
      "categroy": categroy,
      "discripation": discripation,
      "amount": amount
    }

    expenseslist.append(expense)
    print("\n Done BRO. Expense added SUCCEFULLY")

# 2. View all Expenses
  elif choice ==2:
    if(len(expenseslist)==0):
      print("No Expenses Added. Go spend some money.")
    else:
      print("=== ===This Your expense:=== ===")
      count = 1

      for eachexpenses in expenseslist:
        print(f"Expenses number {count} => {eachexpenses['date']}, {eachexpenses['categroy']}, {eachexpenses['discripation']}, {eachexpenses['amount']}")
        count = count+1
  
# 3. View Total cost
  elif choice==3:
    total=0
    for eachexpenses in expenseslist :
      total = total + eachexpenses["amount"]

    print("\n Total Expense =",total)

# EXIT
  elif choice == 4:
    print("Thank you so much for using this program.\n I think you like it....!!!")
    break 

  else:
    print("INVALID CHOICE. \n TRY AGAIN....!!!")
  