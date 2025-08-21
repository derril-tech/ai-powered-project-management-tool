'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Plus, MoreVertical, Calendar, User } from 'lucide-react'

// Mock data for tasks
const mockTasks = {
  todo: [
    {
      id: '1',
      title: 'Design user interface mockups',
      description: 'Create wireframes and mockups for the new dashboard',
      priority: 'high',
      assignee: 'Alice Johnson',
      dueDate: '2024-03-10',
      project: 'E-commerce Platform'
    },
    {
      id: '2',
      title: 'Set up development environment',
      description: 'Configure local development environment for the team',
      priority: 'medium',
      assignee: 'Bob Smith',
      dueDate: '2024-03-08',
      project: 'Mobile App Development'
    }
  ],
  in_progress: [
    {
      id: '3',
      title: 'Implement authentication system',
      description: 'Build JWT-based authentication with refresh tokens',
      priority: 'high',
      assignee: 'Carol Davis',
      dueDate: '2024-03-15',
      project: 'E-commerce Platform'
    }
  ],
  review: [
    {
      id: '4',
      title: 'API documentation review',
      description: 'Review and update API documentation for v2.0',
      priority: 'low',
      assignee: 'David Wilson',
      dueDate: '2024-03-12',
      project: 'API Integration Project'
    }
  ],
  done: [
    {
      id: '5',
      title: 'Database schema design',
      description: 'Design and implement the new database schema',
      priority: 'high',
      assignee: 'Eva Brown',
      dueDate: '2024-03-05',
      project: 'E-commerce Platform'
    }
  ]
}

const priorityColors = {
  high: 'bg-red-100 text-red-800',
  medium: 'bg-yellow-100 text-yellow-800',
  low: 'bg-green-100 text-green-800'
}

const columnTitles = {
  todo: 'To Do',
  in_progress: 'In Progress',
  review: 'Review',
  done: 'Done'
}

const columnColors = {
  todo: 'bg-gray-50',
  in_progress: 'bg-blue-50',
  review: 'bg-yellow-50',
  done: 'bg-green-50'
}

export default function TasksPage() {
  const [tasks, setTasks] = useState(mockTasks)

  const handleDragStart = (e: React.DragEvent, taskId: string) => {
    e.dataTransfer.setData('taskId', taskId)
  }

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault()
  }

  const handleDrop = (e: React.DragEvent, targetStatus: string) => {
    e.preventDefault()
    const taskId = e.dataTransfer.getData('taskId')
    
    // Find the task in the current state
    let sourceStatus = ''
    let task = null
    
    Object.entries(tasks).forEach(([status, taskList]) => {
      const foundTask = taskList.find(t => t.id === taskId)
      if (foundTask) {
        sourceStatus = status
        task = foundTask
      }
    })

    if (task && sourceStatus !== targetStatus) {
      // Remove from source column
      const updatedTasks = { ...tasks }
      updatedTasks[sourceStatus as keyof typeof tasks] = updatedTasks[sourceStatus as keyof typeof tasks].filter(t => t.id !== taskId)
      
      // Add to target column
      updatedTasks[targetStatus as keyof typeof tasks] = [...updatedTasks[targetStatus as keyof typeof tasks], task]
      
      setTasks(updatedTasks)
    }
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Tasks</h1>
          <p className="text-gray-600 dark:text-gray-300">Manage your tasks with Kanban board</p>
        </div>
        <Button className="flex items-center gap-2">
          <Plus className="w-4 h-4" />
          New Task
        </Button>
      </div>

      {/* Kanban Board */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {Object.entries(tasks).map(([status, taskList]) => (
          <div
            key={status}
            className={`${columnColors[status as keyof typeof columnColors]} rounded-lg p-4 min-h-[600px]`}
            onDragOver={handleDragOver}
            onDrop={(e) => handleDrop(e, status)}
          >
            <div className="flex justify-between items-center mb-4">
              <h3 className="font-semibold text-lg">{columnTitles[status as keyof typeof columnTitles]}</h3>
              <Badge variant="secondary">{taskList.length}</Badge>
            </div>
            
            <div className="space-y-3">
              {taskList.map((task) => (
                <Card
                  key={task.id}
                  className="cursor-move hover:shadow-md transition-shadow"
                  draggable
                  onDragStart={(e) => handleDragStart(e, task.id)}
                >
                  <CardHeader className="pb-3">
                    <div className="flex justify-between items-start">
                      <CardTitle className="text-sm font-medium">{task.title}</CardTitle>
                      <Button variant="ghost" size="sm" className="h-6 w-6 p-0">
                        <MoreVertical className="w-3 h-3" />
                      </Button>
                    </div>
                  </CardHeader>
                  <CardContent className="pt-0">
                    <p className="text-xs text-gray-600 mb-3">{task.description}</p>
                    
                    <div className="space-y-2">
                      <div className="flex items-center justify-between">
                        <Badge className={priorityColors[task.priority as keyof typeof priorityColors]}>
                          {task.priority}
                        </Badge>
                        <span className="text-xs text-gray-500">{task.project}</span>
                      </div>
                      
                      <div className="flex items-center justify-between text-xs text-gray-500">
                        <div className="flex items-center gap-1">
                          <User className="w-3 h-3" />
                          {task.assignee}
                        </div>
                        <div className="flex items-center gap-1">
                          <Calendar className="w-3 h-3" />
                          {task.dueDate}
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
