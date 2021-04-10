class Budget():
    def __init__(self, category):
        self.category =  category
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": round(float(amount),2), "description": description})
        self.balance = self.balance + amount

    def withdraw(self, amount, description = ""):
        self.ledger.append({"amount": -1 * round(float(amount),2), "description": description})
        self.balance = self.balance - amount
        self.total_spend = self.total_spend + amount
        
    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_cat):
        self.withdraw(amount, "Transfer to " + target_cat.category)
        target_cat.deposit(amount, "Transfer from " + self.category)
        