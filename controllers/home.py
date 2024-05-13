from models.main import Model
from views.main import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.antar_kota_btn.configure(command=self.antar_kota_btn)
        self.frame.local_btn.configure(command=self.local_btn)

    def antar_kota_btn(self) -> None:
        self.model.action.set(type="order", data={"type": "antar_kota", "message": "KERETA ANTAR KOTA"})
        self.view.switch("order")

    def local_btn(self) -> None:
        self.model.action.set(type="order", data={"type": "lokal", "message": "KERETA LOKAL"})
        self.view.switch("order")

