from models.main import Model
from models.user_model import UserModel
from views.main import View

from .home import HomeController
from .signin import SignInController
from .signup import SignUpController
from .welcome import WelcomeController
from .order import OderController
from .add_penumpang import AddPenumpangController
from .choose_train import ChooseTrainController
from .choose_chair import ChooseChairController
from .detail_order import DetailOrderController
from .payments import PaymentsController
from .ticket import TicketController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)
        self.welcome_controller = WelcomeController(model, view)
        self.order = OderController(model, view)
        self.add_penumpang = AddPenumpangController(model, view)
        self.choose_train = ChooseTrainController(model, view)
        self.choose_chair = ChooseChairController(model, view)
        self.detail_order = DetailOrderController(model, view)
        self.payments = PaymentsController(model, view)
        self.ticket = TicketController(model, view)

        self.model.userModel.add_event_listener("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, data: UserModel) -> None:
        if data.is_logged_in:
            if data.current_user['full_name'] != '' and data.current_user['nik'] != '':
                self.order.frame.add_penumpang_btn.grid_forget()
                self.order.frame.full_name.configure(text=data.current_user['full_name'])
                self.order.frame.next_btn.place(x=745, y=425)
            else:
                self.order.frame.next_btn.place_forget()

            if data.current_user['is_new_user']:
                self.view.switch("welcome")
            else:
                check_user_schedule = self.model.userModel.get_user_schedule()
                if check_user_schedule is not None:
                    self.model.action.set(type="detail_order", data=check_user_schedule)
                    self.view.switch("detail_order")
                else:
                    self.view.switch("home")
        else:
            self.view.switch("signin")

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # TODO: hilankan
        if self.model.userModel.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("signin")

        # TODO: bypass
        # self.view.switch("payments")
        self.view.start_mainloop()
