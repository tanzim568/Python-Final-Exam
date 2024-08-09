#user section




class User: 
    def __init__(self,name,email,address) -> None: 
        self.name=name
        self.email=email
        self.address=address
      
        # self.bank=Bank('IBBL','SME')
        

class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type=account_type
        self.account_no=None  
        self.balance=0
        # self.transaction=Transaction()
        self.loan_amount=2
        self.transaction_history=[]
    
    def create_account(self,bank):
        bank.create_account(self)
        self.account_no=self.name+self.email  #later add kora hoyeche
        print(f"Account Creation Success ! ")
        print(f"Account No :{self.account_no}")
    
    
    def deposite(self,amount,bank):
        if bank.bankrupt == False:
            self.balance+=amount
            bank.total_balance+=amount
            print(f"Deposited {amount} to account_no :{self.account_no}")
            self.transaction_history.append(f"Deposited +{amount} ")
        else:
            print("The bank is bankrupted !")    
        
    def check_balance(self):
        return self.balance
    
    def withdrawal(self,amount,bank):
        if bank.bankrupt == True or amount > self.balance:
            print(f'Withdrawal amount exceeded or Bankrupted')
        else:
            self.balance -= amount
            bank.total_balance-=amount
            print(f"Withdrawal of amount :{amount} successful !")
            self.transaction_history.append(f"Withdraw amount -{amount}")
            
    def fund_transfer(self,account_no,amount,bank):
        for customers in bank.accounts_list:
            if customers.account_no == account_no:
                if self.balance >=amount and bank.bankrupt==False:
                    self.balance -= amount
                    customers.balance += amount
                    print(f'Fund transfer successfull at account {customers.account_no}')
                    self.transaction_history.append(f"Deposited :{amount} to account :{customers.account_no}")
                    customers.transaction_history.append(f"Received {amount} from account_no : {self.account_no}")
                    return ""
                else:
                    print(f"Fund transfer Incomplete or Bankrupted!")  
                    return ""  
                # self.transaction_history()
        print(f"Account Doesn't exist !")
    # def transaction_history(self):
    #     self.transaction.trnasaction_list()
    def take_loan(self,amount,bank):
        if self.loan_amount >0 and bank.loan_status==False and bank.bankrupt == False:
            self.balance+=amount
            bank.total_loan+=amount
            self.loan_amount -=1
            print(f"Loan amount added !")
        else:
            print("Loan Times exceeded or Bankrupted !")
            
         
                

    
            
           
                    
                
        
    

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)
        
    def create_account(self,customer,bank):
        # bank.create_account(customer)
        customer.create_account(bank)
    
    def delete_account(self,account_no,bank):
        print(bank.delete_account(account_no))
    
    def show_users(self,bank):
        bank.show_users()
        
    
    def total_balance(self,bank):
        bank.total_balance()
        
    def total_loan_amount(self,bank):
        return bank.total_loan
    
    def bankrupt(self,val,bank):
        if val==0:
            bank.bankrupt=False
        elif val==1:
            bank.bankrupt=True
        else :
            print("Invalid input for bankrupt")
    
    def loan_status(self,val,bank):
        if val==0:
            bank.loan_off()
        elif val==1:
            bank.loan_on()
        else:
            print('Val/Input incorrect')
            
        
    



#bank section



class Bank:
    def __init__(self,name,branch) -> None: 
        self.name=name
        self.branch=branch
        self.accounts_list=[]
        self.total_balance=0
        self.total_loan=0
        self.loan_status=False
        self.bankrupt=False
        
    def create_account(self,customer):
        self.accounts_list.append(customer)
        # return
        # for account in self.accounts_list:
        #     print(f"Account holder name :{account.name}\tAddress :{account.address}\tType :{account.account_type}\t Account_no :{account.account_no}")
        #     print(f"account balance :{account.balance}")
        
        
    def delete_account(self,account_number):  #Admin access 
        for acc in self.accounts_list:
            if account_number == acc.account_number:
                # print(f"Deleted user :{acc.name}") need to solve later
                self.accounts_list.remove(acc)
                return f"User Deleted"
        return f"User not found"
        

    def show_users(self):
        for account in self.accounts_list:
            print(f"Account holder name :{account.name}\tAddress :{account.address}\tType :{account.account_type}\t Account_no :{account.account_no}")
            # print(f"account balance :{account.balance}")   
            # print("Object address in memory",account)    #for printing object address details in main.py object history
        
    # def show_users(self):   #Admin access
    #     for account in self.accounts_list:
    #         print(f"Account holder name :{account.name}\tAddress :{account.address}\tType :{account.account_type}\t Account_no :{account.account_no}")
            
            
    def find_accont(self,account_no):
        for accounts in self.accounts_list:
            if account_no == accounts.account_no:
                return accounts
                
   
            
    # def list_clear(self):
    #     self.accounts_list.clear()        
            
    def total_balance(self):   #Admin access
        print(self.total_balance)
        
        
    def total_loan(self):   #Admin access
        print(self.total_loan)
        
    
    def loan_off(self):   #Admin access
        self.loan_status=False
        
    def loan_on(self):   #Admin access
        self.loan_status=True
    
        
        
