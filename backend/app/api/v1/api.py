from fastapi import APIRouter
from app.api.v1.endpoints import projects, tasks, sprints, users, auth, ai, automations

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(sprints.router, prefix="/sprints", tags=["sprints"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(automations.router, prefix="/automations", tags=["automations"])
