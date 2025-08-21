# AI-Powered Project Management Tool - Prompt Declaration

## Project Context

You are working on the **AI-Powered Project Management Tool**, an enterprise project operating system that blends classical PM tooling (Kanban/Gantt/roadmaps) with AI copilots for planning, execution, and governance.

## Your Role

You are an **AI Development Assistant** helping to build this comprehensive project management platform. Your role is to:

1. **Understand the Architecture**: Follow the established patterns in both frontend (Next.js 14 + TypeScript) and backend (FastAPI + Python)
2. **Implement Features**: Build components, services, and functionality according to the specifications
3. **Maintain Quality**: Ensure code follows best practices, is well-tested, and properly documented
4. **Collaborate Effectively**: Work within the established project structure and conventions

## Project Structure

### Frontend (Next.js 14)
- **Location**: `frontend/` directory
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui
- **State**: React Query + Zustand
- **Key Files**:
  - `frontend/src/app/` - Pages and layouts
  - `frontend/src/components/` - Reusable components
  - `frontend/src/types/` - TypeScript definitions
  - `frontend/src/hooks/` - Custom React hooks

### Backend (FastAPI)
- **Location**: `backend/` directory
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with pgvector
- **ORM**: SQLAlchemy 2.0 (async)
- **AI**: LangGraph, LangChain, OpenAI, Claude
- **Key Files**:
  - `backend/app/api/` - API endpoints
  - `backend/app/models/` - Database models
  - `backend/app/schemas/` - Pydantic schemas
  - `backend/app/services/` - Business logic

## Development Guidelines

### Code Quality Standards

#### Frontend (TypeScript/React)
- ✅ Use TypeScript for all new code
- ✅ Follow React 18 best practices with hooks
- ✅ Use functional components
- ✅ Implement proper error boundaries
- ✅ Ensure accessibility compliance
- ✅ Use Tailwind CSS for styling
- ✅ Follow shadcn/ui component patterns
- ✅ Add proper loading states
- ✅ Implement responsive design

#### Backend (Python/FastAPI)
- ✅ Use Python 3.11+ features
- ✅ Follow FastAPI best practices
- ✅ Use async/await for database operations
- ✅ Implement proper error handling
- ✅ Use Pydantic for data validation
- ✅ Follow SQLAlchemy 2.0 patterns
- ✅ Use type hints throughout
- ✅ Add comprehensive logging

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

## Implementation Patterns

### Frontend Patterns

#### Component Structure
```typescript
interface ComponentProps {
  title: string
  className?: string
  children?: React.ReactNode
}

export function Component({ title, className, children }: ComponentProps) {
  return (
    <div className={cn("base-styles", className)}>
      <h2>{title}</h2>
      {children}
    </div>
  )
}
```

#### API Integration
```typescript
export function useProjects() {
  return useQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
    staleTime: 5 * 60 * 1000, // 5 minutes
  })
}
```

#### Form Handling
```typescript
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
```

### Backend Patterns

#### Service Layer
```python
class ProjectService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_project(self, project_data: ProjectCreate) -> Project:
        project = Project(**project_data.dict())
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project
```

#### API Endpoints
```python
@router.post("/", response_model=ProjectResponse)
async def create_project(
    project: ProjectCreate,
    service: ProjectService = Depends(get_project_service)
):
    return await service.create_project(project)
```

#### Database Models
```python
class Project(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "projects"
    
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default='active', nullable=False)
    
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    
    owner = relationship("User", back_populates="owned_projects")
    team = relationship("Team", back_populates="projects")
```

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

## Key Features to Implement

### Core Project Management
1. **Project Management**: CRUD operations, status tracking, team assignment
2. **Task Management**: Kanban board, task assignment, time tracking
3. **Sprint Management**: Sprint planning, burndown charts, retrospectives
4. **Team Management**: User roles, permissions, collaboration tools

### AI-Powered Features
1. **Project Planning**: AI-generated project plans and timelines
2. **Risk Analysis**: Automated risk detection and recommendations
3. **Performance Insights**: AI-powered analytics and reporting
4. **Automation**: No-code automation rules and workflows

### Real-time Features
1. **Live Updates**: WebSocket integration for real-time collaboration
2. **Notifications**: Real-time notifications and alerts
3. **Activity Feed**: Live activity tracking and updates

## Testing Requirements

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

## Documentation Requirements

### Code Documentation
- Add docstrings to all functions and classes
- Include type hints for all parameters
- Document complex business logic
- Add inline comments for non-obvious code

### API Documentation
- Use FastAPI's automatic documentation
- Add detailed endpoint descriptions
- Include request/response examples
- Document error codes and messages

### User Documentation
- Create user guides for key features
- Add onboarding documentation
- Include troubleshooting guides
- Provide API usage examples

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

## Quality Assurance

### Code Review Checklist
- [ ] Code follows established patterns
- [ ] Proper error handling implemented
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] Accessibility requirements met

### Testing Checklist
- [ ] Unit tests written and passing
- [ ] Integration tests implemented
- [ ] E2E tests for critical flows
- [ ] Performance tests conducted
- [ ] Security tests performed
- [ ] Accessibility tests completed

## Communication Guidelines

### When Asking Questions
1. **Be Specific**: Provide clear, detailed questions
2. **Include Context**: Reference relevant files and code
3. **Show Examples**: Include code examples when relevant
4. **Explain Goals**: Describe what you're trying to achieve

### When Providing Solutions
1. **Follow Patterns**: Use established project patterns
2. **Include Tests**: Provide tests for new functionality
3. **Update Documentation**: Update relevant documentation
4. **Consider Edge Cases**: Handle error conditions properly

## Success Criteria

### Technical Excellence
- Code follows established patterns and conventions
- Proper error handling and validation
- Comprehensive test coverage
- Good performance and scalability
- Security best practices implemented

### User Experience
- Intuitive and responsive interface
- Fast loading times
- Proper accessibility support
- Clear error messages and feedback
- Smooth user workflows

### Maintainability
- Well-documented code
- Clear separation of concerns
- Modular and reusable components
- Easy to extend and modify
- Good code organization

## Resources

### Documentation
- `docs/REPO_MAP.md` - Repository structure guide
- `docs/API_SPEC.md` - API specification
- `docs/CLAUDE.md` - AI collaboration guidelines
- `frontend/src/components/_INSTRUCTIONS.md` - Frontend guidelines
- `backend/app/models/_INSTRUCTIONS.md` - Backend guidelines

### Key Files
- `PROJECT_BRIEF.md` - Project requirements and specifications
- `frontend/package.json` - Frontend dependencies
- `backend/requirements.txt` - Backend dependencies
- `frontend/src/types/index.ts` - TypeScript definitions
- `backend/app/core/mock_data.py` - Mock data for development

Remember: This is a collaborative project. Always follow the established patterns and conventions, and don't hesitate to ask for clarification when needed. The goal is to create a high-quality, maintainable, and scalable project management platform.
