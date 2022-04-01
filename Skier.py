P = float(input("Введите P: "))/100
A = 10.0
run = A
day = 0
while run <= 200:
   A*=1+P
   run+=A
   day+=1
print("Пробежал = ", run)
print("Дней = ", day)
input()
