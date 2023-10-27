# task 1
# def generate_squares(N):
#     for i in range (N):
#         yield i ** 2
# N = int(input())
# squares_generator = generate_squares(N)
# for square in squares_generator:
#     print(square)

# task 2
# def generate_squares(N):
#     for i in range (N):
#        if i%2!=0:
#            yield i
# N = int(input())
# squares_generator = generate_squares(N)
# for square in squares_generator:
#     print(square)

# task 3
# def divisible_by_3_and_4(n):
#     for num in range(n):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num
# n=int(input())
# for num in divisible_by_3_and_4(n):
#     print(num)

# task 4
# def generate_squares(a,b):
#     for i in range (a,b):
#         yield i ** 2
# a = int(input())
# b = int(input())
# squares_generator = generate_squares(a,b)
# for square in squares_generator:
#     print(square)

# task 5
# def numbers(N):
#     while N >= 0:
#         yield N
#         N -= 1
# N = int(input())
# for num in numbers(N):
#     print(num)

