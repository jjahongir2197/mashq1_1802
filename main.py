class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, dish, qty):
        self.items.append((dish, qty))

    def total(self):
        return sum(d.price * q for d, q in self.items)

    def show(self):
        print("\n--- Buyurtma ---")
        for d, q in self.items:
            print(d.name, "x", q, "=", d.price * q)
        print("Jami:", self.total())

class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish(self, name, price):
        self.menu.append(Dish(name, price))

    def show_menu(self):
        for i, d in enumerate(self.menu):
            print(f"{i+1}. {d.name} - {d.price} so‘m")

def run():
    r = Restaurant()
    r.add_dish("Osh", 25000)
    r.add_dish("Lag‘mon", 30000)
    r.add_dish("Shashlik", 18000)

    order = Order()

    while True:
        print("\n1. Menyu\n2. Buyurtma\n3. Chek\n4. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            r.show_menu()
        elif c == "2":
            r.show_menu()
            i = int(input("Tanlang: ")) - 1
            q = int(input("Soni: "))
            order.add_item(r.menu[i], q)
        elif c == "3":
            order.show()
        elif c == "4":
            break

run()
