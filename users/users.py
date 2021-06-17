import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class UserService:
    name = "user_service"

    redis = Redis('development')
    '''
    @rpc
    def get(self, cedula):
        #user = self.redis.hgetall(cedula)
        user = self.redis.hgetall(cedula)
        return user

    @rpc
    def create(self, cedula, nombre, apellido, email):
        #user_id = uuid.uuid4().hex 
        self.redis.hmset(cedula, {
            "nombre":nombre,
            "apellido":apellido,
            "email":email
        })
        return cedula
    '''
    @rpc
    def get(self, cedula):
        message = self.redis.hgetall(cedula)
        return message

    @rpc
    def create(self, cedula, nombre, apellido, email):
        #user_id = uuid.uuid4().hex
        self.redis.hmset(cedula, {
            "nombre": nombre,
            "apellido": apellido,
            "email":email
        })
        return cedula
