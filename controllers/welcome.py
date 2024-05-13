from models.main import Model
from views.main import View


class WelcomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["welcome"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.next_btn.configure(command=self.next)

    def next(self) -> None:
        self.model.userModel.welcome_next_btn()
        self.view.switch("home")
