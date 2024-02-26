# Endpoints

## User

May not be needed depending on the 

- Create user
```
POST /api/user
```

## Virtual Lab

- Get all virtual labs for user
```
async def get_all_virtual_labs() -> list[VirtualLab]:
```
- Get virtual lab by id
```
async def get_virtual_lab(virtual_lab_id: str) -> VirtualLab:
```
- Create virtual lab
```
@app.post('/api/virtual_lab')
```
- Update virtual lab (including budget)
```
@app.patch('/api/virtual_lab/{virtual_lab_id}')
```
- Delete virtual lab
```
async def delete_virtual_lab(virtual_lab_id: str) -> VirtualLab:
```
- Add resource allocation to virtual lab
```
@app.post('/api/virtual_lab/{virtual_lab_id}/resource_allocation/{resource_name}')
```
- Add admin to virtual lab
```
@app.post('/api/virtual_lab/{virtual_lab_id}/admin')
```
- Delete admin from virtual lab
```
@app.delete('/api/virtual_lab/{virtual_lab_id}/admin/{admin_id}')
```
- Add user to virtual lab
```
@app.post('/api/virtual_lab/{virtual_lab_id}/user')
```
- Remove user from virtual lab
```
@app.delete('/api/virtual_lab/{virtual_lab_id}/user/{user_id}')
```

## Projects

- Get all projects for virtual lab
```
@app.get('/api/virtual_lab/{virtual_lab_id}/project')
```
- Get project by id
```
@app.get('/api/virtual_lab/{virtual_lab_id}/project/{project_id}')
```
- Create project
```
@app.post('/api/virtual_lab/{virtual_lab_id}/project')
```
- Update project
```
@app.patch('/api/virtual_lab/{virtual_lab_id}/project/{project_id}')
```
- Add admin to project
```
@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/admin')
```
- Remove admin from project
```
@app.delete('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/admin/{admin_id}')
```
- Add user to project
```
@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/user')
```
- Remove user from project
```
@app.delete('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/user/{user_id}')
```
- Update resource allocation for virtual lab
```
@app.post('/api/virtual_lab/{virtual_lab_id}/project/{project_id}/resource_allocation/{resource_name}')
```

# Development

1. Start the server
```
poetry run uvicorn virtual_labs.api:app --reload
```