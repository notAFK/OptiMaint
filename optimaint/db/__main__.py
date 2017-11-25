from optimaint.db.config import BASE, ENGINE


BASE.metadata.create_all(ENGINE)