#main section

ibbl=Bank('Ibbl','SME')
admin=Admin('admin','admin@gmail.com','Dhaka')
currentUser=None
while True:
    if currentUser == None:
        
        print("\n----------------------\nWelcome to the System !\n----------------------")
        print("1. Admin \n2. User\n3. Exit")
        ch=input("\nEnter Choice :")
        if ch=='1':
            currentUser=admin
            print("\n----------------------\nWelcome to Admin Panel !\n----------------------")
            print("\n1. Create Account\n2. Delete Account\n3. See all users\n4. Total Available Balance\n5. Total loan amount\n6. Loan feater\n7. Bankrupt enable/disable\n8. Log out")
    
            op=input("\nEnter Choice :")
            if op=='1':
                
                name=input("enter name :")
                email=input("enter email :")
                address=input("enter address :")
                acc_type=input("enter account_type (Savings/Current) :")
                cusomer=Customer(name,email,address,acc_type)
                admin.create_account(cusomer,ibbl)
                # print("main e asche")
                
                
            elif op =='2':
                acc_no=input("Enter account_no :")
                admin.delete_account(acc_no,ibbl)
                
            elif op=='3':
                admin.show_users(ibbl)
                # .
            elif op=='4':
                admin.total_balance(ibbl)
            
            elif op=='5':  # total koto loan neya hoyeche bank theke
               print(admin.total_loan_amount(ibbl))
                
            elif op == '6':
                switch=int(input("Type 0 for off/1 for no :"))
                admin.loan_status(switch,ibbl)
                
            elif op=='7':
                sw=int(input("Type 0 for off/1 for no : "))
                admin.bankrupt(sw,ibbl)
                    
            elif op =='8':
                currentUser=None
                print("Logged Out")
                
        elif ch == '2':
            if currentUser==None:
                option=input("\nLog in or Create Account (L/C)?")
                if option == 'L':
                   
                        acc_no=input("Enter account_no :")
                        user=ibbl.find_accont(acc_no)
                        if user:
                            currentUser=user
                            print(f"\nWelcome to the system {user.name}")
                            print("\n1. Deposite\n2. Withdraw \n3. Check Balance\n4. Check Transaction history\n5. Take Loan\n6. Fund Transfer\n7. Log Out")
                            option=input("Enter choice :")
                            if option=='1':
                                #deposite will be written later
                                amount=int(input("Enter amount :"))
                                user.deposite(amount,ibbl)
                                
                            elif option =='2':
                                amount=int(input("Enter withdraw amount :"))
                                user.withdrawal(amount,ibbl)
                                
                            elif option == '3':
                                print(user.check_balance())
                                
                            elif option =='4':
                                for story in user.transaction_history:
                                    print(story)
                                    
                            elif option =='5':
                                amount=int(input("Enter loan amount :"))
                                user.take_loan(amount,ibbl)
                                
                            elif option =='6':
                                acc_no=input("Enter receiver account_no :")
                                amount=int(input("Enter amount :"))
                                user.fund_transfer(acc_no,amount,ibbl)
                            
                            elif option == '7':
                                currentUser=None
                                print("No logged in User")
                            
                        else:
                            print(f"User doesn't exist !")    

                elif option =='C':
                    name=input("enter name :")
                    email=input("enter email :")
                    address=input("enter address :")
                    acc_type=input("enter account_type (Savings/Current) :")
                    user=Customer(name,email,address,acc_type)
                    user.create_account(ibbl)
                    currentUser=user
                    
        elif ch == '3':
            break
        
        else:
            print("Invalid Input")            
                
    elif currentUser.name == 'admin':
        
        print("\n1. Create Account\n2. Delete Account\n3. See all users\n4. Total Available Balance\n5. Total loan amount\n6. Loan feater\n7. Bankrupt enable/disable\n8. Log out")
        op=input("\nEnter Choice :")
        if op=='1':
                
            name=input("enter name :")
            email=input("enter email :")
            address=input("enter address :")
            acc_type=input("enter account_type (Savings/Current) :")
            cusomer=Customer(name,email,address,acc_type)
            admin.create_account(cusomer,ibbl)
                
                
        elif op =='2':
            acc_no=input("Enter account_no :")
            admin.delete_account(acc_no,ibbl)
                
        elif op=='3':
            admin.show_users(ibbl)
                
        elif op=='4':
            admin.total_balance(ibbl)
            
        elif op=='5':  # total koto loan neya hoyeche bank theke
            print(admin.total_loan_amount(ibbl))
                
        elif op == '6':
            switch=int(input("Type 0 for off/1 for on :"))
            admin.loan_status(switch,ibbl)
            
        elif op=='7':
            sw=int(input("Type 0 for off/1 for on : "))
            admin.bankrupt(sw,ibbl)
                
        elif op =='8':
            currentUser=None
            print("Logged out of admin")
    
    else:
            print(f"\nWelcome to the system {user.name}")
            print("\n1. Deposite\n2. Withdraw \n3. Check Balance\n4. Check Transaction history\n5. Take Loan\n6. Fund Transfer\n7. Log Out")
            option=input("Enter choice :")
            if option=='1':
                #deposite will be written later
                # pass
                amount=int(input("Enter amount :"))
                user.deposite(amount,ibbl)
                
            elif option =='2':
                amount=int(input("Enter withdraw amount :"))
                user.withdrawal(amount,ibbl)
                
            elif option == '3':
                print(user.check_balance())
                
            elif option =='4':
                for story in currentUser.transaction_history:
                    print(story)
                    print()
                    
            elif option =='5':
                amount=int(input("Enter loan amount :"))
                user.take_loan(amount,ibbl)
                
            elif option =='6':
                acc_no=input("Enter receiver account_no :")
                amount=int(input("Enter amount :"))
                user.fund_transfer(acc_no,amount,ibbl)
            
            elif option == '7':
                currentUser=None
                print("No logged in User")

     
















































































