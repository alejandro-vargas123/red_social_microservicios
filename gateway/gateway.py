import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    user_rpc = RpcProxy('user_service')
    message_rpc = RpcProxy('message_service')
    auth_rpc = RpcProxy('auth_service')

    @http('POST', '/auth')
    def auth(self, request):
        data = json.loads(request.get_data(as_text=True))
        cedula = data['cedula']
        usuario = self.user_rpc.get(cedula)
        esExistente = self.user_rpc.verify(cedula)
        if esExistente:
            token = self.auth_rpc.access_token(cedula,usuario)
            return token
        else:
            token = 'False'
            return token

    @http('POST', '/userInfo')
    def userInfo(self, request):
        data = json.loads(request.get_data(as_text=True))
        cedula = data['cedula']
        user = self.user_rpc.get(cedula)
        return json.dumps(user)

    @http('POST', '/createUser')
    def createUser(self, request):
        data = json.loads(request.get_data(as_text=True))
        cedula = self.user_rpc.create(data['cedula'],data['nombre'],data['apellido'],data['email'])

        return cedula

    @http('POST', '/message')
    def messages(self, request):
        data = json.loads(request.get_data(as_text=True))
        message_id = data['message_id']
        message = self.message_rpc.get(message_id)
        return json.dumps(message)

    @http('POST', '/createMessage')
    def createMessage(self, request):
        data = json.loads(request.get_data(as_text=True))
        message_id = self.message_rpc.create(data['token'], data['message'])

        return message_id
