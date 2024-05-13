from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Train(Base):
    __tablename__ = 'trains'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_code = Column(String)
    type = Column(String)
    total_gerbong = Column(Integer)
    total_chair = Column(Integer)
    created_at = Column(Date)

    def __repr__(self):
        return f"<Train(id='{self.id}', name='{self.name}', name_code='{self.name_code}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_code': self.name_code,
            'type': self.type,
            'total_gerbong': self.total_gerbong,
            'total_chair': self.total_chair,
            'created_at': self.created_at.isoformat(),
        }
