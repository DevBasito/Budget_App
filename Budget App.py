
class Budget:
    
    def __init__(self, category):
        self.category= category
        self.bal= 0
 
        

    def deposit_funds(self, deposit):
        self.bal += deposit
        return f'You deposited {deposit} to {self.category}. Your {self.category} Balance is {self.bal}'

    def withdraw_funds(self, withdrawal): 
        if withdrawal > self.bal:
            return 'Insufficient Funds'  
        else:
            self.bal -= withdrawal
            return f'You made a withdrawal of {withdrawal} from {self.category}. Your current {self.category} Balance is {self.bal}'


    def transfer_funds(self, funds_transf, new_category):
        if funds_transf > self.bal:
            return f'Insufficient Funds! You cannot make funds transfer'
        else:
            self.bal -= funds_transf
            new_category.bal += funds_transf

            return f'You transfered {funds_transf} from {self.category} to {new_category.category}. Your current {self.category} Balance is {self.bal} and your new {new_category.category} Balance is {new_category.bal}'
        



Food = Budget('Food')

Clothing= Budget('Clothing')

Entertainment= Budget('Entertaiment')

# print(Clothing.deposit_funds(800))
# print(Food.deposit_funds(3500))
# print(Entertainment.deposit_funds(1000))

# print('='*30)

# print(Entertainment.withdraw_funds(2000))
# print(Food.withdraw_funds(500))

# print('='*30)

# print(Food.transfer_funds(5000, Clothing))
# print(Food.transfer_funds(500, Clothing))
# print(Clothing.withdraw_funds(300))
# print(Clothing.deposit_funds(200))





