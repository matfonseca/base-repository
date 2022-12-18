from fastapi import FastAPI

from .routers import users, state, teams, profiles, notifications, projects
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(state.router)
app.include_router(teams.router)
app.include_router(profiles.router)
app.include_router(notifications.router)
app.include_router(projects.router)
