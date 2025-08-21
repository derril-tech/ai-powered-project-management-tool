'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Bot, Lightbulb, TrendingUp, AlertTriangle, Send } from 'lucide-react'

// Mock AI insights data
const mockAIInsights = [
  {
    id: '1',
    type: 'project_planning',
    title: 'Architecture Recommendation',
    content: 'Based on the project requirements, I recommend implementing a microservices architecture with the following components: 1) User Service for authentication, 2) Product Service for catalog management, 3) Order Service for transaction processing, and 4) Notification Service for communications.',
    confidence: 0.85,
    model: 'gpt-4',
    timestamp: '2024-03-01T10:30:00Z',
    citations: [
      { source: 'Project Requirements Document', page: 5, text: 'The system must support high scalability and maintainability' }
    ]
  },
  {
    id: '2',
    type: 'risk_analysis',
    title: 'Sprint Risk Alert',
    content: 'The current sprint is at risk of not meeting its goals. Key blockers include: 1) Authentication system implementation is behind schedule, 2) Database schema changes are pending review, 3) Team capacity is reduced due to vacation. Recommendations: Extend sprint by 3 days or reduce scope by removing non-critical features.',
    confidence: 0.92,
    model: 'claude-3',
    timestamp: '2024-03-01T09:15:00Z',
    citations: [
      { source: 'Sprint 2 Progress Report', page: 2, text: 'Authentication system is 50% complete with 2 days remaining' }
    ]
  },
  {
    id: '3',
    type: 'optimization',
    title: 'Performance Optimization',
    content: 'Analysis of the current codebase reveals several optimization opportunities: 1) Implement database query caching for frequently accessed data, 2) Add pagination to large result sets, 3) Optimize image loading with lazy loading and compression, 4) Consider implementing a CDN for static assets.',
    confidence: 0.78,
    model: 'gpt-4',
    timestamp: '2024-03-01T08:45:00Z',
    citations: []
  }
]

const insightTypes = {
  project_planning: { icon: Lightbulb, color: 'bg-blue-100 text-blue-800', label: 'Planning' },
  risk_analysis: { icon: AlertTriangle, color: 'bg-red-100 text-red-800', label: 'Risk' },
  optimization: { icon: TrendingUp, color: 'bg-green-100 text-green-800', label: 'Optimization' }
}

export default function AIPage() {
  const [query, setQuery] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!query.trim()) return
    
    setIsLoading(true)
    // TODO: Implement AI query submission
    setTimeout(() => {
      setIsLoading(false)
      setQuery('')
    }, 2000)
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex items-center gap-3 mb-8">
        <Bot className="w-8 h-8 text-blue-600" />
        <div>
          <h1 className="text-3xl font-bold">AI Insights</h1>
          <p className="text-gray-600 dark:text-gray-300">Get AI-powered recommendations and insights</p>
        </div>
      </div>

      {/* AI Query Interface */}
      <Card className="mb-8">
        <CardHeader>
          <CardTitle>Ask AI Assistant</CardTitle>
          <CardDescription>
            Get instant insights about your projects, tasks, and team performance
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <Textarea
              placeholder="Ask about project planning, risk analysis, optimization opportunities, or any other project-related questions..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="min-h-[100px]"
              disabled={isLoading}
            />
            <div className="flex justify-between items-center">
              <div className="text-sm text-gray-500">
                Powered by GPT-4 and Claude-3
              </div>
              <Button type="submit" disabled={isLoading || !query.trim()}>
                {isLoading ? (
                  <div className="flex items-center gap-2">
                    <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                    Analyzing...
                  </div>
                ) : (
                  <div className="flex items-center gap-2">
                    <Send className="w-4 h-4" />
                    Get Insights
                  </div>
                )}
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>

      {/* Recent AI Insights */}
      <div className="space-y-6">
        <h2 className="text-2xl font-semibold">Recent Insights</h2>
        
        {mockAIInsights.map((insight) => {
          const typeInfo = insightTypes[insight.type as keyof typeof insightTypes]
          const TypeIcon = typeInfo.icon
          
          return (
            <Card key={insight.id} className="hover:shadow-md transition-shadow">
              <CardHeader>
                <div className="flex justify-between items-start">
                  <div className="flex items-center gap-3">
                    <TypeIcon className="w-5 h-5 text-gray-600" />
                    <div>
                      <CardTitle className="text-lg">{insight.title}</CardTitle>
                      <div className="flex items-center gap-2 mt-1">
                        <Badge className={typeInfo.color}>
                          {typeInfo.label}
                        </Badge>
                        <Badge variant="secondary">
                          {insight.model}
                        </Badge>
                        <Badge variant="outline">
                          {Math.round(insight.confidence * 100)}% confidence
                        </Badge>
                      </div>
                    </div>
                  </div>
                  <span className="text-sm text-gray-500">
                    {new Date(insight.timestamp).toLocaleDateString()}
                  </span>
                </div>
              </CardHeader>
              <CardContent>
                <p className="text-gray-700 dark:text-gray-300 mb-4">
                  {insight.content}
                </p>
                
                {insight.citations.length > 0 && (
                  <div className="border-t pt-4">
                    <h4 className="text-sm font-medium mb-2">Sources:</h4>
                    <div className="space-y-1">
                      {insight.citations.map((citation, index) => (
                        <div key={index} className="text-sm text-gray-600 dark:text-gray-400">
                          • {citation.source} (p. {citation.page}): "{citation.text}"
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          )
        })}
      </div>

      {/* Quick Actions */}
      <div className="mt-8">
        <h3 className="text-lg font-semibold mb-4">Quick Actions</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Button variant="outline" className="h-auto p-4 flex flex-col items-center gap-2">
            <Lightbulb className="w-6 h-6" />
            <span>Generate Project Plan</span>
          </Button>
          <Button variant="outline" className="h-auto p-4 flex flex-col items-center gap-2">
            <AlertTriangle className="w-6 h-6" />
            <span>Risk Analysis</span>
          </Button>
          <Button variant="outline" className="h-auto p-4 flex flex-col items-center gap-2">
            <TrendingUp className="w-6 h-6" />
            <span>Performance Review</span>
          </Button>
        </div>
      </div>
    </div>
  )
}
