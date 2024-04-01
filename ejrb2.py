from pgmpy.models import BayesianNetwork 
from pgmpy.estimators import ParameterEstimator, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Crear un modelo bayesiano
model = BayesianNetwork ([('Horas_Estudio', 'Rendimiento'),
                       ('Participacion_Extra', 'Rendimiento'),
                       ('Tutorias', 'Rendimiento'),
                       ('Rendimiento', 'Aprobacion')])

# Crear un conjunto de datos de ejemplo más complejo
data_complejo = pd.DataFrame(data={'Horas_Estudio': [5, 2, 8, 3, 7],
                                   'Participacion_Extra': [1, 0, 1, 1, 0],
                                   'Tutorias': [0, 1, 0, 1, 1],
                                   'Rendimiento': [70, 50, 85, 60, 80],
                                   'Aprobacion': [1, 0, 1, 0, 1]})

# Aprender las probabilidades condicionales utilizando MaximumLikelihoodEstimator
model.fit(data_complejo, estimator=MaximumLikelihoodEstimator)

# Inferencia en el modelo
inference = VariableElimination(model)
result = inference.query(variables=['Aprobacion'], evidence={'Horas_Estudio': 7, 'Rendimiento': 80, 'Tutorias': 1})

print(result)
