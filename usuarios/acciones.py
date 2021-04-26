import usuarios.usuario as modelUser

import notas.acciones

class Acciones:
    
    ###############     saludo inicial    ###############
    def primetaAcciones(self):
        print("""
            Estas son las Acciones diaponibles:
            - registro(r)
            - login(l)
        """)
        
    ###############   acciones para registrar un usuario   ###############
    def registro(self):
        
        print("\nOk vamos a registrarte en el sistema...")
        nombre = input("Introduce tus Nombres: ")
        apellido = input("Introduce tus Apellidos: ")
        email = input("Introduce tu Email: ")
        password = input("Introduce tu Contraseña: ")
        
        usuario = modelUser.Usuario(nombre, apellido, email, password)
        
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} teas registrado correctamente con el email {registro[1].email}")
        else:
            print("\nNo te haz registrado correctamente...")
            
    ###############   selecionar proxima accion   ###############        
    def proximasAcciones(self, usuario):
            print("""
                acciones disponibles
                crear nota (c)
                mostrar nota (m)
                eliminar nota (e)
                salir (s)
            """)
            
            accion = input("que deseas hacer? ")
            
            hazEl = notas.acciones.Acciones()
            
            if accion == "c":
                hazEl.crear(usuario)
                self.proximasAcciones(usuario)
                
            elif accion == "m":
                print("bamos a mostrar una nota")
                self.proximasAcciones(usuario)
                
            elif accion == "e":
                print("bamos a eliminar una nota")
                self.proximasAcciones(usuario)
                
            elif accion == "s":
                exit()  
            
            else:
                self.proximasAcciones(usuario)   
                
    ###############   accion de login   ###############        
    def login(self):
        
        print("\nBien¡ identificate en el sistema...")
        
        try:
            email = input("Introduce tu Email:")
            password = input("Introduce tu Contraseña:")
            
            usuario = modelUser.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
              print(f"bienvenido {login[1]} {login[2]}")
              
              self.proximasAcciones(login)
       
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("login incorrecto intentalo de nuevo")
            self.login()
            
        