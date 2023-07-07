# -*- coding: utf-8 -*-
"""
Parámetros para la ejecución

@author: rafle
"""
### Máxima cantidad de entidades a barrer (en función de que tan grande es la base plana)

## Máxima cantidad de hogares
Max_veh = 4
## Máxima cantidad de personas
Max_per = 8
## Máxima cantidad de viajes
Max_via = 12

## Columnas a selecionar por módulo

hogares = [
    "Result Id",
    "Device Name",
    "Q1. Fecha de la encuesta?",
    "Q1. Hora de la encuesta?",
    "Q3. Nombre:",
    "Q4. Municipio?",
    "Q5. Barrio?",
    "Q6. UCG?",
    "Q7. Manzana?",
    "Q8. Dirección",
    "Q9. Teléfono fíjo",
    "Q10. Teléfono móvil",
    "Q12. Estrato de la vivienda?",
    "Q13. Número de hogares residentes\nCuántas familias viven en este hogar?",
    "Q14. Número de personas residentes?",
    "Q15. Régimen de propiedad",
    "Q16. Ingresos mensuales del hogar"
    ]

personas = [
    ('Q22.(',') Genero?'),
    ('Q23.(',') Edad'),
    ('Q24.(',') Nivel de estudios'),
    ('Q25.(',') Principal ocupación'),
    ('Q26.(',') Presente en la entrevista?'),
    ('Q28.(',') En qué sector económico trabaja?'),
    ('Q29.(',') Dirección lugar de actividad principal'),
    ('Q31.(',') Tiene dificultades funcionales'),
    ('Q32.(',') Licencia de conducción:\nAutomovil'),
    ('Q33.(',') Licencia de conducción:\nMoto'),
    ('Q34.(',') ¿Ha salido de la casa el día anterior?')
    ]

vehiculos = [
    ('Q17.(', ') Tipo de vehículo'),
    ('Q18.(', ') Propiedad del vehículo'),
    ('Q19.(', ') Matriculado en?'),
    ('Q20.(', ') Tipo de estacionamiento?')]

viajes = [
    #('Q36.(',') Desea registrar un viaje?'),
    ('Q37.(',') Número de residente'),
    ('Q38.(',') Número de viaje'),
    ('Q39.(',') Frecuencia de viaje'),
    ('Q40.(',') Motivo del viaje'),
    ('Q41.(',') Hora de salida'),
    ('Q42.(',') Origen del viaje:\nMunicipio'),
    ('Q43.(',') Origen del viaje:\nUbicación (barrio)'),
    ('Q44.(',') Origen del viaje:\nHito'),
    ('Q45.(',') Hora de llegada'),
    ('Q46.(',') Destino del viaje:\nMunicipio'),
    ('Q47.(',') Destino del viaje:\nUbicación (barrio)'),
    ('Q48.(',') Destino del viaje:\nHito'),
    ('Q49.(',') Etapa 1:\nTiempo de acceso a pié'),
    ('Q50.(',') Etapa 1:\nMedio de transporte'),
    ('Q51.(',') Etapa 1:\nTiempo de espera'),
    ('Q52.(',') Etapa 1:\nTiempo de viaje'),
    ('Q53.(',') Etapa 1:\nTiempo de finalización a pié'),
    #('Q54.(',''),
    ('Q55.(',') Etapa 2:\nTiempo de acceso a pié'),
    ('Q56.(',') Etapa 2:\nMedio de transporte'),
    ('Q57.(',') Etapa 2:\nTiempo de espera'),
    ('Q58.(',') Etapa 2:\nTiempo de viaje'),
    ('Q59.(',') Etapa 2:\nTiempo de finalización a pié'),
    #('Q60.(',''),
    ('Q61.(',') Etapa 3:\nTiempo de acceso a pié'),
    ('Q62.(',') Etapa 3:\nMedio de transporte'),
    ('Q63.(',') Etapa 3:\nTiempo de espera'),
    ('Q64.(',') Etapa 3:\nTiempo de viaje'),
    ('Q65.(',') Etapa 3:\nTiempo de finalización a pié'),
    #('Q66.(',''),
    ('Q67.(',') Etapa 4:\nTiempo de acceso a pié'),
    ('Q68.(',') Etapa 4:\nMedio de transporte'),
    ('Q69.(',') Etapa 4:\nTiempo de espera'),
    ('Q70.(',') Etapa 4:\nTiempo de viaje'),
    ('Q71.(',') Etapa 4:\nTiempo de finalización a pié'),
    #('Q72.(',''),
    ('Q73.(',') Etapa 5:\nTiempo de acceso a pié'),
    ('Q74.(',') Etapa 5:\nMedio de transporte'),
    ('Q75.(',') Etapa 5:\nTiempo de espera'),
    ('Q76.(',') Etapa 5:\nTiempo de viaje'),
    ('Q77.(',') Etapa 5:\nTiempo de finalización a pié'),
    ('Q78.(',') Trayecto en transporte particular?'),
    ('Q79.(',') Número de ocupantes en transporte particular'),
    ('Q80.(',') Costo del estacionamiento'),
    ('Q81.(',') Tipo de estacionamiento')]
