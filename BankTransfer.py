import datetime
from datetime import datetime

class Bank:
    
    def __init__(self):
        self.all_accounts = {}
        
    def open_account(self, name, account_number, born, money):
        account = {
            'name': name,
            'number': account_number,
            'born': born,
            'money': money,
            'number_of_deposits': 0,
            'number_of_withdraws': 0,
            'history': []
        }
        self.all_accounts[account_number] = account
    
    def show_accounts(self, show_history=False):
        for number, account in self.all_accounts.items():
            print('\n---', number, '---\n')
            self.description(number)
            if show_history:
                print('History:', account['history'])
            
    def get_acc_for_history(self):
        return self.all_accounts
        

    def transfer(self, account_number1, account_number2, value):
        # check if it can withdraw
        if self.withdraw(account_number1, value, account_number2, True):
            self.deposit(account_number2, value, account_number1, True)
     
    def get_account(self, number):
        return self.all_accounts[number]

    # -- from Account, need account_number as first argument ---
    
    def description(self, number):
        account = self.get_account(number)
        print("Name is: " , account['name'])
        print("Account Number: " , account['number'])
        print("Money: " , account['money'])
        
    def deposit(self, number, value, accno, flag):
        account = self.get_account(number)
        account['money'] += value
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if flag == True:
            account['history'].append((str(dt_string), str(number), str(accno), "Transfer ", str(+value)))
        else:
            account['history'].append((str(dt_string), str(number), str('X'), "Deposit ", str(+value)))
        account['number_of_deposits'] += 1
        return True
    
    def withdraw(self, number, value, accno, flag):
        account = self.get_account(number)
        if account['money'] < value:
            print(f'{self.name} no enought money')
            return False
        
        account['money'] -= value
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if flag == True:
            account['history'].append((str(dt_string), str(number), str(accno), "Transfer ", str(-value)))
        else:
            account['history'].append((str(dt_string), str(number), str('X'), "Deposit ", str(-value)))
        account['number_of_withdraws'] += 1
        return True
    
    def transaction_history(self, number):
        account = self.get_account(number)
        today = datetime.datetime.now()
        print("You have withdraw", account['number_of_withdraws'] , "On date:" , today)
        print("You have deposit" , account['number_of_deposits']  , "On date:" , today)
        
    def take_loan(self, number):
        account = self.get_account(number)
        answer = int(input("Enter the amount of loan who would you like to take between - 100Euros and 300 Euros: "))
        if answer > 300:
            print("Choose between 100 - 300 Euros not more")
        else:
            print("You have taken out for loan, you will pay extra 1.5 from that sum" , answer * 1.5)

# --- main ---        
        
'''bank = Bank()
bank.open_account("Bill", 42919502, "Massachutes", 4000)
bank.open_account("John", 30503202104, "Cardiff", 4000)

bank.deposit(42919502, 500)
bank.withdraw(30503202104, 1200)

print('\n===== before =====\n')
bank.show_accounts(show_history=True)

bank.transfer(42919502, 30503202104, 100)
bank.transfer(42919502, 30503202104, 300)
bank.transfer(30503202104, 42919502, 500)

print('\n===== after =====\n')
bank.show_accounts(show_history=True)'''