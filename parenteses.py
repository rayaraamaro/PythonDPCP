import unittest

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

def verificar_parenteses_balanceados(expressao: str) -> bool:
    pilha = Stack()

    for char in expressao:
        if char == "(":
            pilha.push(char)
        elif char == ")":
            if pilha.is_empty():
                return False
            pilha.pop()
    return pilha.is_empty()

class TestVerificarParentesesBalanceados(unittest.TestCase):
    def test_balanceado_simples(self):
        self.assertTrue(verificar_parenteses_balanceados("(a + b) * (c + d)"))
    def test_desbalanceado_faltando_fechamento(self):
        self.assertFalse(verificar_parenteses_balanceados("((a + b) * c"))
    def test_balanceado_complexo(self):
        self.assertTrue(verificar_parenteses_balanceados("((a + b) * (c + d))"))
    def test_desbalanceado_fechamento_excedente(self):
        self.assertFalse(verificar_parenteses_balanceados("a + b) * (c + d)"))
    def test_vazio(self):
     self.assertTrue(verificar_parenteses_balanceados(""))

if __name__ == '__main__':
    unittest.main()