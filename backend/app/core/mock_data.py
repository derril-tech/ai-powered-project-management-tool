"""
Mock data for development and testing purposes.
This file contains sample data that can be used to populate the database
during development or for testing scenarios.
"""

from datetime import datetime, timedelta
from uuid import uuid4

# Mock Teams
MOCK_TEAMS = [
    {
        "id": str(uuid4()),
        "name": "Engineering Team",
        "description": "Core engineering team responsible for product development",
        "settings": '{"theme": "dark", "notifications": true}'
    },
    {
        "id": str(uuid4()),
        "name": "Design Team", 
        "description": "UI/UX design team focused on user experience",
        "settings": '{"theme": "light", "notifications": false}'
    },
    {
        "id": str(uuid4()),
        "name": "Product Team",
        "description": "Product management and strategy team",
        "settings": '{"theme": "auto", "notifications": true}'
    }
]

# Mock Users
MOCK_USERS = [
    {
        "id": str(uuid4()),
        "email": "alice.johnson@company.com",
        "name": "Alice Johnson",
        "role": "admin",
        "team_id": MOCK_TEAMS[0]["id"],
        "avatar": "https://example.com/avatars/alice.jpg",
        "is_active": True,
        "is_verified": True
    },
    {
        "id": str(uuid4()),
        "email": "bob.smith@company.com", 
        "name": "Bob Smith",
        "role": "pm",
        "team_id": MOCK_TEAMS[0]["id"],
        "avatar": "https://example.com/avatars/bob.jpg",
        "is_active": True,
        "is_verified": True
    },
    {
        "id": str(uuid4()),
        "email": "carol.davis@company.com",
        "name": "Carol Davis",
        "role": "contributor", 
        "team_id": MOCK_TEAMS[1]["id"],
        "avatar": "https://example.com/avatars/carol.jpg",
        "is_active": True,
        "is_verified": True
    },
    {
        "id": str(uuid4()),
        "email": "david.wilson@company.com",
        "name": "David Wilson",
        "role": "contributor",
        "team_id": MOCK_TEAMS[0]["id"], 
        "avatar": "https://example.com/avatars/david.jpg",
        "is_active": True,
        "is_verified": True
    },
    {
        "id": str(uuid4()),
        "email": "eva.brown@company.com",
        "name": "Eva Brown",
        "role": "viewer",
        "team_id": MOCK_TEAMS[2]["id"],
        "avatar": "https://example.com/avatars/eva.jpg", 
        "is_active": True,
        "is_verified": True
    }
]

# Mock Projects
MOCK_PROJECTS = [
    {
        "id": str(uuid4()),
        "name": "E-commerce Platform Redesign",
        "description": "Complete redesign of the main e-commerce platform with modern UI/UX and improved performance",
        "status": "active",
        "owner_id": MOCK_USERS[0]["id"],
        "team_id": MOCK_TEAMS[0]["id"],
        "settings": '{"theme": "modern", "features": ["search", "cart", "checkout"]}'
    },
    {
        "id": str(uuid4()),
        "name": "Mobile App Development",
        "description": "Native mobile app for iOS and Android platforms with offline capabilities",
        "status": "active", 
        "owner_id": MOCK_USERS[1]["id"],
        "team_id": MOCK_TEAMS[0]["id"],
        "settings": '{"platforms": ["ios", "android"], "offline": true}'
    },
    {
        "id": str(uuid4()),
        "name": "API Integration Project",
        "description": "Integration with third-party APIs for payment processing and shipping",
        "status": "completed",
        "owner_id": MOCK_USERS[2]["id"], 
        "team_id": MOCK_TEAMS[1]["id"],
        "settings": '{"apis": ["stripe", "shippo"], "webhooks": true}'
    },
    {
        "id": str(uuid4()),
        "name": "Analytics Dashboard",
        "description": "Real-time analytics dashboard for business intelligence and reporting",
        "status": "active",
        "owner_id": MOCK_USERS[3]["id"],
        "team_id": MOCK_TEAMS[2]["id"], 
        "settings": '{"charts": ["line", "bar", "pie"], "real_time": true}'
    }
]

# Mock Sprints
MOCK_SPRINTS = [
    {
        "id": str(uuid4()),
        "name": "Sprint 1 - Foundation",
        "goal": "Set up project foundation and basic architecture",
        "status": "completed",
        "project_id": MOCK_PROJECTS[0]["id"],
        "start_date": datetime.now() - timedelta(days=30),
        "end_date": datetime.now() - timedelta(days=16)
    },
    {
        "id": str(uuid4()),
        "name": "Sprint 2 - Core Features", 
        "goal": "Implement core e-commerce features",
        "status": "active",
        "project_id": MOCK_PROJECTS[0]["id"],
        "start_date": datetime.now() - timedelta(days=15),
        "end_date": datetime.now() + timedelta(days=1)
    },
    {
        "id": str(uuid4()),
        "name": "Sprint 1 - Mobile UI",
        "goal": "Design and implement mobile user interface",
        "status": "planning",
        "project_id": MOCK_PROJECTS[1]["id"], 
        "start_date": datetime.now() + timedelta(days=1),
        "end_date": datetime.now() + timedelta(days=14)
    }
]

