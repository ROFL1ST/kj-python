import random
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Account:
    def __init__(self, bank_number, balance):
        self.bank_number = bank_number
        self.balance = balance


class BankAccount(User, Account):
    def __init__(self, name, age, bank_number, balance):
        # Inheritance/pewarisan
        User.__init__(self, name, age)
        Account.__init__(self, bank_number, balance)

    def print_info(self):
        print(f"Nama : {self.name}")
        print(f"Umur : {self.age}")
        print(f"Nomor akun : {self.bank_number}")
        print(f"Balance : {self.balance}")


class EncapsulationBank:
    def __init__(self, name, age, bank_number, balance):
        self._name = name #memproteksi attribute
        self.__age = age #memprivasi attribute
        self._bank_number = bank_number #memproteksi attribute
        self.__balance = balance #memprivasi attribute

    def getName(self):    #untuk mereturn nama
        return self._name

    def getAge(self):     #untuk mereturn umur
        return self.__age
    def getAccountId(self):     #untuk mereturn umur
        return self._bank_number
    def getBalance(self):     #untuk mereturn umur
        return self.__balance

    def setBalance(self, new_balance):  #memasukkan balance baru kedalam akun
        if new_balance >= 0:
            self.__balance = new_balance

        else:
            print("Invalid balance")
        
def deposit(account, amount):   #memperbarui variable balance di dalam akun bank
    current_balance = account.getBalance()
    new_balance = current_balance + amount
    account.setBalance(new_balance)
    print(f"Deposit {amount}.\nNew Balance : {new_balance}")

def withdraw(account, amount):  # menarik balance dari akun
    current_balance = account.getBalance()
    if amount <= current_balance:
        new_balance = current_balance - amount
        account.setBalance(new_balance)
        print(f"Your withdraw balance {amount}.\nYour current balance : {new_balance}")
    else:
        print("Your balance is Insufficient")

# contoh penggunaan program nya





input_name = input("Masukkan nama anda : ")
input_age = int(input("Masukkan umur anda : "))
input_balance = int(input("Masukkan saldo pertama anda : "))

bank_number = random.randrange(10000, 100000)
account = EncapsulationBank(input_name, input_age, bank_number, input_balance)

print(f"Nama : {account.getName()}")
print(f"Umur : {account.getAge()}")
print(f"Bank Number : {account.getAccountId()}")
print(f"Your Current Balance : {account.getBalance()}")

# mengambil balance dari akun
input_amount = int(input("Masukkan jumlah yang ingin ambil : "))
withdraw(account, input_amount)



# menambahkan saldo kedalam akun
input_newBalance = int(input("Masukkan saldo anda : "))
deposit(account, input_newBalance)



    


