import json
from nameko.web.handlers import http
from nameko.rpc import rpc, RpcProxy
from nameko.standalone.rpc import ClusterRpcProxy
from werkzeug.wrappers import Response

config = {
    'AMQP_URI': 'amqp://guest:guest@localhost',
}


class HttpService(object):
    name = "gateway"

    # user_rpc = RpcProxy('user_note')

    @http('post', '/login')
    def login(self, request):
        request_data = json.loads(request.get_data(as_text=True))
        print(request_data, type(request_data))
        data = request_data['email']
        with ClusterRpcProxy(config) as cluster_rpc:
            conv_data = json.dumps(data)
            response = cluster_rpc.user_note.login_user(data)
        return Response(result)

    @http('post', '/register')
    def register(self, request):
        request_data = json.loads(request.get_data(as_text=True))
        print(request_data, type(request_data))
        data = request_data['email']
        with ClusterRpcProxy(config) as cluster_rpc:
            conv_data = json.dumps(data)
            response = cluster_rpc.user_note.register_user(data)
            result = json.dumps(response)
        return Response(result)

    @http('post', '/forgot')
    def forgot(self, request):
        request_data = json.loads(request.get_data(as_text=True))
        print(request_data, type(request_data))
        data = request_data['email']
        with ClusterRpcProxy(config) as cluster_rpc:
            conv_data = json.dumps(data)
            response = cluster_rpc.user_note.forgot_user(data)
            result = json.dumps(response)
        return Response(result)

    # @http('post', '/api/note/insert')
    # def forgot(self, request):
    #     request_data = json.loads(request.get_data(as_text=True))
    #     print(request_data, type(request_data))
    #     data = request_data['email']
    #     with ClusterRpcProxy(config) as cluster_rpc:
    #         conv_data = json.dumps(data)
    #         response = cluster_rpc.user_note.forgot_user(data)
    #         result = json.dumps(response)
    #     return Response(result)