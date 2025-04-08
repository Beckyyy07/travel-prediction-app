import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Treinar e salvar o modelo
def treinar_modelo():
    # Carregar dataset
    data = pd.read_csv("dataset/train_data.csv")

    # Preenchendo valores nulos e convertendo colunas categóricas
    data = data.dropna()
    data['TripReason'] = data['TripReason'].astype('category').cat.codes

    # Separar features e rótulo
    X = data.drop('TripReason', axis=1)
    y = data['TripReason']

    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar modelo de Árvore de Decisão
    modelo = DecisionTreeClassifier(criterion='entropy', random_state=42)
    modelo.fit(X_train, y_train)

    # Avaliar o modelo
    y_pred = modelo.predict(X_test)
    print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
    print("\nRelatório de Classificação:\n")
    print(classification_report(y_test, y_pred))

    # Salvar o modelo treinado
    joblib.dump(modelo, "modelo_treinado.pkl")

treinar_modelo()  # Treinar e salvar o modelo