from .user_model import UserModel
from .actions_model import ActionModel

class Model:
    def __init__(self):
        self.userModel = UserModel()
        self.action = ActionModel()
    
