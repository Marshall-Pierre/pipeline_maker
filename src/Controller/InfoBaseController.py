import traceback

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import update

from ..DB.Model.InfoBaseModel import InfoBase
from ..Schema import InfoBaseSchema
from ..Enums import StateEnum
from src.Utils import EventBusInstance

event_bus = EventBusInstance.event_bus


def get_all_info_base(db: Session):
    return db.query(InfoBase).all()

def get_info_base_by_id(db: Session, _id: int):
    info_base = db.query(InfoBase).filter(InfoBase.id == _id).first()
    if info_base is not None:
        return InfoBaseSchema.Read(**vars(info_base))


def add_info_base(db: Session, info_base: InfoBaseSchema.Create):
    db_info_base = InfoBase(
        libelle=info_base.libelle,
        link_file_batch=info_base.link_file_batch,
        diffusion=info_base.diffusion
    )
    db.add(db_info_base)
    try:
        db.commit()
        db.refresh(db_info_base)
        return db_info_base
    except IntegrityError as e:
        db.rollback()
        print("Une erreur d'intégrité s'est produite:", e)
        print(traceback.format_exc())  # Imprimer la trace complète de l'erreur
        return None


def update_info_base(db: Session, row):
    print(f"{row.id}, {row.libelle}, {row.link_file_batch}, {row.diffusion}")
    query = update(InfoBase).where(InfoBase.id == row.id).values(
        libelle=row.libelle,
        link_file_batch=row.link_file_batch,
        diffusion=row.diffusion
    )
    db.execute(query)
    db.commit()
    return query

def delete_info_base(db: Session, _id: int):
    db_info_base = db.query(InfoBase).filter(InfoBase.id == _id).first()
    if db_info_base is not None:
        db.delete(db_info_base)
        db.commit()
        return True

def update_state_by_link_file_batch(db: Session, link_file_batch: str, state: StateEnum):
    query = update(InfoBase).where(InfoBase.link_file_batch == link_file_batch).values(
        state=state,
    )
    db.execute(query)
    db.commit()
    event_bus.emit("actualise_data", 1)
    return query
