from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from sqlalchemy.orm import sessionmaker

DATABASE = {
  'drivername': 'postgres',
  'host': 'localhost',
  #'port': '5432',
  'username': 'pet',
  'password': 'pet',
  'database': 'pet'
}


class Backend(object):
  def __init__(self):
    engine = create_engine(
        URL(**DATABASE),
        pool_size = 5,
        pool_recycle = 3600,
        #pool_size = options.mysql_poolsize,
        #pool_recycle = 3600,
        #echo=options.debug,
        #echo_pool=options.debug
    )
    self._session = sessionmaker(bind=engine)
  
  @classmethod
  def instance(cls):
    """Singleton like accessor to instantiate backend object"""
    if not hasattr(cls,"_instance"):
      cls._instance = cls()
    return cls._instance
  
  def get_session(self):
    return self._session()

db = Backend.instance().get_session()
