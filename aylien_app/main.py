from fastapi import FastAPI
from routes import countries_routes, custom_routes

app = FastAPI()

app.include_router(countries_routes.countries_router)
app.include_router(custom_routes.custom_search_router)
