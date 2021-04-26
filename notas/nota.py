############  conexion bd  ############
import usuarios.conexion as conexion

connect = conexion.conextar()
database = connect[0]
cursor = connect[1]

class Nota:
    
    def __init__(self, id_usuario, titulo, descripcion):
      self.id_usuario = id_usuario
      self.titulo = titulo 
      self.descripcion = descripcion
      
    def guardar(self):
        #   NOW() es una funsion sql para guardar la fecha actual
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.id_usuario, self.titulo, self.descripcion)
        
        #try:
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
        #except:   
            #result = [0, self]
        
        #return result