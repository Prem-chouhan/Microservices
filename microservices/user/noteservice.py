class NoteService:
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