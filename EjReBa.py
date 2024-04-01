from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ParameterEstimator, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Crear un modelo bayesiano
model = BayesianNetwork([('Lluvia', 'Tarde'), ('Tráfico', 'Tarde')])

# Crear un conjunto de datos de ejemplo
data = pd.DataFrame(data={'Lluvia': [1, 0, 1, 0, 0],
                           'Tráfico': [1, 1, 0, 0, 1],
                           'Tarde': [1, 1, 1, 0, 1]})

# Aprender las probabilidades condicionales utilizando MaximumLikelihoodEstimator
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Inferencia en el modelo
inference = VariableElimination(model)
result = inference.query(variables=['Tarde'], evidence={'Lluvia': 1, 'Tráfico': 0})

print(model)
print(result)