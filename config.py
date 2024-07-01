import sys

DATABASE_PATH = "db/clientes.csv"
if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"

DELIMITER_FIELDS = ";"