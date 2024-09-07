import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

print(orders)
print(type(orders))

#1.Какой номер самого дорого заказа за июль?
#2.Какой номер заказа с самым большим количеством товаров?
#3.В какой день в июле было сделано больше всего заказов?
#4.Какой пользователь сделал самое большое количество заказов за июль?
#5.У какого пользователя самая большая суммарная стоимость заказов за июль?
#6.Какая средняя стоимость заказа была в июле?
#7.Какая средняя стоимость товаров в июле?

#1.Какой номер самого дорого заказа за июль?
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2.Какой номер заказа с самым большим количеством товаров?
m_quantity = 0
m_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем количество товаров
    quantity = orders_data['quantity']
    #если товар с самым большим количеством заказов - запоминаем номер и количество заказов
    if quantity > m_quantity:
        m_order = order_num
        m_quantity = quantity
print(f'Номер заказа: {m_order}, с самым большим количеством товаров: {m_quantity}')

#3.В какой день в июле было сделано больше всего заказов?
date_dict = {}
for order_num, orders_data in orders.items():
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1
for date in sorted(date_dict):
    m_value = max(date_dict.values())
    if date_dict[date] == m_value:
        print(f'3.Больше всего заказов в июле сделано: {date}, количество заказов: {date_dict[date]}')

#4.Какой пользователь сделал самое большое количество заказов за июль?
s_quantity = 0
p_id = 0
p_order = 0
s_user_id = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    s_user_id[user_id] = s_user_id.get(user_id, 0) + 1
    order_id = s_user_id.get(user_id)
    if order_id > p_order:
        p_order = order_id
print(f'Id пользователя, который сделал больше всего заказов за июль: {user_id}, количество заказов: {p_order}')

#5.У какого пользователя самая большая суммарная стоимость заказов за июль?
k_orders = 0
k_id = 0
user = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    user[user_id] = user.get(user_id, 0) + price
    orders_id = user.get(user_id)
    if order_id >= k_orders:
        k_orders = order_id
        k_id = user_id
print(f'Id пользователя: {k_id}, у которого самая большая суммарная стоимость заказов: {k_orders}')

#6.Какая средняя стоимость заказа была в июле?
sum_price = 0
sum_zakazov = 0
price = 0
l_date = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    date = orders_data['date']
    l_date[date] = l_date.get(date, 0) + 1
    sum_price += price
for date in sorted(l_date):
    sum_zakazov += l_date[date]
print(f'Средняя стоимость заказов в июле: {sum_price/sum_zakazov} рублей')

#7.Какая средняя стоимость товаров в июле?
s_quantity = 0
sum_price = 0
price = 0
s_date = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    s_date[date] = s_date.get(date, 0) + 1
    sum_price += price
    s_quantity += quantity
print(f'Средняя стоимость товаров в июле: {sum_price/s_quantity:.5} рублей')