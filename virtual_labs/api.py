from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class NewUser(BaseModel):
    username: str
    email: str

class User(NewUser):
    id: str 

class Budget(BaseModel):
    amount: float
    currency: str

class ResourceAllocation(BaseModel):
    amount: float
    unit: str

class ResourceAllocations(BaseModel):
    cpu: ResourceAllocation
    ram: ResourceAllocation


class ResourceUsage(BaseModel):
    amount: float
    unit: str
    since: datetime # TODO: Might not be needed

class ResourceUsages(BaseModel):
    cpu: ResourceUsage
    ram: ResourceUsage

class BaseVirtualLab(BaseModel):
    name: str
    description: str
    budget: Budget
    resource_allocation: ResourceAllocations

class NewVirtualLab(BaseVirtualLab):
    admins: list[int]
    users: list[int]

class UpdateVirtualLab(BaseModel):
    id: str
    name: str | None = None
    description: str | None = None
    budget: Budget | None = None

class VirtualLab(BaseVirtualLab):
    id: str
    admins: list[User]
    users: list[User]
    resource_usage: ResourceUsages
    created_at: datetime

class BaseProject(BaseModel):
    virtual_lab_id: str
    name: str
    description: str
    budget: Budget
    resource_allocation: list[ResourceAllocation]

class NewProject(BaseProject):
    admins: list[int]
    users: list[int]

class Project(BaseProject):
    id: str
    admins: list[User]
    users: list[User]
    resource_usage: list[ResourceUsage]
    created_at: datetime

class UpdateProject(BaseModel):
    name: str | None = None
    description: str | None = None
    budget: Budget | None = None

current_user = User(username="wonka", email="willy.wonka@chocolatefactory.ch", id = "2")

@app.post('/api/user')
async def create_user(new_user: NewUser) -> User:
    return User(id = 1, **new_user.model_dump())

@app.get('/api/virtual_lab')
async def get_all_virtual_labs() -> list[VirtualLab]:
    return

@app.get('/api/virtual_lab/{virtual_lab_id}')
async def get_virtual_lab(virtual_lab_id: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/resource_allocation/{resource_name}')
async def virtual_lab_update_resource_allocation(virtual_lab_id: str, resource_name: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/admin')
async def add_admin_to_virtual_lab(virtual_lab_id: str, admin_id: str) -> VirtualLab:
    return

@app.delete('/api/virtual_lab/{virtual_lab_id}/admin/{admin_id}')
async def remove_admin_from_virtual_lab(virtual_lab_id: str, admin_id: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/user')
async def add_user_to_virtual_lab(virtual_lab_id: str, user_id: str) -> VirtualLab:
    return

@app.delete('/api/virtual_lab/{virtual_lab_id}/user/{user_id}')
async def remove_user_from_virtual_lab(virtual_lab_id: str, user_id: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab')
async def create_virtual_lab(new_virtual_lab: NewVirtualLab) -> VirtualLab:
    # Add current user to admins
    return

@app.patch('/api/virtual_lab/{virtual_lab_id}')
async def update_virtual_lab(virtual_lab_id: str, modified_lab: VirtualLab) -> VirtualLab:
    # TODO: Authorization needed
    return

@app.delete('/api/virtual_lab/{virtual_lab_id}')
async def delete_virtual_lab(virtual_lab_id: str) -> VirtualLab:
    # TODO: Authorization needed
    return 

########### PROJECTS #############

@app.get('/api/virtual_lab/{virtual_lab_id}/project')
async def get_all_projects_for_virtual_lab(virtual_lab_id: str) -> list[Project]:
    return

@app.get('/api/virtual_lab/{virtual_lab_id}/project/{project_id}')
async def get_project_for_virtual_lab(virtual_lab_id: str, project_id: str) -> Project:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/project')
async def create_project(new_project: NewProject) -> Project:
    return

@app.patch('/api/virtual_lab/{virtual_lab_id}/project/{project_id}')
async def update_project(project_id: str, udpate_project: UpdateProject) -> Project:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/admin')
async def add_admin_to_project(project_id: str, admin_id: str) -> VirtualLab:
    return

@app.delete('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/admin/{admin_id}')
async def remove_admin_from_project(project_id: str, admin_id: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/user')
async def add_user_to_project(project_id: str, user_id: str) -> VirtualLab:
    return

@app.delete('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/user/{user_id}')
async def remove_user_from_project(project_id: str, user_id: str) -> VirtualLab:
    return

@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/resource_allocation/{resource_name}')
async def project_update_resource_allocation(project_id: str, resource_name: str) -> VirtualLab:
    # TODO: Add validation for the toal
    return


