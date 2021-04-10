n = 24
for y in range(10, n + 1):
    if y > 1:
        for i in range(2,y):
            if (y % i) == 0:
                print(y, "bukan bilangan prima")
                break
        else:
            print(y, "adalah bilangan prima")