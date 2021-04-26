import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        
        print(f"{usuario[1]} Vamos a crear una nota")
        
        titulo = input(f"\nintroduse el titulo de la nota: ")
        descripcion = input(f"\nintroduse la descripcion de la nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar <= 1:
            print(f"\nhaz guardado la nota: {nota.titulo}")
        else:
            print(f"\n{usuario[1]} la nota no se a guardado correctamente")