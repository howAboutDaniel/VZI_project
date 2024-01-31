class Expense:
    def __init__(self, date, currency, name, amount, category, reciever, account) -> None:
        self.date = date               # Dátum výdaju
        self.currency = currency       # Mena v ktorej nastal výdaj
        self.name = name               # Názov výdaju
        self.amount = amount           # Hodnota výdaju
        self.category = category       # Kategória výdaju
        self.reciever = reciever       # Príjemca výdaju
        self.account = account         # Názov účtu, z ktorého bol zaznamenaný výdaj

    def __repr__(self): # Reprezentácia celkového záznamu výdaju vo forme dátového typu string (inak adresa pamäťe!)
        return f"Výdaj: {self.date}, {self.currency}, {self.amount:.2f}, {self.name}, {self.category}, {self.reciever}, {self.account}"
