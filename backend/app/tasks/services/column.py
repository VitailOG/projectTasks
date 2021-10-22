from core.db import BaseDB
from sqlalchemy import select
from ..models import column_task, task


class ColomnService(BaseDB):

    @staticmethod
    async def get_correct_json(qs):
        n = []
        e = {}
        for i in qs:
            if i[0] not in e:
                tasks = [{"id": i[3], "text": i[4]}] if i[3] is not None else []
                n.append({'id': i[0], "title": i[1], "project": i[2], "tasks": tasks})
                e[i[0]] = len(n)
            else:
                index = e[i[0]] - 1
                n[index]['tasks'].append({"id": i[3], "text": i[4]})
        return n

    
    async def get_columns(self, id):
        query = select(column_task, task.c.id, task.c.text)\
            .select_from(column_task.outerjoin(task))\
            .where((column_task.c.project == id) | (column_task.c.id == task.c.column))
        columns = await self.database.fetch_all(query)
        return await self.get_correct_json(columns)


    async def create_columns(self, item: column_task, id):
        new_column = column_task.insert().values(
            **item.dict(), project=id
        )
        column_id = await self.database.execute(new_column)
        return {"Created": True, "id": column_id}


    async def update_columns(self, item: column_task, id: int):
        p = column_task.update().where(column_task.c.id == id).values(**item.dict())
        await self.database.execute(p)
        return {"update": True}


    async def delete_columns(self, id):
        c = column_task.delete().where(column_task.c.id == id)
        await self.database.execute(c)
        return {"Delete": True}
