from environs import Env

config = Env()

ENVIRONMENT = config("ENVIRONMENT", "dev")

if ENVIRONMENT == "test":
    DATABASE_NAME = config("DATABASE_NAME", "development")
    DATABASE_URI = f"sqlite:///{DATABASE_NAME}.db"
