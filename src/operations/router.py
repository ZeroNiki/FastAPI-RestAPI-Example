"""
Router file for API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from typing import List

from .models import task
from .manager import TaskCreate, TaskUpdate
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
    query = insert(task).values(
        title=task_create.title,
        description=task_create.description,
        done=task_create.done,
        created_at=task_create.created_at
    )

    await db.execute(query)
    await db.commit()

    return {"message": "Task created successfully"}


@router.get("/task/{id}", response_model=dict)
async def get_task(id: int, db: AsyncSession = Depends(get_db)):
    query = task.select().where(task.c.id.ilike(f"%{id}%"))
    res = await db.execute(query)
    data = res.fetchone()

    if data is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": data[0],
        "title": data[1],
        "description": data[2],
        "done": data[3],
        "created_at": data[4]
    }


@router.delete("/delete/{id}")
async def delete_data(id: int, db: AsyncSession = Depends(get_db)):
    query = task.select().where(task.c.id.ilike(f"%{id}%"))
    res = await db.execute(query)
    exist = res.fetchone()

    if not exist:
        raise HTTPException(status_code=404, detail="Task not found")

    delete_query = task.delete().where(task.c.id.ilike(f"%{id}%"))
    await db.execute(delete_query)
    await db.commit()

    return {"Message": "Task delete successfully"}


@router.put("/update/{id}")
async def update_data(task_upd: TaskUpdate,
                      id: int, db: AsyncSession = Depends(get_db)):
    query = task.select().where(task.c.id.ilike(f"%{id}%"))
    res = await db.execute(query)

    data = res.fetchone()
    if not data:
        raise HTTPException(status_code=404, detail="Task not found")

    upd_data = task_upd.dict(exclude_unset=True)
    if not upd_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    upd_query = task.update().where(
        task.c.id.ilike(f"%{id}%")).values(upd_data)

    await db.execute(upd_query)
    await db.commit()

    return {"Message": "Task update successfully"}
