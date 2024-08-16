# import locale
import os
import time


def get_int(value: str) -> int:
    try:
        conv = int(value)
    except:
        return -1
    else:
        return conv


def get_float(value: str) -> float:
    try:
        conv = float(value)
    except:
        raise InvalidAmount()
    else:
        return conv


def confirm():
    print('\nPressione <enter> para continuar')
    input('')


class InsufficientFunds(Exception):
    def __init__(self):
        self.message = 'Saldo insuficiente'


class InvalidAmount(Exception):
    def __init__(self):
        self.message = 'Valor invalido'


class Bank:
    __balance: float

    def __init__(self):
        self.__balance = 0.0

    def show_balance(self):
        # locale.setlocale(locale.LC_ALL, 'pt_BR')
        # print(locale.currency(self.__balance, grouping=True, symbol=True))
        print('Saldo atual: R$ {:,.2f}'.format(self.__balance).replace('.', '#').replace(',', '.').replace('#', ','))

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise InsufficientFunds()
        self.__balance -= amount
        print('Saque realizado com sucesso!')

    def deposit(self, amount: float):
        self.__balance += amount
        print('Deposito realizado com sucesso!')


if __name__ == '__main__':
    my_bank = Bank()

    while True:
        try:
            os.system('clear')
            print()
            print('1 - Consultar saldo')
            print('2 - Sacar')
            print('3 - Depositar')
            print('0 - Sair')
            print()
            op = input('Opcao: ')
            op = get_int(op)
            print()

            if op == 1:
                my_bank.show_balance()
            elif op == 2:
                amount = input('Valor: ')
                amount = get_float(amount)
                my_bank.withdraw(amount=amount)
            elif op == 3:
                amount = input('Valor: ')
                amount = get_float(amount)
                my_bank.deposit(amount=amount)
            elif op == 0:
                break
            else:
                print('opcao invalida')
                time.sleep(1.5)
                continue

            confirm()
        except InsufficientFunds as e:
            print(e.message)
            confirm()
        except InvalidAmount as e:
            print(e.message)
            confirm()
