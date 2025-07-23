class Atm:
   def __init__(self,pin) : 
       # Constructor
         self.__pin = pin #privated
         self._balance = 1000 #protected
   
   def deposit(self, amount):
        self.__balance += amount
        print("Depósito exitoso. Saldo actual:", self.__balance)

   def withdraw(self, amount):
        if amount > self.__balance:
            print("Saldo insuficiente.")
        else:
            self.__balance -= amount
            print("Retiro realizado correctamente. Nuevo saldo:", self.__balance)
       
   def show_balance(self):
         print("Tu saldo actual es:" + self.__balance)

   def change_pin(self,new_pin):
      if self._pin != new_pin:
         self.__set_pin(self,new_pin)
         print("Pin modificado correctamente")
      else:
          print("Estas usando el mismo pin ")      

   def __set_pin(self,new_pin): #private
       self._pin = new_pin

pin = input("Enter your pin : ")
bank = Atm(pin)

user_input= input(
   """ ¿Que proceso desea realizar?
       1.Ingresa 1 para cambiar pin
       2.Ingresa 2 para depositar
       3.Ingresa 3 para retirar
       4.Ingresa 4 para Consultar saldo
       5.Ingresa 5 para salir 
       """)

if user_input=="1":
   pin = int(input("Ingresa tu pin: "))
   bank.change_pin(pin)
elif user_input=="2":
   amount=int(input("Ingresa la cantidad: "))
   bank.deposit(amount)
elif user_input=="3":
   amount = int(input("Ingresa la cantidad: "))
   bank.withdraw(amount)
elif user_input=="4":
   bank.check_balance() 
else:
   print("Gracias por usar el servicio")      