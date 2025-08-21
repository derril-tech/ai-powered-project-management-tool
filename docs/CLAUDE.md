# Claude Collaboration Guidelines

This document provides comprehensive guidelines for AI collaboration on the AI-Powered Project Management Tool project.

## Project Overview

The AI-Powered Project Management Tool is an enterprise project operating system that blends classical PM tooling (Kanban/Gantt/roadmaps) with AI copilots for planning, execution, and governance. The goal is to create a unified source of truth for work, decisions, and context.

## Architecture Overview

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

## Development Guidelines

### Code Quality Standards

#### Frontend (TypeScript/React)
- Use TypeScript for all new code
- Follow React 18 best practices
- Use functional components with hooks
- Implement proper error boundaries
- Ensure accessibility compliance
- Use Tailwind CSS for styling
- Follow shadcn/ui component patterns

#### Backend (Python/FastAPI)
- Use Python 3.11+ features
- Follow FastAPI best practices
- Use async/await for database operations
- Implement proper error handling
- Use Pydantic for data validation
- Follow SQLAlchemy 2.0 patterns
- Use type hints throughout

### File Structure Conventions

#### Frontend
```
frontend/src/
├── app/                    # Next.js App Router pages
├── components/            # Reusable React components
│   ├── ui/               # shadcn/ui base components
│   ├── layout/           # Layout components
│   ├── forms/            # Form components
│   └── charts/           # Data visualization
├── hooks/                # Custom React hooks
├── lib/                  # Utility functions
├── types/                # TypeScript definitions
└── utils/                # Helper functions
```

#### Backend
```
backend/app/
├── api/                  # API endpoints
│   └── v1/              # API version 1
├── core/                 # Core application modules
├── models/               # SQLAlchemy database models
├── schemas/              # Pydantic schemas
├── services/             # Business logic services
│   ├── ai/              # AI integration services
│   └── automation/      # Automation engine
└── utils/                # Utility functions
```

### Naming Conventions

#### Frontend
- **Files**: kebab-case (`user-profile.tsx`)
- **Components**: PascalCase (`UserProfile`)
- **Hooks**: camelCase with `use` prefix (`useUserData`)
- **Types**: PascalCase (`UserProfileProps`)

#### Backend
- **Files**: snake_case (`user_profile.py`)
- **Classes**: PascalCase (`UserProfile`)
- **Functions**: snake_case (`get_user_profile`)
- **Variables**: snake_case (`user_profile`)

## AI Integration Guidelines

### LangGraph Workflows
- Create workflows in `backend/app/services/ai/workflows/`
- Use proper state management
- Implement error handling and retries
- Add logging for debugging
- Use human-in-the-loop approvals where needed

### RAG Implementation
- Store embeddings in PostgreSQL with pgvector
- Implement proper chunking strategies
- Use semantic search for retrieval
- Add citation tracking
- Implement confidence scoring

### Prompt Engineering
- Store prompts as code in `backend/app/services/ai/prompts/`
- Use version control for prompt changes
- Implement A/B testing for prompts
- Add prompt validation
- Use structured output formats

## Database Guidelines

### Model Design
- Use UUIDs for primary keys
- Implement soft deletes where appropriate
- Add proper indexes for performance
- Use foreign key constraints
- Implement audit logging

### Migration Strategy
- Use Alembic for migrations
- Test migrations on development data
- Include rollback instructions
- Use descriptive migration names
- Review auto-generated migrations

## API Design Guidelines

### RESTful Endpoints
- Use proper HTTP methods (GET, POST, PUT, DELETE)
- Implement consistent error responses
- Add proper status codes
- Use pagination for list endpoints
- Implement filtering and sorting

### Authentication & Authorization
- Use JWT tokens for authentication
- Implement role-based access control
- Add proper token refresh
- Implement rate limiting
- Use secure password hashing

## Testing Guidelines

### Frontend Testing
- Unit tests for components
- Integration tests for pages
- E2E tests for critical flows
- Accessibility testing
- Performance testing

### Backend Testing
- Unit tests for services
- Integration tests for API endpoints
- Database migration tests
- Performance testing
- Security testing

## Deployment Guidelines

### Frontend Deployment
- Use Vercel for production
- Implement proper environment variables
- Add build optimization
- Implement CDN for static assets
- Add monitoring and analytics

