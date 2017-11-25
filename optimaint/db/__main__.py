from optimaint.db.config import BASE, ENGINE, SESSION
from optimaint.db.database import Train

train = Train(uuid=200039, company='VW', no_cars=5)

BASE.metadata.create_all(ENGINE)

session = SESSION()
session.add(train)
session.commit()
