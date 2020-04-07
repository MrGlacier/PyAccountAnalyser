# https://docs.python.org/3/library/datetime.html
# The datetime module supplies classes for manipulating dates and times.
from datetime import date

class AccountEntry:
    typeOfEntry = None
    date = date.today()
    ammount = 0
    toAccount = None
    toIban = None
    description = None

    def __init__(self, type_of_entry, date, ammount, to_account, to_iban, description):
        self.typeOfEntry = type_of_entry
        self.date = date
        self.ammount = ammount
        self.toAccount = to_account
        self.toIban = to_iban
        self.description = description

    @classmethod
    def fromList(self, account_entry_object):
        self.typeOfEntry = account_entry_object[0]
        self.date = account_entry_object[1]
        self.ammount = account_entry_object[2]
        self.toAccount = account_entry_object[3]
        self.toIban = account_entry_object[4]
        self.description = account_entry_object[5]
        return self

    def get(self):
        print("Typ: {}\nDatum: {}\n,Betrag: {}\nÜberwiesen an: {}\nIBAN: {}\nBeschreibung: {}").format(self.typeOfEntry, self.date, self.ammount, self.toAccount, self.toIban, self.description)