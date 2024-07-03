import sys

# URL de la aplicación
URL = "http://127.0.0.1:8000/"

# cuando se utilizan los APIs con ejemplos de BBDD:
#   - LOCAL tira la una BBDD local 
#   - culquier otro valor, tira de una BBDD en la nube de Mongo
DATABASE_lOCALIZA = "mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster" 
#DATABASE_lOCALIZA = None

# Esto es para los ejemplos con datos en un fichero CSV
DATABASE_PATH = "db/clientes.csv"
if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"
DELIMITER_FIELDS = ";"