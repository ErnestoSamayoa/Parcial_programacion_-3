#3. Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números pares en la lista. 

print("\n******Bienvenido Usuario*****")
Lista = input("Ingrese una lista de numeros separados por espacios: ").split()
Lista = [int(num) for num in Lista]

suma_pares = sum(num for num in Lista if num % 2 == 0)

print("La suma de los numeros pares es:", suma_pares)

print("\n******************************")

