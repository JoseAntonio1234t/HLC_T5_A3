def vowels_and_consonants(input):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    count_consonants = 0
    
    for word in input:
        if word in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    
    return "Contador de consonantes: ", count_consonants, "Contador de vocales: ", count_vowels

input = "hola"
print(vowels_and_consonants(input))

    