# Mock Tasks
MOCK_TASKS = [
    {
        "id": str(uuid4()),
        "title": "Design user interface mockups",
        "description": "Create wireframes and mockups for the new dashboard with modern design principles",
        "status": "todo",
        "priority": "high",
        "project_id": MOCK_PROJECTS[0]["id"],
        "assignee_id": MOCK_USERS[2]["id"],
        "sprint_id": MOCK_SPRINTS[1]["id"],
        "estimated_hours": 16,
        "due_date": datetime.now() + timedelta(days=5)
    },
    {
        "id": str(uuid4()),
        "title": "Set up development environment",
        "description": "Configure local development environment for the team with Docker and CI/CD",
        "status": "done",
        "priority": "medium", 
        "project_id": MOCK_PROJECTS[0]["id"],
        "assignee_id": MOCK_USERS[3]["id"],
        "sprint_id": MOCK_SPRINTS[0]["id"],
        "estimated_hours": 8,
        "actual_hours": 6,
        "due_date": datetime.now() - timedelta(days=20)
    },
    {
        "id": str(uuid4()),
        "title": "Implement authentication system",
        "description": "Build JWT-based authentication with refresh tokens and OAuth integration",
        "status": "in_progress",
        "priority": "high",
        "project_id": MOCK_PROJECTS[0]["id"],
        "assignee_id": MOCK_USERS[0]["id"],
        "sprint_id": MOCK_SPRINTS[1]["id"],
        "estimated_hours": 24,
        "actual_hours": 12,
        "due_date": datetime.now() + timedelta(days=2)
    },
    {
        "id": str(uuid4()),
        "title": "API documentation review",
        "description": "Review and update API documentation for v2.0 with OpenAPI specification",
        "status": "review",
        "priority": "low",
        "project_id": MOCK_PROJECTS[2]["id"],
        "assignee_id": MOCK_USERS[1]["id"],
        "estimated_hours": 4,
        "actual_hours": 3,
        "due_date": datetime.now() - timedelta(days=1)
    },
    {
        "id": str(uuid4()),
        "title": "Database schema design",
        "description": "Design and implement the new database schema with proper indexing and constraints",
        "status": "done",
        "priority": "high",
        "project_id": MOCK_PROJECTS[0]["id"],
        "assignee_id": MOCK_USERS[3]["id"],
        "sprint_id": MOCK_SPRINTS[0]["id"],
        "estimated_hours": 12,
        "actual_hours": 10,
        "due_date": datetime.now() - timedelta(days=25)
    },
    {
        "id": str(uuid4()),
        "title": "Mobile app wireframes",
        "description": "Create wireframes for the mobile app with focus on user experience",
        "status": "todo",
        "priority": "medium",
        "project_id": MOCK_PROJECTS[1]["id"],
        "assignee_id": MOCK_USERS[2]["id"],
        "sprint_id": MOCK_SPRINTS[2]["id"],
        "estimated_hours": 20,
        "due_date": datetime.now() + timedelta(days=10)
    }
]

# Mock Automations
MOCK_AUTOMATIONS = [
    {
        "id": str(uuid4()),
        "name": "Auto-assign high priority tasks",
        "description": "Automatically assign high priority tasks to team lead",
        "trigger": {
            "type": "task_created",
            "config": {}
        },
        "conditions": [
            {
                "field": "priority",
                "operator": "equals", 
                "value": "high"
            }
        ],
        "actions": [
            {
                "type": "assign_task",
                "config": {
                    "assignee_id": MOCK_USERS[0]["id"]
                }
            }
        ],
        "enabled": True
    },
    {
        "id": str(uuid4()),
        "name": "Sprint completion notification",
        "description": "Send notification when sprint is completed",
        "trigger": {
            "type": "sprint_completed",
            "config": {}
        },
        "conditions": [],
        "actions": [
            {
                "type": "send_notification",
                "config": {
                    "recipients": "team",
                    "message": "Sprint {sprint_name} has been completed!"
                }
            }
        ],
        "enabled": True
    }
]

# Mock AI Responses
MOCK_AI_RESPONSES = [
    {
        "id": str(uuid4()),
        "content": "Based on the project requirements, I recommend implementing a microservices architecture with the following components: 1) User Service for authentication, 2) Product Service for catalog management, 3) Order Service for transaction processing, and 4) Notification Service for communications.",
        "citations": [
            {
                "source": "Project Requirements Document",
                "page": 5,
                "text": "The system must support high scalability and maintainability"
            }
        ],
        "confidence": 0.85,
        "model": "gpt-4",
        "created_at": datetime.now() - timedelta(hours=2)
    },
    {
        "id": str(uuid4()),
        "content": "The current sprint is at risk of not meeting its goals. Key blockers include: 1) Authentication system implementation is behind schedule, 2) Database schema changes are pending review, 3) Team capacity is reduced due to vacation. Recommendations: Extend sprint by 3 days or reduce scope by removing non-critical features.",
        "citations": [
            {
                "source": "Sprint 2 Progress Report",
                "page": 2,
                "text": "Authentication system is 50% complete with 2 days remaining"
            }
        ],
        "confidence": 0.92,
        "model": "claude-3",
        "created_at": datetime.now() - timedelta(hours=1)
    }
]
