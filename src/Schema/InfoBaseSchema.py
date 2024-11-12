from pydantic import BaseModel
from datetime import datetime
from ..Enums.StateEnum import StateEnum


class Base(BaseModel):
    libelle: str
    link_file_batch: str
    diffusion: str | None = None


class Create(Base):
    pass

class Read(Base):
    id: int
    state: StateEnum
    created_at: datetime
    updated_at: datetime


class Schema(Read):
    class Config:
        from_attributes = True
        use_enum_values = True