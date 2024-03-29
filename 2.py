'''
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
'''
# Функция exp () принимает целое число или число с плавающей точкой, а возвращает e в соответствующей степени
from math import factorial, exp
# Формула Пуасона
def poisson_distr(m,p,n):
    lamb=p*n
    return exp(-lamb)*(lamb**m)/factorial(m)

P2 = round(poisson_distr(0,0.0004,5000), 2)
print(f'Вероятность того, что ни одна из ламп не перегорит в первый день = {P2} %')

P3 = round(poisson_distr(2,0.0004,5000), 2)
print(f'Вероятность того, что 2 лампы перегорят в первый день = {P3} %')