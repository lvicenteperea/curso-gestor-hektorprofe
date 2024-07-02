from pymongo import MongoClient

#Base de datos LOCAL
db_connect = MongoClient().CursoGestorHektor ## sin nada se conecta a mongo en local

# Bases de dato remota al mongoAtlas (mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/)
#db_connect = MongoClient("mongodb+srv://test:test@atlascluster.iovqvw0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
#                       ).test