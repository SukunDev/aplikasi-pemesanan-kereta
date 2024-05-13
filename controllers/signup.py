from models.main import Model
from views.main import View
from tkinter import messagebox


class SignUpController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.configure(command=self.signin)


    def signin(self) -> None:
        data = {
            "username": self.frame.username_input.get(),
            "password": self.frame.password_input.get(),
            "confirm": self.frame.confirm_input.get(),
        }
        if len(data['username']) < 1:
            messagebox.showinfo('Empty Field', 'Username field can\'t empty')
        elif len(data['password']) < 1:
            messagebox.showinfo('Empty Field', 'Pasword field can\'t empty')
        elif len(data['confirm']) < 1:
            messagebox.showinfo('Empty Field', 'Confirm field can\'t empty')
        elif data['password'] != data['confirm']:
            messagebox.showerror('Error', 'Password and Confirm does not match')
        else:
            self.model.userModel.register(data)
            self.clear_form()
        
    
    def clear_form(self) -> None:
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        confirm = self.frame.confirm_input.get()
        self.frame.username_input.delete(0, last_index=len(username))
        self.frame.username_input.focus()
        self.frame.password_input.delete(0, last_index=len(password))
        self.frame.confirm_input.delete(0, last_index=len(confirm))


