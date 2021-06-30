import uuid
import json
import jwt

from nameko.rpc import rpc
from nameko_redis import Redis


class AuthService:
    name = "auth_service"

    redis = Redis('development')
    
    @rpc
    def access_token(self,cedula,usuario):
        usuario['cedula'] = cedula
        encoded_token = jwt.encode(usuario,"secret",algorithm='HS256')
        return encoded_token
