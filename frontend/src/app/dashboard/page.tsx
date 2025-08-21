export default function DashboardPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Projects</h2>
          <p className="text-gray-600 dark:text-gray-300">Project management overview</p>
        </div>
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Tasks</h2>
          <p className="text-gray-600 dark:text-gray-300">Task tracking and management</p>
        </div>
        <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">AI Insights</h2>
          <p className="text-gray-600 dark:text-gray-300">AI-powered project insights</p>
        </div>
      </div>
    </div>
  )
}
