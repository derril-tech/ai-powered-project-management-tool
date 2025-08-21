'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Plus, Search, Filter } from 'lucide-react'

// Mock data for projects
const mockProjects = [
  {
    id: '1',
    name: 'E-commerce Platform Redesign',
    description: 'Complete redesign of the main e-commerce platform with modern UI/UX',
    status: 'active',
    progress: 65,
    team: ['Alice Johnson', 'Bob Smith', 'Carol Davis'],
    dueDate: '2024-03-15',
    priority: 'high'
  },
  {
    id: '2',
    name: 'Mobile App Development',
    description: 'Native mobile app for iOS and Android platforms',
    status: 'active',
    progress: 35,
    team: ['David Wilson', 'Eva Brown'],
    dueDate: '2024-04-20',
    priority: 'medium'
  },
  {
    id: '3',
    name: 'API Integration Project',
    description: 'Integration with third-party APIs for payment processing',
    status: 'completed',
    progress: 100,
    team: ['Frank Miller', 'Grace Lee'],
    dueDate: '2024-02-28',
    priority: 'low'
  }
]

const statusColors = {
  active: 'bg-green-100 text-green-800',
  completed: 'bg-blue-100 text-blue-800',
  archived: 'bg-gray-100 text-gray-800'
}

const priorityColors = {
  high: 'bg-red-100 text-red-800',
  medium: 'bg-yellow-100 text-yellow-800',
  low: 'bg-green-100 text-green-800'
}

export default function ProjectsPage() {
  const [searchTerm, setSearchTerm] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')

  const filteredProjects = mockProjects.filter(project => {
    const matchesSearch = project.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         project.description.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesStatus = statusFilter === 'all' || project.status === statusFilter
    return matchesSearch && matchesStatus
  })

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Projects</h1>
          <p className="text-gray-600 dark:text-gray-300">Manage and track your projects</p>
        </div>
        <Button className="flex items-center gap-2">
          <Plus className="w-4 h-4" />
          New Project
        </Button>
      </div>

      {/* Search and Filters */}
      <div className="flex gap-4 mb-6">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
          <input
            type="text"
            placeholder="Search projects..."
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <select
          className="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
        >
          <option value="all">All Status</option>
          <option value="active">Active</option>
          <option value="completed">Completed</option>
          <option value="archived">Archived</option>
        </select>
      </div>

      {/* Projects Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredProjects.map((project) => (
          <Card key={project.id} className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <div className="flex justify-between items-start">
                <div>
                  <CardTitle className="text-lg">{project.name}</CardTitle>
                  <CardDescription className="mt-2">{project.description}</CardDescription>
                </div>
                <Badge className={statusColors[project.status as keyof typeof statusColors]}>
                  {project.status}
                </Badge>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {/* Progress Bar */}
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span>Progress</span>
                    <span>{project.progress}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${project.progress}%` }}
                    ></div>
                  </div>
                </div>

                {/* Team Members */}
                <div>
                  <p className="text-sm font-medium mb-2">Team</p>
                  <div className="flex flex-wrap gap-1">
                    {project.team.map((member, index) => (
                      <Badge key={index} variant="secondary" className="text-xs">
                        {member}
                      </Badge>
                    ))}
                  </div>
                </div>

                {/* Project Details */}
                <div className="flex justify-between items-center">
                  <Badge className={priorityColors[project.priority as keyof typeof priorityColors]}>
                    {project.priority}
                  </Badge>
                  <span className="text-sm text-gray-500">Due: {project.dueDate}</span>
                </div>

                {/* Actions */}
                <div className="flex gap-2 pt-2">
                  <Button variant="outline" size="sm" className="flex-1">
                    View Details
                  </Button>
                  <Button variant="outline" size="sm">
                    Edit
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {filteredProjects.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">No projects found matching your criteria.</p>
        </div>
      )}
    </div>
  )
}
