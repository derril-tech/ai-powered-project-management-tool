# AI-Powered Project Management Tool - Backend

This is the backend API for the AI-Powered Project Management Tool, built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- **FastAPI**: Modern, fast web framework for building APIs
- **Async SQLAlchemy**: High-performance async database operations
- **PostgreSQL**: Robust relational database with pgvector for embeddings
- **Redis**: Caching, session storage, and real-time features
- **JWT Authentication**: Secure token-based authentication
- **AI Integration**: LangGraph, LangChain, OpenAI, and Claude integration
- **Real-time**: WebSocket support for live updates
- **Automation Engine**: No-code automation rules
- **File Storage**: S3-compatible file storage with antivirus scanning

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Database**: PostgreSQL + pgvector
- **Cache**: Redis
- **ORM**: SQLAlchemy 2.0 (async)
- **Authentication**: JWT
- **AI**: LangGraph, LangChain, OpenAI, Claude
- **File Storage**: S3/GCS
- **Testing**: pytest
- **Code Quality**: black, ruff, mypy

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- Docker (optional)

### Installation

1. Clone the repository
2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Copy environment variables:
   ```bash
   cp env.example .env
   ```

6. Update `.env` with your configuration:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/ai_project_management
   REDIS_URL=redis://localhost:6379
   SECRET_KEY=your-secret-key-here
   ```

### Database Setup

1. Create PostgreSQL database:
   ```sql
   CREATE DATABASE ai_project_management;
   ```

2. Install pgvector extension:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

3. Run database migrations:
   ```bash
   alembic upgrade head
   ```

### Development

Start the development server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000)

API documentation will be available at [http://localhost:8000/docs](http://localhost:8000/docs)

## Project Structure

```
app/
├── api/                    # API endpoints
│   └── v1/                # API version 1
│       ├── api.py         # Main API router
│       └── endpoints/     # Individual endpoint modules
├── core/                  # Core application modules
│   ├── config.py          # Application settings
│   ├── database.py        # Database configuration
│   └── redis.py           # Redis configuration
├── models/                # SQLAlchemy database models
├── schemas/               # Pydantic schemas
├── services/              # Business logic services
│   ├── ai/               # AI integration services
│   └── automation/       # Automation engine
└── utils/                # Utility functions
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - User logout

### Projects
- `GET /api/v1/projects` - List projects
- `POST /api/v1/projects` - Create project
- `GET /api/v1/projects/{id}` - Get project
- `PUT /api/v1/projects/{id}` - Update project
- `DELETE /api/v1/projects/{id}` - Delete project

### Tasks
- `GET /api/v1/tasks` - List tasks
- `POST /api/v1/tasks` - Create task
- `GET /api/v1/tasks/{id}` - Get task
- `PUT /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

### AI Integration
- `POST /api/v1/ai/plan` - Generate project plan
- `POST /api/v1/ai/analyze` - Analyze project health
- `POST /api/v1/ai/summarize` - Generate summaries

### Automations
- `GET /api/v1/automations` - List automations
- `POST /api/v1/automations` - Create automation
- `GET /api/v1/automations/{id}` - Get automation
- `PUT /api/v1/automations/{id}` - Update automation
- `DELETE /api/v1/automations/{id}` - Delete automation

## Available Scripts

- `uvicorn main:app --reload` - Start development server
- `pytest` - Run tests
- `black .` - Format code
- `ruff check .` - Lint code
- `mypy .` - Type checking
- `alembic upgrade head` - Run database migrations

## Environment Variables

See `env.example` for all available environment variables.

## Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migrations:
```bash
alembic downgrade -1
```

## Testing

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app
```

## Code Quality

Format code:
```bash
black .
```

Lint code:
```bash
ruff check .
```

Type checking:
```bash
mypy .
```

## Deployment

The application can be deployed to:
- Docker containers
- Cloud platforms (AWS, GCP, Azure)
- VPS or dedicated servers

## API Documentation

- Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## Support

For questions and support, please refer to the main project documentation.
