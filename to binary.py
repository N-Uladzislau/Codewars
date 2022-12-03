def to_binary3(n):
    return int(bin(n)[2:])
  
def to_binary1(n1):
    b = ""
    while n1 > 0:
        b = str(n1 % 2) + b
        n1 = n1 // 2
    return int(b) 
"""
Простое решение — использовать str.format() Функция, которая выполняет операцию форматирования строки.
Чтобы преобразовать целое число в его двоичное представление, вы можете использовать тип представления строки b.
"""
def to_binary2(n2):
    binary = f'{n2:b}'
    # old format binary = "{0:b}".format(n2)
    return int(binary)
  
