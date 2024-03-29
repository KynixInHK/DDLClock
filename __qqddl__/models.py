from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    group_number = Column(String(15), unique=True, index=True)  # 群号
    group_name = Column(String(40))
    group_ren = Column(String(20))
    is_active = Column(Boolean, default=True)

# class Msg(Base):
#     __tablename__="messages"

#     id = Column(Integer,primary_key=True,index=True,autoincrement=True)
#     relevant_DDL=Column(Integer)
#     from_group=Column(String,index=True)
#     internal_id=Column(Integer)


class DDLs(Base):
    __tablename__ = "DDLs"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    description = Column(String, index=True)
    text = Column(String, index=True)  # 群聊消息
    ddltime = Column(String)  # ddl时间
    status = Column(String)  # 紧急情况
    group_num = Column(String(15))
