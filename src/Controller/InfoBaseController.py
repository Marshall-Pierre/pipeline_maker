from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..DB.Model.InfoBaseModel import InfoBase
from ..Schema import InfoBaseSchema

def get_all_info_base(db: Session):
    return db.query(InfoBase).all()

def add_info_base(db: Session, info_base: InfoBaseSchema.Create):
    db_info_base = InfoBase(
        libelle=info_base.libelle,
        link_file_batch=info_base.link_file_batch
    )
    db.add(db_info_base)
    try:
        db.commit()
        db.refresh(db_info_base)
        return db_info_base
    except IntegrityError:
        db.rollback()
        print("déjà existant")
        return None
