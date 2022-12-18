from fastapi import APIRouter
from app import config
from app.services import Services

router = APIRouter()


@router.post("/projects/", tags=["projects"], status_code=201)
async def create_project(body: dict):
    url = config.PROJECT_SERVICE_URL
    resource = "projects/"
    params = {}
    return Services.post(url, resource, params, body)


@router.get("/projects/", tags=["projects"])
async def list_projects(creator_uid: str = None):
    url = config.PROJECT_SERVICE_URL
    resource = "projects/"
    params = {}
    if creator_uid is not None:
        params["creator_uid"] = creator_uid
    return Services.get(url, resource, params)


@router.get("/projects/{pid}", tags=["projects"])
async def read_project(pid: str):
    url = config.PROJECT_SERVICE_URL
    resource = f"projects/{pid}"
    params = {}
    return Services.get(url, resource, params)
