from pygments.lexer import default
from sqlalchemy import Column, Integer, String, func, DateTime, Enum
from src.Enums.StateEnum import StateEnum

from ..Connection import Base


class InfoBase(Base):
    __tablename__ = "info_bases"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    libelle = Column(String, nullable=False)
    link_file_batch = Column(String, nullable=False)
    state = Column(Enum(StateEnum), default=StateEnum.DOWN, nullable=False)
    diffusion = Column(String)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)
