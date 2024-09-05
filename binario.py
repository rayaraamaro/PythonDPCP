from unicodedata import decimal
import unittest
import pilha
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError('pop from empty stack')

    def is_empty(self):
        return len(self.items) == 0

def decimal_para_binario(decimal: int) -> str:
    if decimal == 0:
        return '0'

    while decimal > 0:
        resto = decimal % 2
        pilha.push(resto)
        decimal = decimal // 2
    binario = " "
    while not pilha.is_empty():
        binario += str(pilha.pop())

    return binario.zfill(8)

print(decimal_para_binario(10))



