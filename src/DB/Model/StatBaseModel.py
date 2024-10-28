from sqlalchemy import Column, Integer, String, func, DateTime

from ..Connection import Base


class StatBase(Base):
    __tablename__ = "stat_bases"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    libelle = Column(String, nullable=False)
    link_file_batch = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)
