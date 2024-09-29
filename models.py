from sqlalchemy import create_engine, BigInteger, Column, Float, String
from sqlalchemy.ext.declarative import declarative_base

# Création d'un moteur pour la base de données SQLite
engine = create_engine('sqlite:///databases/retail_conanguy.db') 
Base = declarative_base()

# Définition des classes de l'ORM
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(String, primary_key=True)
    transaction_date = Column(String)
    category = Column(String)
    name = Column(String)
    quantity = Column(BigInteger)
    amount_excl_tax = Column(Float)
    amount_inc_tax = Column(Float)
    
if __name__ == '__main__':
    # Drop the table if it already exists
    Transaction.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)