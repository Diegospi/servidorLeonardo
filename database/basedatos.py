from sqlalchemy import create_engine,MetaData

motorBD=create_engine("mysql+pymysql://root@localhost:3366/leonadrodb")

metaDatos=MetaData()

conexion=motorBD.connect()