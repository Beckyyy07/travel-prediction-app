from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import joblib
import sqlalchemy
from datetime import datetime

# Inicializar a API
app = FastAPI()

# Conectar ao PostgreSQL
engine = sqlalchemy.create_engine("postgresql://usuario:senha@localhost:5432/nomedobanco")

# Carregar modelo treinado
modelo = joblib.load("modelo_treinado.pkl")

# Classe para validar os dados recebidos
class FormData(BaseModel):
    created: str
    cancel_time: Optional[str] = None
    departure_time: str
    bill_id: str
    ticket_id: str
    reserve_status: str
    user_id: str
    male: bool
    price: float
    coupon_discount: float
    origin: str
    destination: str
    domestic: bool
    vehicle_type: str
    vehicle_class: bool
    vehicle: str
    cancel: bool
    trip_reason: Optional[str] = None

@app.post("/prever")
def prever_viagem(data: FormData):
    # Transformar dados recebidos em DataFrame
    df = pd.DataFrame([data.dict()])

    # Fazer a predição
    predicao = modelo.predict(df)[0]
    df['predicao'] = predicao
    df['prediction_date'] = datetime.now()

    # Salvar no banco de dados
    df.to_sql("predictions", engine, if_exists="append", index=False)

    # Retornar o resultado
    return {"ticket_id": data.ticket_id, "predicao": int(predicao)}