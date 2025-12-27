import pandas as pd
import numpy as np
datos = pd.read_csv('living.csv')
print(datos.head())
print(datos.info())
print(datos.describe())
nuevo= pd.DataFrame(datos)
print(nuevo.head())