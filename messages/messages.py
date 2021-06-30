import uuid
import jwt

from nameko.rpc import rpc
from nameko_redis import Redis


class MessageService:
    name = "message_service"

    redis = Redis('development')

    @rpc
    def get(self, message_id):
        message = self.redis.hgetall(message_id)
        return message

    @rpc
    def create(self, token, message):
        message_id = uuid.uuid4().hex
        usuario = jwt.decode(token,"secret",algorithms=["HS256"])
        self.redis.hmset(message_id, {
            "cedula": usuario['cedula'],
            "message": message
        })
        return message_id
