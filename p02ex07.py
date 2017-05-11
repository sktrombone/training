for i in range(1,81):
    print(i)
    for j in range(1,i+1):
        for k in range(1,i-j+2):
            print("*",end="")
        print()
    
