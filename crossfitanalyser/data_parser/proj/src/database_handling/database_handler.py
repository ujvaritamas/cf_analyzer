from sqlalchemy import create_engine, insert, text
import sqlalchemy as db

from sqlalchemy import Table, Column, MetaData

meta = MetaData()
students = Table(
   'athletes', meta,
   Column('id', db.Integer, db.Identity(start=1, cycle=True), primary_key=True),
    db.Column('name', db.String),
    db.Column('age', db.Integer),
    db.Column('height', db.Float),
    db.Column('weight', db.Float),
    db.Column('rank', db.Integer),
)


class DataBaseHandler:
    def __init__(self) -> None:
        #'postgresql+psycopg2://{user}:{password}\\@{hostname}/{database_name}'
        conn_url = 'postgresql+psycopg2://yourUserDBName:yourUserDBPassword@yourDBDockerContainerName/yourDBName'
        self.engine = db.create_engine("postgresql+psycopg2://my_user:my_pwd@db:5432/exampledb")
        #self.conn = self.engine.connect()
        self.table_name = 'athletes'
        self.metadata_obj = db.MetaData()
        self.table = db.Table(
            self.table_name,
            self.metadata_obj,
            db.Column('id', db.Integer, db.Identity(start=1, cycle=True), primary_key=True),
            db.Column('name', db.String),
            db.Column('age', db.Integer),
            db.Column('height', db.Float),
            db.Column('weight', db.Float),
            db.Column('rank', db.Integer),
        )


    def create_athlete_table(self):
        self.metadata_obj.create_all(self.engine)

    def insert_athlete(self, athlete):
        stmt = db.insert(self.table).values(name=athlete.name, age=athlete.age, height = athlete.height, weight=athlete.weight, rank=athlete.rank)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()

import Athlete


#db_handler = DataBaseHandler()
#db_handler.create_athlete_table()
#db_handler.insert_athlete(3)

#print('done')