from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class Model(Model):
    __abstract__ = True
