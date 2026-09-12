# Expense Tracker Project
expenseslist =[]
print("Welcome to Expence Tracker:")

while True:
    print("===Menu===")
    print("1. Add Expence")
    print("2. View All Expence")
    print("3. View total kharcha")
    print("4. Exit")

    choice =input("Enter your choise:")

    # Add expence
    if(choice == 1):
        date= input("kis date par kharch kiya tha")
        category= input("kis type ka kharcha kiya ? (Food, Travel,Mackup,books)")
        description=input("Aur detil dedo")
        amount= float(input("Enter the amount"))

        expense={
            "date": date,
            "category":category,
            "description":description,
            "amount": amount
        }

        expenseslist.append(expense)
        print("\n Done bro. Expense is added succesfully")


        #2 view all expenses
    if(choice==2):
        if(len(expenseslist)==0):
            print("No expenses added. jao pahle kharch karo.")
        else:
            print("====ye apka sra expence====")
            count=1
            for eachkharcha in expenseslist:
                print(f"kharcha number{"count"}->{eachkharcha["data"]},{eachkharcha["category"]},{eachkharcha["description"]},{eachkharcha["amount"]}")
                count= count+1

    if(choice==3):
        total=0
        for eachkharcha in expenseslist:
            total= total+ eachkharcha["amount"]

        print("\n total khrcha=",total)


    elif(choice==4):
        print("Dhanywad aapko humara sysem use kiya")
        break
    else:
        print("invalid choice. try again")
