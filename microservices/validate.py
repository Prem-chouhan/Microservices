import re


class Utility:

    def email_validate(self, email):
        """Here email validation is done"""
        print(email)
        if re.match(f"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        else:
            return False
