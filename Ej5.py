def contarvalores(text):
    words = text.split()
    dictionary = {}
    
    for word in words:
        
        if word in dictionary:
            
            dictionary[word] +=1
            
        else:
            
            dictionary[word] = 1
    
    return dictionary


entrada = "hola mundo hola"
resultado = contarvalores(entrada)
print(resultado)
    
    
    

    