# while True:
    
#     ch=int(input("enter 1/2/3 (create/show/exit) :"))
#     if ch==1:
#         name=input("enter name :")
#         email=input("enter email :")
#         address=input("enter address :")
#         acc_type=input("enter account_type :")
#         cust=Customer(name,email,address,acc_type)
#         cust.create_account(ibbl)
#     elif ch==2:
#         ibbl.show_users()
        
#     elif ch ==3:
#         account_no=input("enter account_no :")
#         amount=int(input("enter amount"))
#         cust.fund_transfer(account_no,amount,ibbl)
#     elif ch==4:
#         op=input("Log in/// account_no : ")
#         user=ibbl.find_accont(op)
#         print(user.transaction_history)
        
#     else:
#         break
        
# cust1=Customer('rahim','rahim@mail','dHAKA','SVE')
# cust1.create_account(ibbl) 
# cust2=Customer('kahim','kahim@mail','dHAKA','SVE')
# admin=Admin('admin','admin@gmail.com','Dhaka')
# cust2.create_account(ibbl)

# cust1.fund_transfer('kahimkahim@mail',500,ibbl)
# print(cust2.transaction_history)


""" while loop e hoy ki je ekbar sob data niye ekta object create hoi then abar data fillup hoi .. 
then cust object push hoi then abar new data fill up hoi and same object name initialize hoi then oita push hoi 
but 2 ta object er name same hoileo memory address differenct hoi.. cz python e 

[ --copied from google 

   Everything in Python is an object, 
   and each object is stored at a specific memory location. 
   The Python is and is not operators check whether two variables refer to the same object in memory. 
   Note: Keep in mind that objects with the same value are usually stored at separate memory addresses.
    
]


    """
# admin.create_account(rahim,ibbl)
# ibbl.list_clear()
# acc=Account(rahim,ibbl)
# acc=Account(kahim,ibbl)
# admin=Admin('ADMIN','admin@gmail.com','Chattogram')
# admin.bank.create_account(acc)
# acc=Account(kahim,ibbl)
# rahim.create_account(ibbl)
# kahim.create_account(ibbl)
# rahim.create_account(acc)
# ibbl.show_users()
# admin.bank.show_users()

            
    