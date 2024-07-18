from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from models.chatbot import chat
from database.basedatos import conexion

rutas=APIRouter()

@rutas.get("/leonardo")
def consultarChat():
    try:
        consulta=select(chat)
        resultado=conexion.execute(consulta).fetchall()
        resultadoJSON=[{"id":row.id,"pregunta":row.pregunta,"respuesta":row.pregunta} for row in resultado]
        return resultadoJSON

    except Exception as error:
        raise HTTPException(status_code=500,detail=str(error))
