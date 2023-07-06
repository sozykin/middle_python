from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column
from sqlalchemy import String, Integer
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Базовый класс для создание классов, которые будут сохраняться в базе данных
Base = declarative_base()

# Создаем класс и описываем отображение атрибутов в столбцы таблицы базы данных
class Name(Base):
    # Название таблицы в базе данных
    __tablename__ = 'names'

    # Атрибуты  
    id = Column('id', Integer)
    name = Column('name', String)
    number_of_persons = Column('number_of_persons', Integer)
    global_id = Column('global_id', Integer, primary_key=True)
    year = Column('year', Integer)
    month = Column('month', String)

    # Функция инициализации
    def __init__(self, id, name, number_of_persons, global_id, year, month):
        self.id = id
        self.name = name
        self.number_of_persons = number_of_persons
        self.global_id = global_id
        self.year = year
        self.month = month

    # Текстовое представление объекта
    def __repr__(self):
        return(f"{self.id}, {self.name}, {self.number_of_persons}, {self.global_id}, {self.year}, {self.month}")
    
# Создаем соединение с базой данных SQLite
engine = create_engine("sqlite:///test.db")
                       
# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)