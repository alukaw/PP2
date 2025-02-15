#Task1

def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input())
for square in square_generator(N):
    print(square, end=" ")


#Task2

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input())
print(" ".join(even_generator(n)))

#Task3

def div_by_3_and_4(z):
    for i in range(z + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

z = int(input())
for num in div_by_3_and_4(z):
    print(num, end=" ")

#Task4

def square(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = map(int, input().split())  
for sq in squares(a, b):
    print(sq)

#Task5

def countdpwn(p):
    for i in range(0, -1, -1):
        yield i

p = int(input())
for q in countdpwn(p):
    print(q, end=" ")
