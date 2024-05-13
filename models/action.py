from sqlalchemy import Column, Integer, String, JSON, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Action(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    data = Column(JSON)
    created_at = Column(Date)

    def __repr__(self):
        return f"<User(id='{self.id}', type='{self.type}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'data': self.data,
            'created_at': self.created_at.isoformat(),
        }
