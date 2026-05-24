class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{desc:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    print("Percentage spent by category")
    spent_per_category = []
    for category in categories:
        spent = sum(abs(item["amount"]) for item in category.ledger if item["amount"] < 0)
        spent_per_category.append(spent)
        
    total_spent = sum(spent_per_category)
    
    # 2. Calculate percentages rounded down to the nearest 10
    # Guard against division by zero if nothing has been spent yet
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in spent_per_category]
        
    # 3. Build the chart top-down (from 100% down to 0%)
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    # 4. Add the horizontal separator line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # 5. Write category names vertically
    max_len = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_len) for category in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in padded_names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart