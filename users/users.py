import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class UserService:
    name = "user_service"

    redis = Redis('development')

    @rpc
    def get(self, cedula):
        user = self.redis.get(cedula)
        return user

    @rpc
    def create(self, cedula, nombre, apellido, email):
        #user_id = uuid.uuid4().hex
        datos = {
            "nombre":nombre,
            "apellido":apellido,
            "email":email
        }
        self.redis.hmset(cedula, datos)
        return cedula
