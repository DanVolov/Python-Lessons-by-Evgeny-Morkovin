class Product:
    def __init__(self,product_id,  name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price
        print(f'Цена товара {self.name} обновлена: {new_price} руб.')

    def update_quantity(self, new_quantity):
        if new_quantity <= self.quantity:
            self.quantity -= new_quantity
            return True
        return False

    def get_next_id(self):
        return self.product_id + 1

    def __str__(self):
        return f'{self.name} - {self.price} руб. (осталось: {self.quantity})'

class User:
    def __init__(self,user_id, first_name, last_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cart = []

    def add_product(self, product, quantity):
        if product.update_quantity(quantity):
            self.cart.append({
                'product': product,
                'quantity': quantity,
            })
            print(f'{quantity} шт. товара {product.name} добавлено в корзину')
        else:
            print(f'недостаточно товара {product.name} на складе')

    def get_cart_total(self):
        summa = 0
        for cart in self.cart:
            summa += cart['quantity'] * cart['product'].price

        return summa

class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.total = self.user.get_cart_total()
        self.status = "Обрабатывается"

    def process_order(self):
        self.status = "Обработан"
        print('Товары в заказе')
        for cart in self.user.cart:
            print(f'Товар: {cart["product"].name} Количество: {cart['quantity']}')
        print(f'Заказ {self.order_id} обработан. Сумма: {self.total}')




product_1 = Product(1, 'Phone1', 3333333,  10)
print(product_1)
product_1.update_price(44444)
product_1.update_quantity(10)
print(product_1)
product_1.quantity = 333333
product_2 = Product(product_1.get_next_id(), 'Phone2', 555,  10)
product_3 = Product(product_2.get_next_id(), 'Phone3', 77,  10)

user1 = User(1, 'Vasya', 'Vasya', 'admin@admin.ru')
user1.add_product(product_1, 10)
user1.add_product(product_2, 5)
user1.add_product(product_3, 4)
print(user1.get_cart_total())

order = Order(1, user1)
order.process_order()