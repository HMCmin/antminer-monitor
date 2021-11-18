from sqlalchemy import Column, Integer, String
from antminermonitor.database import Base

class Miner(Base):
    __tablename__ = 'miner'
    id = Column(Integer, primary_key=True)
    ip = Column(String(15), unique=True, nullable=False)
    ips = Column(Integer, unique=True, nullable=False)
    model_id = Column(String(15), nullable=False)
    remarks = Column(String(255), nullable=True)

    def __repr__(self):
        return "Miner(ip='{}', ips='{}', model_id='{}', remarks='{}')" \
            .format(self.ip, self.ips, self.model_id, self.remarks)
