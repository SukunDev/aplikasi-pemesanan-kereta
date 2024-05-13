from models.main import Model
from views.main import View
from tkinter import messagebox

class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.configure(command=self.signin)
        self.frame.signup_btn.configure(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_input.get()
        pasword = self.frame.password_input.get()
        if len(username) < 1:
            messagebox.showinfo('Empty Field', 'Username field can\'t empty')
        elif len(pasword) < 1:
            messagebox.showinfo('Empty Field', 'Pasword field can\'t empty')
        else:
            data = {"username": username, "password": pasword}
            self.frame.password_input.delete(0, last_index=len(pasword))
            self.model.userModel.login(data)
