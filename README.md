1. Angular frontend and FastApi backend with MySQL
2. User registration => Login
3. Create User
4. Create task and they can be mark as done
5. Task can be assigned to user
6. Create workflow
7. A workflow contains multiple task and task are sequential
8. Tasks in a workflow can be reordered
9. A workflow is done if all the tasks in that workflow is done



Relationships
- A User can be assigned multiple Tasks.
- A Task is assigned to one User.
- A Workflow contains multiple Tasks.
- A Task belongs to one Workflow.


Here are the possible API paths for your backend:

# User Registration and Login

POST /api/register
POST /api/login

# User Management

GET /api/users
GET /api/users/{user_id}
POST /api/users
PUT /api/users/{user_id}
DELETE /api/users/{user_id}

# Task Management

GET /api/tasks
GET /api/tasks/{task_id}
POST /api/tasks
PUT /api/tasks/{task_id}
DELETE /api/tasks/{task_id}
PUT /api/tasks/{task_id}/mark-done
PUT /api/tasks/{task_id}/assign-user/{user_id}

# Workflow Management

GET /api/workflows
GET /api/workflows/{workflow_id}
POST /api/workflows
PUT /api/workflows/{workflow_id}
DELETE /api/workflows/{workflow_id}
PUT /api/workflows/{workflow_id}/reorder-tasks
GET /api/workflows/{workflow_id}/check-completion