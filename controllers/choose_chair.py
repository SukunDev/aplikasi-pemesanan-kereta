from models.main import Model
from views.main import View
from models.actions_model import ActionModel


class ChooseChairController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["choose_chair"]

        self.current_pos = 1
        self.total_gerbong = 5
        self.total_chair = 36
        self._bind()

        self.schedules = None

        self.model.action.add_event_listener("actions", self.action_state_listener)

    def _bind(self):
        self.frame.header_label.configure(text=f"PILIH KURSI GERBONG {self.current_pos}")
        self.frame.add_kursi(total_chair=self.total_chair)
        self.frame.next_button.configure(command=self.next_button)
        self.frame.prev_button.configure(command=self.prev_button)
        for loop_index in range(len(self.frame.choose_chair_btn)):
            choose_btn_callback = lambda index=int(loop_index+1): self.choose_btn(index)
            self.frame.choose_chair_btn[loop_index].configure(text=f"{chr(ord('a') + self.current_pos - 1).upper()}{loop_index+1}", command=choose_btn_callback)
    
    def _update_view(self):
        self.frame.header_label.configure(text=f"PILIH KURSI GERBONG {self.current_pos}")
        for loop_index in range(len(self.frame.choose_chair_btn)):
            self.frame.choose_chair_btn[loop_index].configure(text=f"{chr(ord('a') + self.current_pos - 1).upper()}{loop_index+1}")

    def action_state_listener(self, props: ActionModel) -> None:
        action = props.get()
        if action is not None:
            if action['type'] == "choose_chair":
                self.schedules = action['data']

    def next_button(self):
        if self.current_pos < self.total_gerbong:
            self.current_pos+=1
        self._update_view()

    def prev_button(self):
        if self.current_pos > 1:
            self.current_pos-=1
        self._update_view()

    def choose_btn(self, index):
        schedule_id = self.model.userModel.create_user_schedule(data=self.schedules, no_gerbong=self.current_pos, no_chair=index)
        self.schedules.update({"no_gerbong":self.current_pos, "no_chair":index, "schedule_id": schedule_id})
        self.model.action.set(type="detail_order", data=self.schedules)
        self.view.switch("detail_order")
        