from pgmpy.models import  BayesianNetwork
from pgmpy.estimators import ParameterEstimator, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Definir la estructura del modelo para clasificación
modelo_clasificacion =  BayesianNetwork([('Nivel_Glucosa', 'Diabetes'), ('Presion_Sanguinea', 'Diabetes')])

# Datos de entrenamiento ficticios
data_clasificacion = pd.DataFrame(data={
    'Nivel_Glucosa': [120, 90, 150, 110, 130, 95, 140, 105, 125, 100],
    'Presion_Sanguinea': [80, 70, 95, 85, 75, 65, 90, 80, 88, 72],
    'Diabetes': ['Si', 'No', 'Si', 'No', 'Si', 'No', 'Si', 'No', 'Si', 'No']
})

# Establecer los datos en el modelo
modelo_clasificacion.fit(data_clasificacion, estimator=MaximumLikelihoodEstimator)

# Imprimir las CPDs aprendidas
print(modelo_clasificacion.get_cpds())

# Realizar inferencias para clasificación
inferencia_clasificacion = VariableElimination(modelo_clasificacion)
resultado_clasificacion = inferencia_clasificacion.map_query(variables=['Diabetes'], evidence={'Nivel_Glucosa': 130, 'Presion_Sanguinea': 75})

print("Probabilidad de tener diabetes dado nivel de glucosa y presión sanguínea:")
print(resultado_clasificacion)
