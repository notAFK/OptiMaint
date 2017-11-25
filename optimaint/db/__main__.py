from optimaint.db.config import BASE, ENGINE
from optimaint.db.database import Train

train = Train(uuid=200039, company='VW', no_cars=5)
print(train)

BASE.metadata.create_all(ENGINE)
