# src/etl.py

import pandas as pd
import requests
from pandas import DataFrame

def cargar_datos_desde_api(url: str) -> pd.DataFrame:
    """Carga y aplana los datos JSON desde una URL."""
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener los datos: {response.status_code}")
    
    data_json = response.json()
    df = pd.json_normalize(data_json)
    
    print("✅ Datos cargados correctamente.")
    return df