#Lista principal de empleados
empleados=[]

#=======================
#FUNCIONES DE VALIDACION
#=======================

def validar_nombre(nombre):
    return nombre.strip()  != ""

def validar_edad(edad):
    return edad >0

def validar_salario(salario):
    return salario>0

#==================
#FUNCIONES DEL MENU
#==================
def mostrar_menu():
    print("\n=======MENU PRINCIPAL=======")
    print("1.Agregar empleado")
    print("2.Buscar empleado")
    print("3.Eliminar empleado")
    print("4.Actualizar estado")
    print("5.Mostrar empleado")
    print("6.Salir")
    print("==============================")
    
def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion(1-6): "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("Deber ingresar una opcion entre 1 y 6")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido")

#=====================
#FUNIONES DE EMPLEADOS
#=====================

def agregar_empleado(lista):
    nombre=input("ingrese nombre: ")
    
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacio")
        return
    
    try:
        edad=int(input("Ingrese edad: "))
        if not validar_edad(edad):
            print("Error: La edad debe ser mayor que cero")
            return
    except ValueError:
        print("Error: La edad debe ser un numero entero")
        return
    
    try:
        salario=float(input("ingrese salario: "))
        if not validar_salario(salario):
            print("Error: Debe ingresar un salario mayor que cero")
            return
    except ValueError:
        print("Error: El salario debe ser un numero decimal")
        
    empleado={"nombre":nombre,
              "edad":edad,
              "salario": salario,
              "activo": False}
    
    lista.append(empleado)
    print("Empleado registrado correctamente")
    
def buscar_empleado(lista,nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"]==nombre:
            return i
    return  -1

def eliminar_empleado(lista):
    nombre=input("Ingrese nombre a eliminar: ")
    
    pocision= buscar_empleado(lista,nombre)
    
    if pocision != -1:
        lista.pop(pocision)
        print("Empleado elimado correctamente")
    else:
        print(f"El empleado {nombre} no se encuentra registrado")
        
            
def actualizar_estado(lista):
    for empleado in lista:
        if empleado["edad"]>=18:
            empleado["activo"]=True
        else:
            empleado["activo"]=False
    
    print("Estado Actualizado correctamente")

def mostrar_empleados(lista):
    actualizar_estado(lista)
    
    if len(lista)==0:
        print("No existen empleados registrados") 
        return
    
    print("\n==LISTA DE EMPLEADOS===")
    
    for empleado in lista:
        
        estado="ACTIVO" if empleado["activo"] else "INACTIVO"
        
        print(f"Nombre: {empleado["nombre"]}")
        print(f"Edad: {empleado["edad"]}")
        print(f"Salario: {empleado["salario"]}")
        print(f"Estado: {estado}")
        print("=====================")  
        

#==================
#PROGRAMA PRINCIPAL
#==================

while True:
    mostrar_menu()
    opcion=leer_opcion()
    
    if opcion==1:
        agregar_empleado(empleados)
    
    elif opcion==2:
        nombre=input("Ingrese nombre a buscar: ")
        
        posicion=buscar_empleado(empleados,nombre)
        
        if posicion != -1:
            emp=empleados[posicion]
            
            print("\nEmpleado Encontrado")
            print("Posicion: ", posicion)
            print("Nombre: ",emp["nombre"]) 
            print("Edad: ",emp["edad"])
            print("Salario: ",emp["salario"])
            print("Activo: ",emp["activo"])
        
        else:
            print("Empleado no encontrado")
    
    elif opcion==3:
        eliminar_empleado(empleados)
    
    elif opcion==4:
        actualizar_estado(empleados)
    
    elif opcion==5:
        mostrar_empleados(empleados)
    
    elif opcion==6:
        print("Gracias por usar el sistema, vuelva pronto")
        break
    
    else: 
        print("ingrese una opcion valida")                   
            
   
    
            
        
                            
    
