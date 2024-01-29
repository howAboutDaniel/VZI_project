class Expense:
    def __init__(self, date, currency, name, amount, category, reciever, account, note) -> None:
        self.date = date               # date of an expense
        self.currency = currency       # currency of an expense
        self.name = name               # name of an expense
        self.amount = amount           # expense's amount
        self.category = category       # expense's category
        self.reciever = reciever       # reciever of an expense
        self.account = account         # 3 letter account shortcut, from which an expense was made
        self.note = note               # short description of an expense

    def __repr__(self):
        return f"<Expense: {self.date}, {self.currency}, {self.name}, ${self.amount:.2f}, {self.category}, {self.reciever}, {self.account}, {self.note} >"
