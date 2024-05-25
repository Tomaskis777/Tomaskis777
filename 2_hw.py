a = 2
print(a, "относится к типу", type(a))

b = 35.53
print(b, "относится к типу", type(b))


g = 'Сторона'
print (g + '\n')


test_list = ['один', 'два', 'три', 'четыре', 'пять']
for elem in test_list:
  print(elem)


print(15 > 8)
print(12 == 3)
print(4 < 2)

b = False
if a:
    print('a = True')
else:
    print("a != True")


a: int = 6
b: str = 'строчка'
с: list = [1, 2]

def indent(s: str, width: int) -> str:
    return  " " * (max(0, width - len(s))) + s

print(indent('69', 13))
