# models.py
# Classes for our factory entities

class Product:
    def __init__(self, p_id, name, stock, price):
        self.p_id = p_id
        self.name = name
        self.stock = stock
        self.price = price

    def display_info(self):
        print(f"  [ID: {self.p_id}] {self.name} | Available Stock: {self.stock} | Price: rs {self.price}")


class Machine:
    def __init__(self, m_id, name, is_working=True):
        self.m_id = m_id
        self.name = name
        self.is_working = is_working
