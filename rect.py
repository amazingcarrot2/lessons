def rect(height = 5, width = 5, sign = '*'):
    for i in range(0,height):
        for j in range(0,width):
            print(sign, end = ' ')
        print()

rect()
rect(4,3)
rect(2,6,'!')
