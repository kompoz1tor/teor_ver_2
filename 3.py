'''
Монету подбросили 144 раза. 
Какова вероятность, что орел выпадет ровно 70 раз?
'''

from math import factorial
# Формула Бернулли
def bernulli(n, k, p):
    combination = factorial(n)/(factorial(k)*factorial(n-k)) #биноминальный коэффициент
    return combination*(p**k)*(1-p)**(n-k)
P4 = bernulli(144,70,0.5)*100

print(f'Вероятность того, что при 144-х кратном подбрасывании монетки орёл выпадет ровно 70 раз = {round(P4, 4)} %')