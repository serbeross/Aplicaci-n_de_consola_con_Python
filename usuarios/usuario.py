###############   modulo fecha   ###############
import datetime
###############   modulo para incriptar password   ###############
import hashlib
###############   conexion base de datos   ###############
import usuarios.conexion as conexion

connect = conexion.conextar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    ###############   constructor   ###############
    def __init__(self, nombre, apellido, email, password):
      self.nombre = nombre
      self.apellido = apellido
      self.email = email
      self.password =password 
      
    ###############   crear un usuario   ###############
    def registrar(self):
        fecha = datetime.datetime.now()
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuarios VALUE(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
            
        except:
            result = [0, self]
        
        return result
    
    ###############   consulta de login   ###############
    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result
        