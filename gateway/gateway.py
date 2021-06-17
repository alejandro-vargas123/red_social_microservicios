import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    user_rpc = RpcProxy('user_service')
    message_rpc = RpcProxy('message_service')

    @http('GET', '/user/<string:cedula>')
    def get_user(self, request, cedula):
        user = self.user_rpc.get(cedula)#get(posiblemente)
        return json.dumps(user)

    @http('POST', '/user')
    def post_user(self, request):
        data = json.loads(request.get_data(as_text=True))
        cedula = self.user_rpc.create(data['cedula'],data['nombre'],data['apellido'],data['email'])

        return cedula

    @http('GET', '/message/<string:message_id>')
    def get_message(self, request, message_id):
        message = self.message_rpc.get(message_id)
        return json.dumps(message)

    @http('POST', '/message')
    def post_message(self, request):
        data = json.loads(request.get_data(as_text=True))
        message_id = self.message_rpc.create(data['cedula'], data['message'])

        return message_id
