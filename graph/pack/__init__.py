def test():
    n = 2
    x = 3
    y = 4
    
    n_increase = 0
    x_increase = 0
    y_increase = 0
    
    while n_increase < n : 
        while x_increase < x :
            while y_increase < y :
                print("%d "% n)
                y_increase +=1
            x_increase += 1
        n += 1
    print(n)
    
test()