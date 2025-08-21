// Project Management Types
export interface Project {
  id: string
  name: string
  description: string
  status: 'active' | 'completed' | 'archived'
  createdAt: string
  updatedAt: string
  ownerId: string
  teamId: string
}

export interface Task {
  id: string
  title: string
  description: string
  status: 'todo' | 'in_progress' | 'review' | 'done'
  priority: 'low' | 'medium' | 'high' | 'urgent'
  assigneeId?: string
  projectId: string
  sprintId?: string
  estimatedHours?: number
  actualHours?: number
  dueDate?: string
  createdAt: string
  updatedAt: string
}

export interface Sprint {
  id: string
  name: string
  startDate: string
  endDate: string
  projectId: string
  status: 'planning' | 'active' | 'completed'
  goal: string
}

export interface User {
  id: string
  email: string
  name: string
  avatar?: string
  role: 'owner' | 'admin' | 'pm' | 'contributor' | 'viewer'
  teamId: string
}

export interface Team {
  id: string
  name: string
  description: string
  createdAt: string
  updatedAt: string
}

// AI Integration Types
export interface AIResponse {
  content: string
  citations: Citation[]
  confidence: number
}

export interface Citation {
  source: string
  page?: number
  text: string
}

// Automation Types
export interface Automation {
  id: string
  name: string
  description: string
  trigger: AutomationTrigger
  conditions: AutomationCondition[]
  actions: AutomationAction[]
  enabled: boolean
  createdAt: string
  updatedAt: string
}

export interface AutomationTrigger {
  type: 'task_created' | 'task_updated' | 'sprint_started' | 'due_date_approaching'
  config: Record<string, any>
}

export interface AutomationCondition {
  field: string
  operator: 'equals' | 'not_equals' | 'contains' | 'greater_than' | 'less_than'
  value: any
}

export interface AutomationAction {
  type: 'assign_task' | 'send_notification' | 'update_status' | 'create_task'
  config: Record<string, any>
}
