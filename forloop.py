# for i in range(0, 5):
#     for j in range(0, 5):
#         print('*', end=' ')
#     print()
#
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         print('*', end=' ')
#     print()

# i = 0
# while i < 5:
#     i += 1
#     for j in range(3):
#         print(j)
#         if j == 2:
#             break
#     for k in range(3):
#         if k == 2:
#             continue
#         print(k)
#     if i > 3:
#         break
#     print(i)

for i in range(1, 5):
    for j in range(1, 5):
        if j == i:
            continue
        for k in range(1, 5):
            if k == j or k == i:
                continue
            else:
                print(str(i)+str(j)+str(k))
