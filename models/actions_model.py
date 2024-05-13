from .base import ObservableModel
from datetime import datetime
from .action import Action, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS



class ActionModel(ObservableModel):
    def __init__(self):
        super().__init__()
        engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_TRACK_MODIFICATIONS)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def set(self, type, data):
        new_action = Action(type=type, data=data, created_at=datetime.today())
        self.session.add(new_action)
        self.session.commit()
        self.trigger_event("actions")

    def get(self):
        try:
            return self.session.query(Action).order_by(Action.id.desc()).first().serialize
        except:
            return None