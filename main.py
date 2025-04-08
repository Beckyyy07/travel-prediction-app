import os
import psycopg2
from psycopg2.extras import execute_values 
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

# Configuração de conexão
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
 }

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    created TIMESTAMP,
    cancel_time TIMESTAMP,
    departure_time TIMESTAMP,
    bill_id VARCHAR,
    ticket_id VARCHAR UNIQUE NOT NULL,
    reserve_status VARCHAR,
    user_id VARCHAR,
    male BOOLEAN,
    price FLOAT,
    coupon_discount FLOAT,
    origin VARCHAR,
    destination VARCHAR,
    domestic BOOLEAN,
    vehicle_type VARCHAR,
    vehicle_class BOOLEAN,
    vehicle VARCHAR,
    cancel BOOLEAN,
    trip_reason VARCHAR,
    predicao INT,
    prediction_date TIMESTAMP
);
            """)

conn.commit()

cur.close()
conn.close()
