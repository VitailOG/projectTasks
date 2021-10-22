from core.db import BaseDB
from .models import project


class ProjectService(BaseDB):

    async def create_project(self, item, id: int):
        new_project = project.insert().values(
            **item.dict(), admin=id
        )
        project_id = await self.database.execute(new_project)
        return {"success": True, 'id': project_id}

    async def update_project(self, item: project, id):
        p = project.update() \
                   .where(project.c.id == id)\
                   .values(**item.dict())
        await self.database.execute(p)

    async def delete_project(self, id: int):
        _project = project.delete().where(project.c.id == id)
        await self.database.execute(_project)
        return {"delete": True}

    
    async def list_user_project(self, id):
        query = project.select().where(project.c.admin == id)
        user_projects = await self.database.fetch_all(query)
        return user_projects
    