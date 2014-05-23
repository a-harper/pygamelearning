__author__ = 'DarkFlare'
# for j in range(10):
#     for x in range(j):
#         print(" ", end=" ")
#     for i in range(10-j):
#         print(i, end=" ")
#     print()


# for row in range(1, 10):
#     for column in range(1, 10):
#         if row * column < 10:
#             print(" ", end="")
#         print(str(row * column), end=" ")
#     print()

for row in range(1, 10):
    for column in range(row):
        print(str(column + 1), end=" ")
    print()