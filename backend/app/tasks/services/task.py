from core.db import BaseDB
from ..models import task


class TaskService(BaseDB):
    
    async def create_task(self, item, id):
        print(id)
        new_task = task.insert().values(
            **item.dict(), column=id
        )
        task_id = await self.database.execute(new_task)
        return {"Created": True, "id": task_id}


    async def delete_task(self, id):
        t = task.delete().where(task.c.id == id)
        await self.database.execute(t)
        return {"Delete": True}

    async def update_task(self, item, id):
        t = task.update().where(task.c.id == id).values(**item.dict())
        await self.database.execute(t)
        return {"Update": True}
