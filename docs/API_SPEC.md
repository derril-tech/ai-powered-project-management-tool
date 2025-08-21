# API Specification

This document defines the API endpoints for the AI-Powered Project Management Tool.

## Base URL

- **Development**: `http://localhost:8000/api/v1`
- **Production**: `https://api.example.com/api/v1`

## Authentication

All API endpoints require authentication via JWT tokens, except for `/auth/login` and `/auth/register`.

### Headers
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

## Endpoints

### Authentication

#### POST /auth/login
Authenticate user and return JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### POST /auth/register
Register a new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "team_name": "My Team"
}
```

### Projects

#### GET /projects
Retrieve all projects with pagination.

**Query Parameters:**
- `skip` (int): Number of records to skip (default: 0)
- `limit` (int): Maximum number of records to return (default: 100)
- `status` (string): Filter by project status
- `team_id` (string): Filter by team ID

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "Project Name",
    "description": "Project description",
    "status": "active",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "owner_id": "uuid",
    "team_id": "uuid"
  }
]
```

#### POST /projects
Create a new project.

**Request Body:**
```json
{
  "name": "Project Name",
  "description": "Project description"
}
```

#### GET /projects/{project_id}
Retrieve a specific project.

#### PUT /projects/{project_id}
Update a project.

#### DELETE /projects/{project_id}
Delete a project.

### Tasks

#### GET /tasks
Retrieve all tasks with filtering and pagination.

**Query Parameters:**
- `project_id` (string): Filter by project ID
- `assignee_id` (string): Filter by assignee
- `status` (string): Filter by task status
- `priority` (string): Filter by priority level

#### POST /tasks
Create a new task.

**Request Body:**
```json
{
  "title": "Task Title",
  "description": "Task description",
  "project_id": "uuid",
  "assignee_id": "uuid",
  "priority": "medium",
  "estimated_hours": 8,
  "due_date": "2024-01-15T00:00:00Z"
}
```

#### GET /tasks/{task_id}
Retrieve a specific task.

#### PUT /tasks/{task_id}
Update a task.

#### DELETE /tasks/{task_id}
Delete a task.

### Sprints

#### GET /sprints
Retrieve all sprints for a project.

#### POST /sprints
Create a new sprint.

#### GET /sprints/{sprint_id}
Retrieve a specific sprint.

#### PUT /sprints/{sprint_id}
Update a sprint.

### AI Integration

#### POST /ai/plan
Generate project plan using AI.

**Request Body:**
```json
{
  "project_id": "uuid",
  "description": "Natural language project description",
  "constraints": ["budget", "timeline", "team_size"]
}
```

#### POST /ai/analyze
Analyze project health and risks.

#### POST /ai/summarize
Generate standup summaries.

### Automations

#### GET /automations
Retrieve all automations.

#### POST /automations
Create a new automation rule.

**Request Body:**
```json
{
  "name": "Auto-assign high priority tasks",
  "description": "Automatically assign high priority tasks to team lead",
  "trigger": {
    "type": "task_created",
    "config": {}
  },
  "conditions": [
    {
      "field": "priority",
      "operator": "equals",
      "value": "high"
    }
  ],
  "actions": [
    {
      "type": "assign_task",
      "config": {
        "assignee_id": "team_lead_uuid"
      }
    }
  ]
}
```

## Error Responses

All endpoints return consistent error responses:

```json
{
  "detail": "Error message",
  "error_code": "ERROR_CODE",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Common HTTP Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

## Rate Limiting

- **Authenticated requests**: 1000 requests per hour
- **Unauthenticated requests**: 100 requests per hour

## WebSocket Endpoints

### /ws/projects/{project_id}
Real-time updates for project changes.

**Events:**
- `task_created`
- `task_updated`
- `task_deleted`
- `sprint_started`
- `sprint_completed`

## Pagination

All list endpoints support pagination with the following response format:

```json
{
  "items": [...],
  "total": 100,
  "page": 1,
  "size": 20,
  "pages": 5
}
```
