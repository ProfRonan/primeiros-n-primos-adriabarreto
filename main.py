n = int(input("Digite um número: "))
if n >= 1:
    print("2")
    p = 1
    y = 3
    while p < n:
        x = 3
        while(x < y):
            if y % x == 0:
                break
            x = x + 2
        if x == y:
            print(x)
            p = p + 1
        y = y + 2