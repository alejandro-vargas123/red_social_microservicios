import uuid
import jwt

from nameko.rpc import rpc
from nameko_redis import Redis


class UserService:
    name = "user_service"

    redis = Redis('development')
    
    @rpc
    def get(self, cedula):
        usuario = self.redis.hgetall(cedula)
        return usuario

    @rpc
    def create(self, cedula, nombre, apellido, email):
        #user_id = uuid.uuid4().hex
        self.redis.hmset(cedula, {
            "nombre": nombre,
            "apellido": apellido,
            "email":email
        })
        return cedula
    
    @rpc
    def verify(self,cedula):
        estado = False
        usuario = self.redis.hgetall(cedula)
        if len(usuario) > 0:
            estado = True
        
        return estado
