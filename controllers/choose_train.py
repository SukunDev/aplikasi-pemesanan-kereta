from models.main import Model
from models.actions_model import ActionModel
from models.train_model import TrainModel
from views.main import View


class ChooseTrainController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["choose_train"]
        self.train = TrainModel()
        self.train_schedule = []
        self._bind()
        self.model.action.add_event_listener("actions", self.action_state_listener)
        self.booking_date = None

    def _bind(self):
        self.frame.add_schdule(trains=self.train_schedule)
        for loop_index in range(len(self.frame.pilih_btn)):
            pilih_btn_callback = lambda index=loop_index: self.pilih_btn_callback(index)
            self.frame.pilih_btn[loop_index].configure(command=pilih_btn_callback)
    
    def action_state_listener(self, props: ActionModel) -> None:
        action = props.get()
        if action is not None:
            if action['type'] == "choose_train":
                self.booking_date = action['data']['tanggal']
                self.train_schedule = self.train.get_schedule(train_type=action['data']['type'], dari=action['data']['dari'], ke=action['data']['ke'])
                self._bind()

    def pilih_btn_callback(self, index):
        self.train_schedule[index].update({"booking_date": self.booking_date})
        self.model.action.set(type="choose_chair", data=self.train_schedule[index])
        self.view.switch("choose_chair")