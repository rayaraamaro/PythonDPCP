class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue_front(self, item):
        self.items.insert(0, item)

    def enqueue_rear(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if not self.is_empty():
            return self.items.pop(0)

        else:
            raise IndexError("Deque is empty")

    def dequeue_rear(self):
        if not self.is_empty():
            return self.items.pop()

        else:
            raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]

        else:
        raise IndexError("Deque is empty")

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]

        else:
            raise IndexError("Deque is empty")

class Atendimento:

    def __init__(self):
        self.fila_padrao = Deque()
        self.fila_prioritaria = Deque()

    def enfileirar_elemento(self, pessoa):

    def ajustar_filas(self):
        class TestAtendimento(unittest.TestCase):
            def setUp(self):

                self.atendimento = Atendimento()

        def test_enfileirar_varias_pessoas(self):
            pessoas = [
                {'nome': 'João', 'idade': 30},
                {'nome': 'Maria', 'idade': 70},
                {'nome': 'Ana', 'idade': 65},
                {'nome': 'Carlos', 'idade': 80}
            ]

        for pessoa in pessoas:
            self.atendimento.enfileirar_elemento(pessoa)
        self.assertEqual(self.atendimento.fila_padrao.size(), 2)
        self.assertEqual(self.atendimento.fila_prioritaria.size(), 2)
        self.assertEqual(self.atendimento.fila_padrao.peek_front(), pessoas[0])
        self.assertEqual(self.atendimento.fila_prioritaria.peek_front(), pessoas[1])
        self.assertEqual(self.atendimento.fila_prioritaria.peek_rear(), pessoas[3])