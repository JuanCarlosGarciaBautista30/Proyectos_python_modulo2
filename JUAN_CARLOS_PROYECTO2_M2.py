# Crear un programa que en base a 2 números de entrada, coordenadas, 
# identifique en cuál de los 4 cuadrantes se encuentra el punto. 
# El programa debe verificar que ninguna coordenada sea 0. Por ejemplo.

print("\nCUADRO CARTECIANO\n") # nombre de la app

 # preguntamos al usuario su nombre, y la primer letra se mostrara en mayuscula.
nombre=input("Hola! ¿Cuál es tu nombre? ").capitalize()

lista_vacia=[] # se declara lista vacia donde se introduciran los datos introducidos del usuario.
cuadrante=["1° cuadrante","2° cuadrante","3° cuadrante","4° cuadrante"] # creamos una lista con los nombres de cuadrantes.

print("\n"+nombre + """ elige dos coordenadas 
que sean números enteros positivos o negativos\n""")

# recordatorio
print("""Recuerda que el eje de la (x) es la linea orizontal(absisas) 
y el eje de la (y) es el eje vertical (ordenadas), y esta dividivo en cuatro cuadrantes\n""")

# si el usuario introduce un valor no valido, el programa lanzara la excepción y preguntara nuevamente.
# de lo contrario, se ejecuta el bloque try, y con break rompemos ciclo y continuamos con la ejecución del programa.    

# metemos el codigo en un bucle while True para iterar las preguntas si el usuario introduce algo incorrecto.
while True:
    # si no se produce una excepción se ejecuta el bloque try.
    try:
        # pedimos al usuario las coordenadas.
        cor_x=int(input("elige una coordenada (x): "))
        cor_y=int(input("elige una coordenada (y): "))
        
        # hacemos validaciones para saber en que cuadrate podrian estar nuestras coordenadas. 
        # en cualquiera de las validaciones (if elif) con las que cumplan los requisitos
        # los valores de las variables se guardaran en lista_vacia.

        if cor_x >0 and cor_x!=0 and cor_y >0 and cor_y !=0: 
            lista_vacia.append([cor_x,cor_y])
            
            print(f"{nombre} las coordenadas {lista_vacia} estan en el {cuadrante[0]}")
            break
        
        elif cor_x <0 and cor_x!=0 and cor_y >0 and cor_y !=0: 
            lista_vacia.append([cor_x,cor_y])

            print(f"{nombre} las coordenadas {lista_vacia} estan en el {cuadrante[1]}")
            break
        
        elif cor_x <0 and cor_x!=0 and cor_y <0 and cor_y !=0:
            lista_vacia.append([cor_x,cor_y])

            print(f"{nombre} las coordenadas {lista_vacia} estan en el {cuadrante[2]}")
            break

        elif cor_x >0 and cor_x!=0 and cor_y <0 and cor_y !=0:
            lista_vacia.append([cor_x,cor_y])

            print(f"{nombre} las coordenadas {lista_vacia} estan en el {cuadrante[3]}")
            break
        
        else: # si introducimos un cero se ejecuta ésta parte
            print("el (0) es invalido, vuelve a intentar.")
            # hacemos una linea divisoria
            print("_______________________________________________________________________________________")
            continue # entonses continuamos con un nuevo ciclo.
  
   # si se produce una excepción se ejecuta éste bloque
    except ValueError:
        print("no letras,símbolos, ni campos vacios. intenta de nuevo")
        continue