from core.database import Base, engine

from models.agent import Agent

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")