from models.main import Model
from views.main import View
from models.actions_model import ActionModel


class PaymentsController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["payments"]
        self.data = None
        
        self._bind()
        self.model.action.add_event_listener("actions", self.action_state_listener)

    def _bind(self):
        self.frame.next_btn.configure(command=self.next_btn)

    def action_state_listener(self, props: ActionModel) -> None:
        action = props.get()
        if action is not None:
            if action['type'] == "payments":
                self.data = action['data']
    
    def next_btn(self):
        self.model.action.set(type="ticket", data=self.data)
        self.model.userModel.update_schedule(schedule_id=self.data['schedule_id'])
        self.view.switch("ticket")
               
                