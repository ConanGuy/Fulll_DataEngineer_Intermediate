from sqlalchemy import create_engine, BigInteger, Column, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_engine(db: str):
    return create_engine(f'sqlite:///databases/{db}.db')

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
    engine = get_engine('retail_conanguy')
    Transaction.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)