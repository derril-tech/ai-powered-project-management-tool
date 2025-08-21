export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">About</h1>
      <div className="prose dark:prose-invert max-w-none">
        <p className="text-lg mb-4">
          The AI-Powered Project Management Tool is an enterprise project operating system 
          that blends classical PM tooling with AI copilots for planning, execution, and governance.
        </p>
        <h2 className="text-2xl font-semibold mb-4">Key Features</h2>
        <ul className="list-disc pl-6 mb-6">
          <li>Unified source of truth for work, decisions, and context</li>
          <li>Natural-language planning and updates</li>
          <li>Proactive risk/blocked-task detection and nudges</li>
          <li>Automation builder ("When X, do Y") to remove busywork</li>
          <li>Deep integrations with Jira/GitHub/Slack/Calendar</li>
        </ul>
        <h2 className="text-2xl font-semibold mb-4">Technology Stack</h2>
        <ul className="list-disc pl-6">
          <li><strong>Frontend:</strong> Next.js 14, React 18, TypeScript, Tailwind CSS</li>
          <li><strong>Backend:</strong> FastAPI, SQLAlchemy, PostgreSQL, Redis</li>
          <li><strong>AI:</strong> LangGraph, LangChain, OpenAI, Claude</li>
          <li><strong>Real-time:</strong> WebSockets, Socket.io</li>
        </ul>
      </div>
    </div>
  )
}
