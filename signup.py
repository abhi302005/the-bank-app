def create_acc():
    import json
    temp_records=dict()
    records=dict()
    file=open("bank.json",mode="r+",encoding='utf-8')
    #temp_records=json.load(file)
    records=json.load(file)
    file.close()
    name=input("enter your name\n")
    age=int(input("enter your age\n"))
    if age<18:
            print("sorry you are not enaglabe\n")
    inital_bal=float(input("please enter your amount\n"))
    if inital_bal<2000:
        print("sorry please deposite minmum amount to open the account\n")
    email=input("enter the email\n")#email varifiaction
    username=input("enter the username\n")#user varifiaction
    n="abhi302005"
#     if username is temp_records["abhi302005"]:
    if username == n:
        print("\nplease enter the another user_name\n")
        username=input("enter the username\n")
    password=input("enter your password\n")
   # records.update({username:{"name":name,"age":age,"Balance":inital_bal,"email":email,"username":username,"password":password}})
    records[username]={"name":name,"age":age,"Balance":inital_bal,"email":email,"username":username,"password":password}
    print("thankyou")
    file=open("bank.json","w+")
    json.dump(records,file)
    file.close()
