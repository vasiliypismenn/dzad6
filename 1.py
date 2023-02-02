#**44. Напишите программу, которая принимает на вход
#  координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21


from functools import reduce
k_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
k_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(k_1, k_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (k_1[1] - dot[0])**2, zip(k_1, k2_2))))
     return round(rng, 2)
print(dot_range(k_1, k_2))