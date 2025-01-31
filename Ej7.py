def divisors():
    
    my_list = []
    
    value=int(input("Introduce un valor:"))
    
    for i in range(2, value + 1):
        
        if value % i == 0:
    
            my_list.append(i)
            
            print("Divisores:", divisors())
            
    return  my_list

divisors()
    
    