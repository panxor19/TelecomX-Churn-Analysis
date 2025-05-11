📊 Análisis de Evasión de Clientes en una Empresa de Telecomunicaciones
Este proyecto tiene como objetivo identificar los factores que influyen en la cancelación del servicio (churn) por parte de los clientes en una empresa de telecomunicaciones. El análisis permite comprender mejor el comportamiento del cliente y diseñar estrategias efectivas para mejorar la retención.

🔍 Contenido
Introducción

Limpieza y Tratamiento de Datos

Análisis Exploratorio de Datos

Conclusiones e Insights

Recomendaciones

Tecnologías Utilizadas

Cómo Ejecutar el Proyecto

📌 Introducción
Se busca analizar un conjunto de datos para detectar qué variables están más asociadas a la evasión de clientes, con el fin de orientar estrategias comerciales e iniciativas de retención.

🧹 Limpieza y Tratamiento de Datos
Carga de datos desde una API pública en formato JSON.

Conversión a DataFrame de Pandas.

Renombrado de columnas (estilo snake_case).

Conversión de tipos (numérico y categórico).

Eliminación de duplicados.

Relleno de valores nulos (0 para numéricos, "desconocido" para categóricos).

Estandarización de valores textuales (Yes/No a 1/0).

Creación de variable cuentas_diarias como promedio mensual diario.

📊 Análisis Exploratorio de Datos
Estudio de la distribución general del churn.

Comparativa de churn según género, tipo de contrato y método de pago.

Análisis de antigüedad (tenure) y facturación mensual.

📈 Conclusiones e Insights
Mayor antigüedad está asociada a menor churn.

Contratos mensuales tienen mayor tasa de cancelación.

Ausencia de servicios técnicos o de streaming incrementa el churn.

Facturación baja puede reflejar desuso o insatisfacción.

💡 Recomendaciones
Incentivar contratos anuales mediante promociones.

Detectar bajo uso y ofrecer paquetes personalizados.

Promover el uso de pagos automáticos con beneficios.

Realizar campañas dirigidas en los primeros meses del cliente.

🛠️ Tecnologías Utilizadas
Python 3.x

Pandas

Matplotlib / Seaborn

Jupyter Notebook

API pública (formato JSON)

▶️ Cómo Ejecutar el Proyecto
Clonar este repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git

