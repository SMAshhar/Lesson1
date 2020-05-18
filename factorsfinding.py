def prime_check():
    a = 2
    c = []
    while a <= x:
        b = x % a
        if b == 0 and a != x:
            c.append(a)
            a += 1
        elif a == x:
            break
        else:
           a += 1
    if c == []:
        print(f"{x} is a prime number")
    else:
        c = []
        a = 2
        while a <= x:
            b = x % a
            if b == 0 and a != x:
                c.append(a)
                a += 1
            elif a == x:
                break
            else:
                a += 1
        print(c)
    
x = int(input("Please enter an integere greater then 1"))
prime_check()