### Backend Deployment
- Use Docker containers
- Implement health checks
- Add proper logging
- Use environment-specific configs
- Implement auto-scaling

## Security Guidelines

### Data Protection
- Encrypt sensitive data at rest
- Use HTTPS for all communications
- Implement proper input validation
- Add SQL injection protection
- Use secure session management

### Access Control
- Implement proper authentication
- Use role-based permissions
- Add audit logging
- Implement rate limiting
- Use secure API keys

## Performance Guidelines

### Frontend Performance
- Implement code splitting
- Use lazy loading for components
- Optimize bundle size
- Implement caching strategies
- Add performance monitoring

### Backend Performance
- Use database connection pooling
- Implement caching with Redis
- Add proper indexing
- Use async operations
- Monitor response times

## Monitoring & Observability

### Logging
- Use structured logging
- Add correlation IDs
- Implement log levels
- Add request/response logging
- Use centralized logging

### Metrics
- Track API response times
- Monitor database performance
- Add business metrics
- Implement alerting
- Use dashboards for visualization

## Common Patterns

### Frontend Patterns
```typescript
// Custom hook for API calls
export function useProjects() {
  return useQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
    staleTime: 5 * 60 * 1000, // 5 minutes
  })
}

// Form with validation
export function ProjectForm() {
  const form = useForm({
    resolver: zodResolver(projectSchema),
  })
  
  return (
    <Form {...form}>
      <FormField
        control={form.control}
        name="name"
        render={({ field }) => (
          <FormItem>
            <FormLabel>Project Name</FormLabel>
            <FormControl>
              <Input {...field} />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
    </Form>
  )
}
```

### Backend Patterns
```python
# Service layer pattern
class ProjectService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_project(self, project_data: ProjectCreate) -> Project:
        project = Project(**project_data.dict())
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project

# Dependency injection
async def get_project_service(db: AsyncSession = Depends(get_db)) -> ProjectService:
    return ProjectService(db)

# API endpoint
@router.post("/", response_model=ProjectResponse)
async def create_project(
    project: ProjectCreate,
    service: ProjectService = Depends(get_project_service)
):
    return await service.create_project(project)
```

## Troubleshooting Guide

### Common Issues

#### Frontend Issues
- **Build errors**: Check TypeScript types and imports
- **Runtime errors**: Check browser console and React DevTools
- **Styling issues**: Verify Tailwind classes and CSS variables
- **Performance issues**: Use React DevTools Profiler

#### Backend Issues
- **Database errors**: Check connection strings and migrations
- **API errors**: Check FastAPI logs and response codes
- **Authentication issues**: Verify JWT tokens and permissions
- **Performance issues**: Check database queries and Redis

### Debugging Tools
- **Frontend**: React DevTools, browser dev tools
- **Backend**: FastAPI docs, database logs, Redis CLI
- **Database**: pgAdmin, database logs
- **Monitoring**: Application logs, metrics dashboards

## Best Practices

### Code Organization
- Keep components small and focused
- Use proper separation of concerns
- Implement consistent error handling
- Add comprehensive documentation
- Use meaningful variable names

### Performance
- Implement proper caching strategies
- Use database indexes effectively
- Optimize bundle sizes
- Implement lazy loading
- Monitor performance metrics

### Security
- Validate all inputs
- Use secure authentication
- Implement proper authorization
- Encrypt sensitive data
- Follow security best practices

### Testing
- Write tests for critical functionality
- Use proper test data
- Implement CI/CD pipelines
- Add automated testing
- Monitor test coverage

## Resources

### Documentation
- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com/)

### Tools
- **Frontend**: VS Code, React DevTools, Tailwind CSS IntelliSense
- **Backend**: PyCharm, FastAPI docs, pgAdmin
- **Database**: PostgreSQL, Redis CLI
- **Testing**: Jest, Playwright, pytest
- **Deployment**: Vercel, Docker, GitHub Actions

## Contact & Support

For questions about this project:
1. Check the documentation in the `docs/` folder
2. Review the code examples in the repository
3. Check the `_INSTRUCTIONS.md` files in each directory
4. Refer to the API specification in `docs/API_SPEC.md`
5. Review the repository structure in `docs/REPO_MAP.md`

Remember: This is a collaborative project. Always follow the established patterns and conventions, and don't hesitate to ask for clarification when needed.
