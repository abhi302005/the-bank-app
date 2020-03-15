
def login():
    import json
    records=dict()
    file=open("bank.json",mode="r+",encoding='utf-8')
    records=json.load(file)
    file.close()
    entered_user=input("please enter the username\n")
    if entered_user in records:
        entered_password=input("please enter your password")
        if entered_password==records[entered_user]["password"]:
            print("\nuser's information\n")
            print(records[entered_user]["name"])
            print(records[entered_user]["age"])
            print(records[entered_user]["Balance"])
            user_choice=int(input("\npress 1 to Debit the amount of your account \n press 2 to Credit the amount of your account \n press 3 to logout "))
            if user_choice<3:
                if user_choice==1:#debit the Balance
                        #a function can be called to debit the balance.
                    if records[entered_user]["Balance"]<2000:
                        print("insufficent amout please contact to Bank")
                    else:
                        enter_amt=float(input("enter the amount to Debit"))
                        if records[entered_user]["Balance"]<enter_amt:
                            print("insufficent amout please contact to Bank")
                        else:
                            temp=records[entered_user]["Balance"]-enter_amt
                            if temp<2000:
                                print("insufficent amout please contact to Bank")
                            else:
                                records[entered_user]["Balance"]=temp
                                print("updated Balance :\t",records[entered_user]["Balance"])
                                file=open("bank.json","w+")
                                json.dump(records,file)
                                file.close()
                if user_choice==2:#credit the Balance
                        #a function can be called to credit the balance.
                    enter_amt=float(input("enter the amount to credit in your account"))
                    records[entered_user]["Balance"]+=enter_amt
                    print("\nupdated amount of account:\t",records[entered_user]["Balance"])
                    file=open("bank.json","w+")
                    json.dump(records,file)
                    file.close()

            else:
                print("thank you for using our services")
#                 exit()
