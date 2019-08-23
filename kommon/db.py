from sqlalchemy import create_engine, sessionmaker

Session = sessionmaker()

engine = create_engine("sqlite:///db.db")

session = Session(bind=engine)
