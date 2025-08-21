from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_sprints(
    project_id: str = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve all sprints for a project.
    """
    # TODO: Implement sprint retrieval logic
    return []


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_sprint(
    sprint_data: dict,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new sprint.
    """
    # TODO: Implement sprint creation logic
    return {"id": "placeholder", "name": sprint_data.get("name")}


@router.get("/{sprint_id}")
async def get_sprint(
    sprint_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve a specific sprint.
    """
    # TODO: Implement sprint retrieval logic
    raise HTTPException(status_code=404, detail="Sprint not found")


@router.put("/{sprint_id}")
async def update_sprint(
    sprint_id: str,
    sprint_data: dict,
    db: AsyncSession = Depends(get_db)
):
    """
    Update a sprint.
    """
    # TODO: Implement sprint update logic
    raise HTTPException(status_code=404, detail="Sprint not found")
