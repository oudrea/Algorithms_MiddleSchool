if __name__ == '__main__':
    G = input("Enter a value for G:")
    Y = input("Enter a value for Y:")
    D = input("Enter a value for D:")
    if G > Y: 
        if G > D:
            print (G)
            # YES
        else: print (D) 
            # NO
        # YES is here
    else: 
        if Y > D:
            print (Y)
        else: print (D)    
        # NO is here
