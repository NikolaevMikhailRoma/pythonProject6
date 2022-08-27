"""
my pokupki
"""
import os

orders = []

if 'sum.txt' not in os.listdir():
    with open('sum.txt', 'w') as f:
        f.write('0')
with open("sum.txt", 'r') as f:
    sum = float(f.read())

if 'orders.txt' not in os.listdir():
    with open("orders.txt", 'w') as f:
        f.write('')
if 'orders.txt' in os.listdir():
    with open("orders.txt", 'r') as f:
        for order in f:
            orders.append(order.replace('\n', ''))

while True:

    print('1. Add order')
    print('2. Order history')
    print('3. Exit')
    print('66 delete history')
    choise = input("Write number: ")
    if choise == '1':
        name = input('Write Order name: ')
        orders.append(name)
        price = input('Write Order price: ')

        sum += float(price)
        pass
    elif choise == '2':
        print(orders)
        pass
    elif choise == '3':
        with open ('orders.txt', 'w') as f:
            for order in orders:
                f.write(order+'\n')
        f = open("sum.txt", 'w')
        f.write(str(sum))
        f.close()
        break
    elif choise == '66':
        f = open("models.txt", 'w')
        f.close()
        f = open("sum.txt", 'w')
        f.write('0.0')
        f.close()
    else:
        print('Wrong number')