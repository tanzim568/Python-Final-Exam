

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
    
        
        