# backend/controller/connector.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
from datetime import datetime

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///mydatabase.db')  # Altere conforme necessário

# Cria o engine e a sessão do SQLAlchemy
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Declarative base para definição de modelos
Base = declarative_base()

# Definição do modelo Commit
class Commit(Base):
    __tablename__ = 'commits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    commit_time = Column(TIMESTAMP, nullable=False)
    commit_id = Column(String, nullable=False)
    ticket_id = Column(Integer, nullable=False)
    commit_text = Column(String, nullable=False)
    prediction = Column(Float, nullable=False)
    label_status = Column(String, nullable=False)
    history_datetime = Column(TIMESTAMP, nullable=False)

# Criação da tabela no banco de dados
def create_tables():
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso.")

# Função para adicionar dados à tabela
def add_commit(commit_data):
    new_commit = Commit(**commit_data)
    session.add(new_commit)
    session.commit()
    print("Dados inseridos com sucesso.")

# Função para buscar todos os commits
def fetch_commits():
    return session.query(Commit).all()

# Exemplo de uso para testar
if __name__ == "__main__":
    # Criação da tabela (descomente se precisar criar a tabela)
    # create_tables()

    # Exemplo de dados para inserção (descomente para inserir dados)
    commit_data = {
         'commit_time': datetime.now(),
         'commit_id': '1069',
         'ticket_id': 1069,
         'commit_text': '1069 fixed error.',
         'prediction': 0.75,
         'label_status': 'Aprovado',
         'history_datetime': datetime.now()
     }
    add_commit(commit_data)
     
    # Exemplo de busca de commits
    commits = fetch_commits()
    for commit in commits:
        print(f"ID: {commit.id}, Commit ID: {commit.commit_id}, Commit Time: {commit.commit_time}")
    

