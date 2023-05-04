from datetime import datetime

from sqlalchemy import (CHAR, DATETIME, INT, TEXT, TIMESTAMP, VARCHAR, Column,
                        String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UsrUser(Base):
    __tablename__ = 'usr_user'
    user_id = Column(CHAR(38), nullable=False)
    client_id = Column(CHAR(38))
    association_id = Column(CHAR(38))
    association_type_term = Column(VARCHAR(39))
    user_name = Column(VARCHAR(61))
    password = Column(TEXT)
    token = Column(TEXT)
    status_term = Column(VARCHAR(39))
    profile_pic = Column(VARCHAR(361))
    display_name = Column(VARCHAR(61))
    created_on = Column(DATETIME)
    created_by = Column(CHAR(39))
    updated_on = Column(DATETIME)
    updated_by = Column(CHAR(39))
    email = Column(CHAR(161))
    mobile_no = Column(CHAR(13))
    is_active = Column(String(1))
    is_delete = Column(String(1))
    update_log = Column(TIMESTAMP, default=datetime.now())
    seq_no = Column(INT, primary_key=True, index=True)
    user_type_term = Column(VARCHAR(39))
    is_default = Column(String(1))
    is_it_admin = Column(String(1))
    forgot_password_token = Column(TEXT)

    class Config:
        orm_mode = True
