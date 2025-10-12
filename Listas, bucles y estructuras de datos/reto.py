# Crea un programa que:
# Pida cuántos participantes hay.
# Pida el nombre y edad de cada uno.
# Guarde los datos en una lista de diccionarios.
# Al final, muestre los nombres de quienes sí pueden participar (edad ≥ 18).

personas = []

while True:
    nombre = input("Ingrese el nombre del participante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    
    persona = {"nombre": nombre, "edad": edad}
    
    personas.append(persona)
    
    # Mostramos toda la lista de personas
print("\nLista de personas registradas:")
for p in personas:
    print(f"Nombre: {p['nombre']}, Edad: {p['edad']}")
    
    # Mostrar quienes pueden participar (edad ≥ 18)
print("\nPersonas que pueden participar:")
for p in personas:
    if p["edad"] >= 18:
        print(p["nombre"])