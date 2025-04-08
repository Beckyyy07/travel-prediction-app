import sqlalchemy

def conectar_ao_banco():
    # Configuração de conexão
    engine = sqlalchemy.create_engine("postgresql://usuario:senha@localhost:5432/nomedobanco")
    return engine