import pandas as pd

# Leer un archivo CSV de ejemplo
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados correctamente:")
        print(data.head())
        return data
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe.")
        return None

# Procesar datos básicos
def process_data(data):
    if data is not None:
        print(f"Resumen de datos:\n{data.describe()}")
    else:
        print("No hay datos para procesar.")

if __name__ == "__main__":
    # Ruta del archivo CSV
    file_path = "./data/sample.csv"
    
    # Cargar y procesar datos
    data = load_data(file_path)
    process_data(data)
