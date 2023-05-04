from sqlalchemy import CHAR, DATETIME, INT, TIMESTAMP, VARCHAR, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CliClient(Base):
    __tablename__ = 'cli_client'
    client_id = Column(CHAR(38))
    association_id = Column(CHAR(38))
    association_type_term = Column(VARCHAR(39))
    status_term = Column(VARCHAR(39))
    display_name = Column(VARCHAR(61))
    created_on = Column(DATETIME)
    created_by = Column(CHAR(39))
    updated_on = Column(DATETIME)
    updated_by = Column(CHAR(39))
    is_active = Column(String(1))
    is_delete = Column(String(1))
    update_log = Column(TIMESTAMP)
    seq_no = Column(INT, primary_key=True, index=True)
    user_type_term = Column(VARCHAR(39))

    class Config:
        orm_mode = True
