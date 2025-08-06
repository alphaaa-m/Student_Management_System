from fastapi import FastAPI
from app.database.db import engine
from app.routes import usr_route, std_route, crs_route, enr_route
from app.models import usr, std, crs, enr


app = FastAPI(
                title="Student Management System",
                description="""Welcome to **SMS**..!""",
                version="1.0.0",
                license_info={"name": "Muneeb Ashraf"})



@app.get("/")
def home():
    return {"message": "Welcome to the Student Management System API"}


app.include_router(usr_route.router)
app.include_router(std_route.router)
app.include_router(crs_route.router)
app.include_router(enr_route.router)