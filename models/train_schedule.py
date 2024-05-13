from sqlalchemy import Column, Integer, String, Time, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrainSchedule(Base):
    __tablename__ = 'train_schedules'

    id = Column(Integer, primary_key=True)
    train_id = Column(Integer)
    station = Column(String)
    arrival = Column(Time)
    departure = Column(Time)
    created_at = Column(Date)

    def __repr__(self):
        return f"<TrainSchedule(id='{self.id}', train_id='{self.train_id}', station='{self.station}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'train_id': self.train_id,
            'station': self.station,
            'arrival': self.arrival,
            'departure': self.departure,
            'created_at': self.created_at.isoformat(),
        }
