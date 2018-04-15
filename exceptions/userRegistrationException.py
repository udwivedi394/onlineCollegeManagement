class invalidEmailId(Exception):
    def __init__(self):
        super().__init__("Invaid Email ID!!")

class invalidUserid(Exception):
    def __init__(self):
        super().__init__("User-id already exists!!")

class invalidPassword(Exception):
    def __init__(self):
        super().__init__("Password is not strong enough!!")

class invalidConfirmPass(Exception):
    def __init__(self):
        super().__init__("Confirm password not matching!!")
