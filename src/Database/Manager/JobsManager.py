import sqlalchemy as db
from src.Config import Config
from sqlalchemy import text, insert
import hashlib


class JobsManager:
    def __init__(self, config: Config):
        self.__config = config
        self.__connectionString = self.__config.get_database_connection_string()
        self.__engine = db.create_engine(self.__connectionString)
        self.__metadata = db.MetaData()

        self.__con = self.__engine.connect()

        self.__jobsTable = db.Table('jobs', self.__metadata, autoload_with=self.__engine)

    def add_new_job(self, title: str, link: str) -> bool:
        hash = hashlib.md5(f'{title}:{link}'.encode('utf8')).hexdigest()

        if self.exists(hash):
            return False

        self.insert(hash, title, link)

        return True

    def exists(self, hash: str) -> bool:
        query = self.__jobsTable.select().add_columns(text('id')).where(text('hash = :hash')).params(hash=hash)
        row = self.__con.execute(query).fetchone()

        return True if row else False

    def insert(self, hash: str, title: str, link: str) -> None:
        stmt = (
            insert(self.__jobsTable).
            values(hash=hash, title=title, link=link)
        )

        self.__con.execute(stmt)
        self.__con.commit()
