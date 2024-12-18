class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  
        self.amount = amount  
 
    def __repr__(self):
        return repr((self.currency, self.amount))
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception("Currencies Do Not Match")
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)
        


value1 = Currency("USD", 20)
value2 = Currency("USD", 30)
value3 = Currency("INR",30)
print(value1 + value2)  
# print(value1 + value3)  exception occurs