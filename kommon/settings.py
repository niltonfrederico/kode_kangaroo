from os import environ

DATABASE_NAME = "db" if "DATABASE_NAME" not in environ else environ["DATABASE_NAME"]
DATABASE_URI = f"sqlite:///{DATABASE_NAME}.db"
