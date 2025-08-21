# AI-Powered Project Management Tool

An enterprise project operating system that blends classical PM tooling (Kanban/Gantt/roadmaps) with AI copilots for planning, execution, and governance.

## 🚀 Features

### Core Project Management
- **Project Management**: CRUD operations, status tracking, team assignment
- **Task Management**: Kanban board, task assignment, time tracking
- **Sprint Management**: Sprint planning, burndown charts, retrospectives
- **Team Management**: User roles, permissions, collaboration tools

### AI-Powered Features
- **Project Planning**: AI-generated project plans and timelines
- **Risk Analysis**: Automated risk detection and recommendations
- **Performance Insights**: AI-powered analytics and reporting
- **Automation**: No-code automation rules and workflows

### Real-time Features
- **Live Updates**: WebSocket integration for real-time collaboration
- **Notifications**: Real-time notifications and alerts
- **Activity Feed**: Live activity tracking and updates

## 🏗️ Architecture

### Frontend (Next.js 14)
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui
- **State Management**: React Query + Zustand
- **Real-time**: WebSocket integration
- **Key Features**: SSR/ISR, dark mode, responsive design

### Backend (FastAPI)
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with pgvector for embeddings
- **ORM**: SQLAlchemy 2.0 (async)
- **Cache**: Redis
- **AI Integration**: LangGraph, LangChain, OpenAI, Claude
- **Authentication**: JWT
- **Real-time**: WebSocket support

## 📁 Project Structure

```
ai-powered-project-management-tool/
├── frontend/                 # Next.js 14 frontend application
│   ├── src/
│   │   ├── app/             # Next.js App Router pages
│   │   ├── components/      # Reusable React components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── lib/             # Utility functions
│   │   ├── types/           # TypeScript definitions
│   │   └── utils/           # Helper functions
│   ├── package.json         # Frontend dependencies
│   └── README_FRONTEND.md   # Frontend documentation
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── api/             # API endpoints
│   │   ├── core/            # Core application modules
│   │   ├── models/          # SQLAlchemy database models
│   │   ├── schemas/         # Pydantic schemas
│   │   └── services/        # Business logic services
│   ├── requirements.txt     # Backend dependencies
│   └── README_BACKEND.md    # Backend documentation
├── docs/                     # Documentation and guides
│   ├── REPO_MAP.md          # Repository structure guide
│   ├── API_SPEC.md          # API specification
│   └── CLAUDE.md            # AI collaboration guidelines
├── PROJECT_BRIEF.md         # Project requirements and specifications
├── PROMPT_DECLARATION.md    # AI collaboration guidelines
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Redis 6+

### Frontend Setup
```bash
cd frontend
npm install
cp env.example .env.local
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# Update .env with your configuration
uvicorn main:app --reload
```

### Database Setup
```sql
CREATE DATABASE ai_project_management;
CREATE EXTENSION IF NOT EXISTS vector;
```

## 📚 Documentation

- **[Project Brief](PROJECT_BRIEF.md)** - Detailed project requirements and specifications
- **[Repository Map](docs/REPO_MAP.md)** - Complete repository structure guide
- **[API Specification](docs/API_SPEC.md)** - Comprehensive API documentation
- **[AI Guidelines](docs/CLAUDE.md)** - AI collaboration guidelines
- **[Frontend README](frontend/README_FRONTEND.md)** - Frontend-specific documentation
- **[Backend README](backend/README_BACKEND.md)** - Backend-specific documentation

## 🛠️ Development

### Code Quality
- **Frontend**: TypeScript, ESLint, Prettier
- **Backend**: Black, Ruff, MyPy
- **Testing**: Jest, Playwright, pytest
- **Documentation**: Comprehensive inline and external docs

### Key Development Files
- `frontend/src/components/_INSTRUCTIONS.md` - Frontend development guidelines
- `backend/app/models/_INSTRUCTIONS.md` - Backend development guidelines
- `PROMPT_DECLARATION.md` - AI collaboration guidelines

### Environment Variables
- **Frontend**: See `frontend/env.example`
- **Backend**: See `backend/env.example`

## 🔧 Configuration

### Frontend Environment Variables
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
NEXT_PUBLIC_ENABLE_AI_FEATURES=true
```

### Backend Environment Variables
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/ai_project_management
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm run test
npm run test:e2e
```

### Backend Testing
```bash
cd backend
pytest
pytest --cov=app
```

## 🚀 Deployment

### Frontend Deployment
- **Platform**: Vercel (recommended)
- **Build Command**: `npm run build`
- **Output Directory**: `.next`

### Backend Deployment
- **Platform**: Docker, Cloud platforms (AWS, GCP, Azure)
- **Docker**: Use provided Dockerfile
- **Environment**: Set all required environment variables

## 🤝 Contributing

1. Follow the established patterns and conventions
2. Use TypeScript for frontend, Python for backend
3. Add tests for new functionality
4. Update documentation as needed
5. Follow the guidelines in `PROMPT_DECLARATION.md`

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions and support:
1. Check the documentation in the `docs/` folder
2. Review the `_INSTRUCTIONS.md` files in each directory
3. Refer to the API specification in `docs/API_SPEC.md`
4. Check the repository structure in `docs/REPO_MAP.md`

## 🎯 Roadmap

### Phase 1: Core Infrastructure ✅
- [x] Project setup and scaffolding
- [x] Basic frontend and backend structure
- [x] Database models and schemas
- [x] API endpoints and documentation
- [x] AI integration foundation

### Phase 2: Core Features 🚧
- [ ] User authentication and authorization
- [ ] Project and task management
- [ ] Team collaboration features
- [ ] Real-time updates and notifications

### Phase 3: AI Features 🚧
- [ ] AI-powered project planning
- [ ] Risk analysis and recommendations
- [ ] Performance insights and analytics
- [ ] Automation workflows

### Phase 4: Advanced Features 📋
- [ ] Gantt charts and timeline views
- [ ] Advanced reporting and analytics
- [ ] Integration with external tools
- [ ] Mobile application

---

**Built with ❤️ using Next.js, FastAPI, and AI technologies**