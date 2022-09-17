from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, TIMESTAMP, BIGINT, BOOLEAN, text, CHAR, VARCHAR, DATETIME, INT

Base = declarative_base()


class UsrUser(Base):
    __tablename__ = "UsrUser"
    user_id = Column(CHAR(38))
    client_id = Column(CHAR(38))
    association_id = Column(CHAR(38))
    association_type_term = Column(VARCHAR(39))
    user_name = Column(VARCHAR(61))
    password = Column(String)
    token = Column(String)
    status_term = Column(VARCHAR(39))
    profile_pic = Column(VARCHAR(361))
    display_name = Column(VARCHAR(61))
    created_on = Column(DATETIME)
    created_by = Column(CHAR(39))
    updated_on = Column(DATETIME)
    updated_by = Column(CHAR(39))
    email = Column(CHAR(161))
    mobile_no = Column(CHAR(13))
    is_active = Column(String)
    is_delete = Column(String)
    update_log = Column(TIMESTAMP)
    seq_no = Column(INT, primary_key=True, index=True)
    user_type_term = Column(VARCHAR(39))
    is_default = Column(String)
    is_it_admin = Column(String)
    forgot_password_token = Column(String)
