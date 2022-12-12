class BankAccount:
    Bank_Name = 'Jordans Federal Credit Union'
    # Basic_int_rate = .01
    # Pro_int_rate = .025
    # Business_int_rate = .035
    your_int_rate = .01


    def __init__(self, name, checking, savings):
        self.name = name
        self.int_rate = .01
        self.checking = checking
        self.savings = savings

    def deposit(self, account_type, amount):
        if account_type == 'checking':
            self.checking = self.checking + amount
            if self.savings >= 10000:
                self.int_rate = .035
                return self
            elif self.savings >= 2500:
                self.int_rate = .025
                return self
            elif self.savings < 2500:
                self.int_rate = .01
                return self
        elif account_type == 'savings':
            self.savings = self.savings + amount
            if self.savings >= 10000:
                self.int_rate = .035
                return self
            elif self.savings >= 2500:
                self.int_rate = .025
                return self
            elif self.savings < 2500:
                self.int_rate = .01
                return self

    
    def withdraw(self, account_type, amount):
        if account_type == 'checking':
            if amount > self.checking:
                print('You have insufficient funds: you will be charged a 5$ overdraft fee')
                self.checking = self.checking - amount - 5
                print(f'Your updated balance is ${round(self.checking, 2)}')
                if self.savings >= 10000:
                    self.int_rate = .035
                    return self
                elif self.savings >= 2500:
                    self.int_rate = .025
                    return self
                elif self.savings < 2500:
                    self.int_rate = .01
                    return self
            else:
                self.checking = self.checking - amount
                print(f'Your updated balance is ${round(self.checking, 2)}')
                if self.savings >= 10000:
                    self.int_rate = .035
                    return self
                elif self.savings >= 2500:
                    self.int_rate = .025
                    return self
                elif self.savings < 2500:
                    self.int_rate = .01
                    return self
        elif account_type == 'savings':
            if amount > self.savings:
                print('You have insufficient funds: you will be charged a 5$ overdraft fee')
                self.savings = self.savings - amount - 5
                print(f'Your updated balance is ${round(self.savings, 2)}')
                if self.savings >= 10000:
                    self.int_rate = .035
                    return self
                elif self.savings >= 2500:
                    self.int_rate = .025
                    return self
                elif self.savings < 2500:
                    self.int_rate = .01
                    return self
            else:
                self.savings = self.savings - amount
                print(f'Your updated balance is ${round(self.savings, 2)}')
                if self.savings >= 10000:
                    self.int_rate = .035
                    return self
                elif self.savings >= 2500:
                    self.int_rate = .025
                    return self
                elif self.savings < 2500:
                    self.int_rate = .01
                    return self

    def display_account_info(self, account_type):
        if account_type == 'checking':
            print(f'Hello {self.name} ||| ${round(self.savings, 2)}||')
            print('|__________________________________________________________________________')
            return self
        elif account_type == 'all':
            print('|__________________________________________________________________________')
            print(f'|Hello {self.name} ||Your checking balance is:|| ${round(self.checking, 2)}|')
            print('|__________________________________________________________________________')
            print(f'|Hello {self.name} ||Your savings balance is:|| ${round(self.savings, 2)}|')
            print('|__________________________________________________________________________')
            return self

    def yeild_interest(self):
        print(f'Current interest rate: {self.int_rate}')
        self.savings = round(self.savings + (self.savings * self.int_rate),2)
        if self.savings >= 10000:
            self.int_rate = .035
            return self
        elif self.savings >= 2500:
            self.int_rate = .025
            return self
        elif self.savings < 2500:
            self.int_rate = .01
            return self

    def tansfer_money(self, username, account_type, amount):
        user = username
        account = account_type
        if account_type == 'checking':
            account = user.checking
        elif account_type == 'savings':
            account = user.savings
        
        user.savings += amount
        Member_Jordan.savings -= amount
        
        



    @classmethod
    def get_bank_info(cls):
        print(BankAccount.Bank_Name)
        print(BankAccount.your_int_rate)


# classifying a child class inheriting parent attributes
class Checking_Account(BankAccount):
    def __init__(self, name, check_rate, checking, savings, testing):
        super().__init__(name, checking, savings)
        self.check_rate = check_rate
        self.testing = testing

    #using the inheritance for a method in parent class


    def withdraw(self, account_type, amount, testing):
        self.name = testing

        super().withdraw(account_type, amount)
        return self

jordan = Checking_Account('jordan', 543210, 4000, 3000, '????')
jordan.withdraw('checking', 500, 'yolo')
print(jordan.name)



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount('Bryan', 1500, 5000, )
    
    def make_deposit(self,account_type, amount):
        self.account.deposit(account_type, amount)
        if account_type == 'checking':
            print(f'Your current checking balance is: ${round(self.account.checking, 2)}')
            return self
        elif account_type == 'savings':
            print(f'Your current savings balance is: ${round(self.account.savings, 2)}')
            return self

    
    def make_withdrawal(self, account_type, amount):
        self.account.withdraw(account_type, amount)
        if account_type == 'checking':
            print(f'Your current checking balance is: ${round(self.account.checking, 2)}')
            return self
        elif account_type == 'savings':
            print(f'Your current savings balance is: ${round(self.account.savings, 2)}')
            return self
    
    def display_user_balance(self):
        print(self.account.balance)
        return self

Member_Jordan = BankAccount('Jordan Ronk', 500, 2500)
Member_Bryan = BankAccount('Bryan Cord', 1500, 5000)
# Member_Bryan = User('Bryan Cord', ' bryanbbgun@gmail.com')

# Member_Jordan.display_account_info('all')
# Member_Bryan.display_account_info('all')
Member_Jordan.tansfer_money(Member_Bryan, 'savings', 500)
Member_Jordan.display_account_info('all')
Member_Bryan.display_account_info('all')
# Member_Bryan.account.deposit('savings', 10341).yeild_interest()
# Member_Bryan.make_deposit('savings', 1000).make_withdrawal('savings', 20000)
# Member_Bryan.account.display_account_info('all')
# Member_Jordan.deposit('savings', 15000).withdraw('checking', 1000).yeild_interest()

# Member_Jordan.display_account_info('all')







