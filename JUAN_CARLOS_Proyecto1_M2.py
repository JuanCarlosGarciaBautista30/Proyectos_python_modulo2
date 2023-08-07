
print(" escrive una palabra,(devera tener minimo 4 caracteres maximo 8 caracteres)")

while True:
    # pedimos al usuario una palabra cualquiera.
    palabra=input(" escrive la palabra: ") 
   
    # es esta parte en donde validamos la palabra.
    if  len(palabra) >=4 and len(palabra) <=8:# si se cumple con esta función cumple los requisitos y se termina el programa 
        print("Palabra correcta")
        print(f"La palabra tiene {len(palabra)} caracteres")
        break # se rompe el bucle.
    
    # usamos len para saber cuantos digitos tiene la palabra.
    elif len(palabra) >=1 and len(palabra)<4:
        print(f"le hacen falta letras,la palabra solo tiene {len(palabra)} letras, min(4) max(8). inteta de nuevo.")
        continue # continua con otro ciclo 

    elif len(palabra) >8:
        print(f"la palabra rebasa el limite con {len(palabra)} letras, intenta otravez, min(4), max(8). ")
        continue # continua con otro ciclo
    
    # si se deja el campo vacio ejecuta el siguiente codigo.
    elif len(palabra)<=0 or palabra.isnumeric():
        print("""no puedes dejar el campo vacio.
              intenta de nuevo.""")
        continue # continuamos con otro ciclo

   

    


