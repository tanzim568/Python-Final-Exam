


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
            
        
    