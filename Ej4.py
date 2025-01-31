def sume_average():
    numbers = [5,10,15,20,25]
    sume = 0

    for i in numbers:
        sume += i 
    print("La suma es: ", sume)
    print("El promedio es: ", sume/len(numbers))
sume_average()