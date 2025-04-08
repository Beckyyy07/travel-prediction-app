import joblib
import pandas as pd

def carregar_modelo_e_prever(dados):
    # Carregar o modelo treinado
    modelo = joblib.load("modelo_treinado.pkl")

    # Transformar dados em DataFrame
    df = pd.DataFrame([dados])

    # Fazer predição
    predicao = modelo.predict(df)[0]
    return predicao