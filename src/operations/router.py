import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from typing import Optional, List

from .models import task
from .manager import TaskCreate
from .utils import get_db

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)


@router.get("/data", response_model=List[dict])
async def get_all(db: AsyncSession = Depends(get_db)):
    query = select(
        task.c.id,
        task.c.title,
        task.c.description,
        task.c.done,
        task.c.created_at
    )

    result = await db.execute(query)
    data = result.fetchall()

    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "done": row[3],
        "created_at": row[4]
    } for row in data]


@router.post("/add")
async def add_data(task_create: TaskCreate,
                   db: AsyncSession = Depends(get_db)):
    # created_at = datetime.date.fromisoformat(str(task_create.created_at))
    query = insert(task).values(
        title=task_create.title,
        description=task_create.description,
        done=task_create.done,
        created_at=task_create.created_at
    )

    await db.execute(query)
    await db.commit()

    return {"message": "Task created successfully"}
