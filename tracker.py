from expenses import Expense # Expense class zo súboru expense.py
# from forex_python.converter import CurrencyRates

def main():
    print(f"Vitajte v osobnom účtovníctve!")
    
    # Funkcia pre vytvorenie uživateľovho výdaju
    expense = get_user_input()
    
    # CSV súbor, do ktorého sa ukládajú záznamy výdajov
    file_path = "expenses.csv"
    
    # Funkcia pre uloženie výdaju do CSV súboru
    log_expense(expense, file_path)
    
    # Funckia pre čítanie CSV súboru, roztriedenie výdajov podľa kategórie a meny
    summarize(file_path)

# Vytvorenie funkcie pre záznam uživateľovho výdaju
def get_user_input():
    print("Nahrajte svoje výdaje!")

    # Dátum zaznamenaného výdaju
    expense_date = input("K akému dátumu náleží výdaj? (DD/MM/YY) ")

    # Zoznam použiteľných mien, nelogický prvok programu (iba zoznam)
    currency_expense = [
        "CZK - Česká Koruna", 
        "EUR - Euro", 
        "DOL - Americký Dollar", 
        "AED - UAE Dirham", 
        "AUD - Australský Dollar", 
        "BGN - Bulharský Lev",
        "CAD - Kanadský Dollar",
        "CHF - Švajčiarský Franc",
        "CLP - Čilské Peso",
        "COP - Kolumbíjske Peso",
        "DKK - Dánska Koruna",
        "EGP - Egyptská Libra"
        "GBP - Britská Libra",
        "HKD - Honk Kongský Dollar",
        "HUF - Maďarský Forint",
        "ILS - Israelský Nový Sheqel",
        "INR - Indická Rupia",
        "ISK - Islandská Koruna",
        "JPY - Japonský Yen",
        "KRW - Juho Kórejský Won",
        "KZT - Kazachstánska Tenga",
        "MAD - Marocký Dirham",
        "MXN - Mexické Peso",
        "NOK - Norksá Koruna",
        "NZD - Novo Zealandský Dollar",
        "PHP - Filipínske Peso",
        "PLN - Poľské Zlote",
        "QAR - Qatarský Riyal",
        "RON - Rumúnske Leu",
        "RSD - Srbský Dinár",
        "SAR - Saudsko Arabský Riyal",
        "SEK - Švédksa Koruna",
        "SGD - Singapúrský Dollar",
        "THB - Thaiský Baht",
        "TRY - Turecká Lira",
        "ZAR - Juhoafrický Rand",
    ]
    
    # Názov výdaju
    expense_name = input("Vložte názov vášho výdaju: ")
    
    # Výpis zoznamu mien
    print(*currency_expense,sep='\n')
    
    # Užívateľom zvolená mena
    currency_select = input("Vložte 3-miestny kód meny: ").upper()
    
    # Podmienka pre zadanie presne 3-miestneho kódu meny
    while len(currency_select) != 3:
        print("Zadali ste nesprávny formát meny!")
        currency_select = input("VLOŽTE 3-MIESTNY KÓD MENY: ").upper()
    
    # Hodnota výdaju
    expense_amount = float(input("Vložte cenu výdaju: "))
    
    # Zoznam použiteľných kategórií
    category_expense = [
        "Food", # Výdaje týkajúce sa jedla a nápojov (Potraviny/Reštaurácia)
        "Personal Items", # Produkty a služby pre osobnú potrebu (Oblečenie)
        "Transportation", # Výdaje týkajúce sa prepravy (Autobus, Vlak, Lietadlo)
        "Entertainment", # Výdaje týkajúce sa zábavy (Kino, Bar, ...)
        "Portfolio", # Výdaje týkajúce sa investovania (Komodity, Akcie, Dlhopisy, Krypto)
        "Work", # Pracovné výdaje
        "Household", # Výdaje týkajúce sa domácnosti (Nájom, Energie, Internet)
        "Fees", # Výdaje vo forme poplatkov
        "Other", # Iný druh výdajov
    ]

    #Príjemca výdaju
    expense_reciever = input("Zadajte meno/názov príjmateľa vášho výdaju: ") 
    
    # Názov účtu, z ktorého bol zaznamenaný výdaj
    expense_account = input("Zadajte názov účtu, z ktorého ste vykonali výdaj (Cash, KB, Reiffeisen, ČSOB, ...): ")
    
    # Výber kategórie pomocou indexu zoznamu
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(category_expense):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(category_expense)}]"
        index_select = int(input(f"Vložte INDEX kategórie výdaju {value_range}: ")) - 1
        
        # Vloženie nenumerických znakov pri voľbe kategórie zhodí program!
        
        if index_select in range(len(category_expense)):
            category_select = category_expense[index_select]
            # Expense class zo súboru expense.py
            new_expense = Expense(
                date=expense_date, currency=currency_select, amount=expense_amount, name=expense_name, category=category_select, reciever=expense_reciever, account=expense_account
                ) 
            return new_expense
        else:
            print("Vybrali ste neexistujúcu kategóriu. Vložte INDEX kategórie výdaju:")

# Vytvorenie funkcie pre uloženie výdaju do CSV súboru
def log_expense(expense: Expense, file_path):
    print(f"Záznam výdaju: {expense} bol uložený do {file_path}")
    # Zápis do CSV súboru, ďalší záznam bude "a" (append)
    with open(file_path, "a") as f:
        f.write(
            f"{expense.date},{expense.currency},{expense.amount},{expense.name},{expense.category},{expense.reciever},{expense.account}\n"
            )

# Vytvorenie funckie pre čítanie CSV súboru, roztriedenie výdajov podľa kategórie a meny
def summarize(file_path):
    print("") # Prázdny riadok
    print("Prehľad vaších výdajov: ")
    vydaje: list[Expense] = []
    with open(file_path, "r") as f:
        # Zoznam stringov, kde každý záznam reprezentuje jeden riadok v CSV súbore
        lines = f.readlines() 
        for line in lines:
            expense_date, expense_currency, expense_amount, expense_name, expense_category, expense_reciever, expense_account = line.strip().split(",")
            print(expense_date, expense_currency, expense_amount, expense_name, expense_category, expense_reciever, expense_account)
            lined_expense = Expense(
                date = expense_date,
                currency = expense_currency,
                amount = float(expense_amount),
                name = expense_name,
                category = expense_category,
                reciever = expense_reciever,
                account = expense_account,
            )
            vydaje.append(lined_expense)

    # Výpis výdajov podľa kategórie
    amount_by_category = {}
    for expense in vydaje:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("") # Prázdny riadok
    print("Výdaje podľa kategórie: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: {amount:.2f}")
    print("") # Prázdny riadok
    total_spent = sum([x.amount for x in vydaje])
    
    # Výpis výdajov podľa meny
    amount_by_currency = {}
    for expense in vydaje:
        key = expense.currency
        if key in amount_by_currency:
            amount_by_currency[key] += expense.amount
        else:
            amount_by_currency[key] = expense.amount
    print("") # Prázdny riadok
    print("Výdaje podľa meny: ")
    for key, amount in amount_by_currency.items():
        print(f"  {key}: {amount:.2f}")
    print("") # Prázdny riadok
    total_spent = sum([x.amount for x in vydaje])

if __name__ == "__main__": # Comment! 9'33"
    main()