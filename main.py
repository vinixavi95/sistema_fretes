from fastapi import FastAPI, HTTPException
from src.routes.freteRoutes import router as freteRoutes
from src.routes.usuarioRoute import router as usuarioRoute
from src.routes.relatoriosRoute import router as relatorioRoute

app = FastAPI(
    title='Sistema de fretes',
    version='1.0.0'
)

app.include_router(freteRoutes)
app.include_router(usuarioRoute)
app.include_router(relatorioRoute)