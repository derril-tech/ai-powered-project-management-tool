# Repository Map

This document provides a comprehensive overview of the AI-Powered Project Management Tool repository structure.

## Root Structure

```
ai-powered-project-management-tool/
├── frontend/                 # Next.js 14 frontend application
├── backend/                  # FastAPI backend application
├── docs/                     # Documentation and guides
├── PROJECT_BRIEF.md         # Project requirements and specifications
├── PROMPT_DECLARATION.md    # AI collaboration guidelines
└── README.md                # Main project readme
```

## Frontend Structure (`frontend/`)

```
frontend/
├── src/
│   ├── app/                 # Next.js App Router pages
│   │   ├── layout.tsx       # Root layout component
│   │   ├── page.tsx         # Landing page
│   │   ├── dashboard/       # Dashboard pages
│   │   ├── projects/        # Project management pages
│   │   ├── tasks/           # Task management pages
│   │   └── globals.css      # Global styles
│   ├── components/          # Reusable React components
│   │   ├── ui/              # shadcn/ui components
│   │   ├── providers.tsx    # Context providers
│   │   └── _INSTRUCTIONS.md # Component development guidelines
│   ├── lib/                 # Utility functions and configurations
│   ├── hooks/               # Custom React hooks
│   ├── types/               # TypeScript type definitions
│   └── utils/               # Helper functions
├── public/                  # Static assets
├── package.json             # Frontend dependencies
├── tailwind.config.js       # Tailwind CSS configuration
├── tsconfig.json            # TypeScript configuration
└── next.config.js           # Next.js configuration
```

## Backend Structure (`backend/`)

```
backend/
├── app/
│   ├── api/                 # API endpoints
│   │   └── v1/              # API version 1
│   │       ├── api.py       # Main API router
│   │       └── endpoints/   # Individual endpoint modules
│   │           ├── projects.py
│   │           ├── tasks.py
│   │           ├── sprints.py
│   │           ├── users.py
│   │           ├── auth.py
│   │           ├── ai.py
│   │           └── automations.py
│   ├── core/                # Core application modules
│   │   ├── config.py        # Application settings
│   │   ├── database.py      # Database configuration
│   │   ├── redis.py         # Redis configuration
│   │   └── security.py      # Authentication and authorization
│   ├── models/              # SQLAlchemy database models
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── user.py
│   │   └── _INSTRUCTIONS.md # Model development guidelines
│   ├── schemas/             # Pydantic schemas for API
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── user.py
│   │   └── _INSTRUCTIONS.md # Schema development guidelines
│   ├── services/            # Business logic services
│   │   ├── ai/              # AI integration services
│   │   ├── automation/      # Automation engine
│   │   └── _INSTRUCTIONS.md # Service development guidelines
│   └── utils/               # Utility functions
├── alembic/                 # Database migrations
├── tests/                   # Test files
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
└── .env.example             # Environment variables template
```

## Documentation Structure (`docs/`)

```
docs/
├── REPO_MAP.md             # This file - repository structure guide
├── API_SPEC.md             # API specification and endpoints
├── CLAUDE.md               # AI collaboration guidelines
└── _INSTRUCTIONS.md        # Documentation guidelines
```

## Key Development Areas

### Frontend Development
- **Components**: Build reusable UI components in `frontend/src/components/`
- **Pages**: Create new pages in `frontend/src/app/` using App Router
- **Types**: Define TypeScript interfaces in `frontend/src/types/`
- **Hooks**: Create custom React hooks in `frontend/src/hooks/`

### Backend Development
- **Endpoints**: Add new API endpoints in `backend/app/api/v1/endpoints/`
- **Models**: Create database models in `backend/app/models/`
- **Schemas**: Define API schemas in `backend/app/schemas/`
- **Services**: Implement business logic in `backend/app/services/`

### AI Integration
- **LangGraph**: Implement AI workflows in `backend/app/services/ai/`
- **RAG**: Build retrieval-augmented generation in `backend/app/services/ai/rag/`
- **Automation**: Create automation rules in `backend/app/services/automation/`

## File Naming Conventions

- **Frontend**: Use kebab-case for files, PascalCase for components
- **Backend**: Use snake_case for Python files and functions
- **Database**: Use snake_case for table and column names
- **API**: Use kebab-case for endpoint URLs

## TODO Markers

Throughout the codebase, you'll find TODO markers indicating areas that need implementation:
- `# TODO: Implement...` - Backend implementation needed
- `// TODO: Implement...` - Frontend implementation needed
- `<!-- TODO: Implement... -->` - HTML/JSX implementation needed

## _INSTRUCTIONS.md Files

Each major directory contains an `_INSTRUCTIONS.md` file with specific guidelines for development in that area. These files provide:
- Coding conventions for that module
- Common patterns and examples
- Integration points with other modules
- Testing requirements
