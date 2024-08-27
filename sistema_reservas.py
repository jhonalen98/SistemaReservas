UsuariosRegistrados=[]
Reservas=[]

def mostrar_menu():
    print("Bienvenido Sistema de Reservas")
    print("1. Registrar Usuario")
    print("2. Reservar un Viaje")
    print("3. Ver Reservas")
    print("4. Cancelar una Reserva")
    print("5. Salir del programa")

def registrar_usuario():
    registro=input("Ingrese el nombre del nuevo usuario: ")
    UsuariosRegistrados.append(registro)

def reservar_viaje():
    usuario=input("Ingrese el nombre de usuario: ")
    destino=input("Ingrese el destino: ")
    fecha=input("Ingrese la fecha: ")
    reserva={'usuario':usuario, 'destino':destino, 'fecha':fecha}
    Reservas.append(reserva)
    
    
def mostrar_reservas():
    resrva=input
    
    
    
def ejecutar():
    while True:
        mostrar_menu()
        opcion=input("Selecciona una opción: ")
        if opcion=="1":
            registrar_usuario()
        elif opcion=="2":
            reservar_viaje()
        elif opcion=="3":
            mostrar_reservas()
        elif opcion=="4":
            pagar()
        elif opcion =="5":
            print("Gracias por usar el Sistema de Reservas, ¡Hasta Luego!")
            break
        else:
            print("Opcion no válida, por favor vuelve a intentarlo.")
            
ejecutar()