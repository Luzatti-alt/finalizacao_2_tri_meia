from sqlalchemy import create_engine, Column, String , Integer,Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
#criar db
db = create_engine("sqlite:///Meia_controle_fios.db")#tipo de sql:///nome do db.db
#sessão com o db
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base() #permitir que exista herança de classes
class Cores(Base):
  __tablename__ = 'Cores de meia'
  id = Column("id",Integer,primary_key=True, autoincrement=True)#chave principal & qnd add uma nova cor ele ja cria um novo id
  cor = Column("cor",String)
  quantidade_cor_kg = Column("quantidade_cor_kg",Float)
  disponivel = Column("disponivel",Boolean)
  def __int__(self,cor,quantidade_cor_kg,disponivel = True):
    self.cor = cor
    self.quantidade_cor_kg = quantidade_cor_kg
    self.disponivel = disponivel

#criar o arquivo do db com o que precisa
Base.metadata.create_all(bind=db)#ele cria o arquivo do db
Cores(cor="vermelho",quantidade_cor_kg="100",disponivel=True)
