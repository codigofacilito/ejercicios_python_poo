class Atm:
  def __init__(self,pin):
    self.__pin = pin #private
    self._balance = 1000 #protect

  def deposit(self, amount):
      self._balance += amount
      print("Deposito exitoso. Saldo actual: ", self._balance)

  def withdraw(self,amount):
     if amount <self._balance:
        self._balance -= amount
        print("Retiro realizado correctamente: ",self._balance)
     else: 
        print("Saldo insuficiente.")   

  def show_balance(self):
     print("Tu saldo actual es: ",self._balance)

  def change_pin(self,new_pin):
     if self.__pin != new_pin:
        self.__set_pin(new_pin)
        print("Pin modificado correctamente")
     else:
        print("Estas usando el mismo pin")
           
  def __set_pin(self,new_pin): #private
     self.__pin = new_pin                         


#Ejecutar en main.py
'''
from atm import Atm

pin = input("Ingresa tu pin: ")
atm = Atm(pin)

user_input = input(
  """ ¿ Que proceso desea realizar?
  1. Ingresa 1 para cambiar el pin
  2. Ingresa 2 para depositar
  3. Ingresa 3 para retirar
  4. Ingresa 4 para consultar tu saldo
"""
)
if user_input == "1":
  new_pin = int(input("Ingresa el nuevo pin: "))
  atm.change_pin(new_pin)
elif user_input == "2":
  amount = int(input("Ingresa la cantidad a depositar: "))
  atm.deposit(amount)
elif user_input == "3":
    amount = int(input("Ingresa la cantidad: "))    
    atm.withdraw(amount)
elif user_input == "4":
   atm.show_balance()
else:
   print("Gracias por usar el servicio") 
'''     