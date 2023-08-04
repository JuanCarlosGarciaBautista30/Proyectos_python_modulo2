
print(" escrive un apalabra(devera tener minimo 4 caracteres maximo 8)")

while True:
    palabra=input(" escrive la palabra: ").capitalize() #pedimos al usuario una palabra 
   

    if  len(palabra) >=4 and len(palabra) <=8:
        print("Palabra correcta")
        print(f"La palabra tiene {len(palabra)} letras")
        break

    elif len(palabra) >=1 and len(palabra)<4:
        print(f"le hacen falta letras,la palabra solo tiene {len(palabra)} letras, min(4) max(8). inteta de nuevo.")
        continue

    elif len(palabra) >8:
        print(f"la palabra rebasa el limite con {len(palabra)} letras, intenta otravez, min(4), max(8). ")
        continue
    
    elif len(palabra)<=0 or palabra.isnumeric():
        print("""no puedes dejar el campo vacio.
              intenta de nuevo.""")
        continue

    else:
       
        break


    


