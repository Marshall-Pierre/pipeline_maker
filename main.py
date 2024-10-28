from src.DB import Migration, Connection

Migration.Base.metadata.create_all(bind=Connection.engine)
