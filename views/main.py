from typing import TypedDict

from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView
from .welcome import WelcomeView
from .order import OrderView
from .add_penumpang import AddPenumpangView
from .choose_train import ChooseTrainView
from .choose_chair import ChooseChairView
from .detail_order import DetailOrderView
from .payments import PaymentsView
from .ticket import TicketView


class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView
    welcome: WelcomeView
    order: OrderView
    add_penumpang: AddPenumpangView
    choos_train: ChooseTrainView
    choose_chair: ChooseChairView
    detail_order: DetailOrderView
    payments: PaymentsView
    ticket: TicketView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(WelcomeView, "welcome")
        self._add_frame(OrderView, "order")
        self._add_frame(AddPenumpangView, "add_penumpang")
        self._add_frame(ChooseTrainView, "choose_train")
        self._add_frame(ChooseChairView, "choose_chair")
        self._add_frame(DetailOrderView, "detail_order")
        self._add_frame(PaymentsView, "payments")
        self._add_frame(TicketView, "ticket")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root, fg_color="white", bg_color="white")
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
