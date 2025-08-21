# AI-Powered Project Management Tool - Frontend

This is the frontend application for the AI-Powered Project Management Tool, built with Next.js 14, React 18, TypeScript, and Tailwind CSS.

## Features

- **Modern React**: Built with React 18 and Next.js 14 App Router
- **TypeScript**: Full type safety throughout the application
- **Tailwind CSS**: Utility-first CSS framework with custom design system
- **shadcn/ui**: Beautiful, accessible UI components
- **Real-time Updates**: WebSocket integration for live updates
- **AI Integration**: AI-powered features and insights
- **Responsive Design**: Mobile-first responsive design
- **Dark Mode**: Built-in dark/light theme support

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui
- **State Management**: React Query + Zustand
- **Real-time**: Socket.io Client
- **Forms**: React Hook Form + Zod
- **Charts**: Recharts
- **Icons**: Lucide React

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running (see backend README)

### Installation

1. Clone the repository
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

4. Copy environment variables:
   ```bash
   cp env.example .env.local
   ```

5. Update `.env.local` with your configuration:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
   NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
   ```

### Development

Start the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Building for Production

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Landing page
│   ├── dashboard/         # Dashboard pages
│   ├── projects/          # Project management
│   └── tasks/             # Task management
├── components/            # Reusable components
│   ├── ui/               # shadcn/ui components
│   ├── layout/           # Layout components
│   ├── forms/            # Form components
│   └── charts/           # Data visualization
├── hooks/                # Custom React hooks
├── lib/                  # Utility functions
├── types/                # TypeScript definitions
└── utils/                # Helper functions
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## Contributing

1. Follow the component development guidelines in `src/components/_INSTRUCTIONS.md`
2. Use TypeScript for all new code
3. Follow the established naming conventions
4. Add tests for new components
5. Ensure accessibility compliance

## Environment Variables

See `env.example` for all available environment variables.

## API Integration

The frontend communicates with the backend API through:
- REST API calls using React Query
- WebSocket connections for real-time updates
- File uploads to S3-compatible storage

## Deployment

The application can be deployed to:
- Vercel (recommended)
- Netlify
- Any static hosting service

## Support

For questions and support, please refer to the main project documentation.
