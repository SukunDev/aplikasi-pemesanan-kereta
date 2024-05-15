from models.main import Model
from views.main import View
from models.actions_model import ActionModel


class DetailOrderController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["detail_order"]

        self._bind()
        self.model.action.add_event_listener("actions", self.action_state_listener)

        self.data = None

    def _bind(self):
        self.frame.next_btn.configure(command=self.next_btn)
        self.frame.back_btn.configure(command=self.back_btn)

    def action_state_listener(self, props: ActionModel) -> None:
        action = props.get()
        if action is not None:
            if action['type'] == "detail_order":
                self.data = action['data']
                self.frame.full_name_label.configure(text=self.model.userModel.current_user['full_name'])
                self.frame.nik_label.configure(text=self.model.userModel.current_user['nik'])
                self.frame.train_name_label.configure(text=action['data']['name'])
                self.frame.tempat_duduk_label.configure(text=f"{chr(ord('a') + action['data']['no_gerbong'] - 1).upper()}{action['data']['no_chair']}")
                self.frame.booking_date_label.configure(text=action['data']['booking_date'])
                self.frame.stasiun_awal_label.configure(text=action['data']['stasiun_awal']['name'])
                self.frame.stasiun_akhir_label.configure(text=action['data']['stasiun_akhir']['name'])
                

    def next_btn(self):
        schedule_id = self.model.userModel.create_user_schedule(data=self.data, no_gerbong=self.data['no_gerbong'], no_chair=self.data['no_chair'])
        self.data.update({"schedule_id": schedule_id})
        self.model.action.set(type="payments", data=self.data)
        self.view.switch("payments")
    
    def back_btn(self):
        self.model.action.set(type="choose_chair", data=self.data)
        self.view.switch("choose_chair")
