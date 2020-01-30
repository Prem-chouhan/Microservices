from nameko.rpc import rpc, RpcProxy
from models import *
from validate import Utility
from smtp import smtp
import jwt
from datetime import datetime, timedelta

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 100000000


class UserService:
    name = "user_note"

    @rpc
    def login_user(self, data):
        response_data = {'success': True, "data": [], "message": ""}
        my_db = DbManaged()
        my_obj = Utility()
        present = my_obj.email_validate(data)
        success = my_db.read_email(data)
        if not present:
            response_data.update({
                "message": "Email Format is Invalid please Re-enter Email",
                "success": False,
                "data": []
            })
        else:
            if success:
                print(success)
                payload = {
                    'id': id,
                    'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
                }

                encoded_token = jwt.encode(payload, 'secret', 'HS256').decode('utf-8')
                redis_obj = RedisService()
                # id_key = id[0]
                redis_obj.set(id, encoded_token)
                print(redis_obj.get(id), '------------->r.get')
                res = response(success=True, message="Login Successfully", data=[{
                    "token": encoded_token
                }])
                Response(self).jsonResponse(status=200, data=res)
                response_data.update({
                    "success": True,
                    "message": "Login done Successfully",
                    "data": []
                })

            else:
                response_data.update({
                    "success": False,
                    "message": "something went wrong",
                    "data": []
                })

        return response_data

    @rpc
    def register_user(self, data):
        response_data = {'success': True, "data": [], "message": ""}
        my_db = DbManaged()
        my_obj = Utility()
        present = my_obj.email_validate(data)
        success = my_db.read_email(data)
        if not present:
            response_data.update({
                "message": "Email Format is Invalid please Re-enter Email",
                "success": False,
                "data": []
            })
        else:
            if success:
                response_data.update({
                    "success": True,
                    "message": "Register user  Successfully",
                    "data": []
                })

            else:
                response_data.update({
                    "success": False,
                    "message": "something went wrong",
                    "data": []
                })

        return response_data

    @rpc
    def forgot_user(self, data):
        response_data = {'success': True, "data": [], "message": ""}
        my_db = DbManaged()
        my_obj = Utility()
        present = my_obj.email_validate(data)
        success = my_db.read_email(data)
        if not present:
            response_data.update({
                "message": "Email Format is Invalid please Re-enter Email",
                "success": False,
                "data": []
            })
        else:
            if success:
                obj = smtp()
                encoded = jwt.encode({"email_id": data}, 'secret', algorithm='HS256').decode("utf-8")
                message = f"http://127.0.0.1:8000/reset/?token={encoded}"
                obj.smtp(data, message)
                response_data.update({
                    "success": True,
                    "message": "Message sent Successfully",
                    "data": []
                })

            else:
                response_data.update({
                    "success": False,
                    "message": "something went wrong",
                    "data": []
                })

        return response_data
