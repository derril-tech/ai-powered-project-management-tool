# Frontend Components Development Guidelines

## Overview

This directory contains all reusable React components for the AI-Powered Project Management Tool frontend.

## Directory Structure

```
components/
├── ui/                    # shadcn/ui base components
├── providers.tsx          # Context providers (React Query, etc.)
├── layout/               # Layout components (Header, Sidebar, etc.)
├── forms/                # Form components
├── charts/               # Data visualization components
├── kanban/               # Kanban board components
├── gantt/                # Gantt chart components
└── ai/                   # AI-specific components
```

## Component Development Rules

### 1. File Naming
- Use PascalCase for component files: `TaskCard.tsx`
- Use kebab-case for directories: `task-management/`

### 2. Component Structure
```tsx
// ComponentName.tsx
import React from 'react'
import { cn } from '@/lib/utils'

interface ComponentNameProps {
  // Define props with TypeScript
  title: string
  className?: string
}

export function ComponentName({ title, className }: ComponentNameProps) {
  return (
    <div className={cn("base-styles", className)}>
      {title}
    </div>
  )
}
```

### 3. Styling Guidelines
- Use Tailwind CSS for styling
- Use the `cn()` utility for conditional classes
- Follow the design system defined in `tailwind.config.js`
- Use CSS variables for theming (dark/light mode)

### 4. Props and Types
- Always define TypeScript interfaces for props
- Use optional props with default values when appropriate
- Include `className` prop for external styling
- Use discriminated unions for complex prop variations

### 5. Accessibility
- Include proper ARIA labels and roles
- Ensure keyboard navigation works
- Maintain proper color contrast ratios
- Test with screen readers

### 6. Performance
- Use `React.memo()` for expensive components
- Implement proper loading states
- Use `useCallback` and `useMemo` when needed
- Lazy load heavy components

## Common Patterns

### Form Components
```tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const formSchema = z.object({
  title: z.string().min(1, 'Title is required'),
})

export function TaskForm() {
  const form = useForm({
    resolver: zodResolver(formSchema),
  })
  
  // Form implementation
}
```

### Data Fetching Components
```tsx
import { useQuery } from '@tanstack/react-query'

export function ProjectList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
  })
  
  if (isLoading) return <LoadingSpinner />
  if (error) return <ErrorMessage error={error} />
  
  return <ProjectGrid projects={data} />
}
```

### Interactive Components
```tsx
import { useState } from 'react'
import { Button } from '@/components/ui/button'

export function InteractiveComponent() {
  const [isOpen, setIsOpen] = useState(false)
  
  return (
    <div>
      <Button onClick={() => setIsOpen(!isOpen)}>
        Toggle
      </Button>
      {isOpen && <Content />}
    </div>
  )
}
```

## Integration Points

### State Management
- Use React Query for server state
- Use Zustand for client state
- Use React Context sparingly (mainly for theme/auth)

### API Integration
- Create custom hooks for API calls
- Use React Query for caching and synchronization
- Handle loading and error states consistently

### Real-time Updates
- Use WebSocket connections for live updates
- Implement optimistic updates for better UX
- Handle connection errors gracefully

## Testing Requirements

### Unit Tests
- Test component rendering
- Test user interactions
- Test prop variations
- Test error states

### Integration Tests
- Test component integration
- Test API interactions
- Test form submissions

### Accessibility Tests
- Test keyboard navigation
- Test screen reader compatibility
- Test color contrast

## Examples

### Good Component
```tsx
interface TaskCardProps {
  task: Task
  onEdit?: (task: Task) => void
  onDelete?: (taskId: string) => void
  className?: string
}

export function TaskCard({ task, onEdit, onDelete, className }: TaskCardProps) {
  const { mutate: deleteTask, isPending } = useDeleteTask()
  
  return (
    <Card className={cn("p-4", className)}>
      <CardHeader>
        <CardTitle>{task.title}</CardTitle>
        <CardDescription>{task.description}</CardDescription>
      </CardHeader>
      <CardContent>
        <TaskStatus status={task.status} />
        <TaskPriority priority={task.priority} />
      </CardContent>
      <CardFooter>
        <Button onClick={() => onEdit?.(task)}>Edit</Button>
        <Button 
          variant="destructive" 
          onClick={() => deleteTask(task.id)}
          disabled={isPending}
        >
          Delete
        </Button>
      </CardFooter>
    </Card>
  )
}
```

### Bad Component
```tsx
// ❌ Avoid: No TypeScript, no accessibility, poor structure
export function TaskCard(props) {
  return (
    <div onClick={() => props.onClick()}>
      <h3>{props.task.title}</h3>
      <p>{props.task.description}</p>
      <button>Edit</button>
      <button>Delete</button>
    </div>
  )
}
```

## TODO Items

- [ ] Create base UI components using shadcn/ui
- [ ] Implement layout components (Header, Sidebar, Footer)
- [ ] Build form components with validation
- [ ] Create data visualization components
- [ ] Implement Kanban board components
- [ ] Build Gantt chart components
- [ ] Create AI-specific components (chat, suggestions)
- [ ] Add comprehensive test coverage
- [ ] Implement accessibility features
- [ ] Add loading and error states
