# THE PROJECT BRIEF #

# Project Name #

# Product Description / Presentation #


AI‑Powered Project Management Tool — Claude‑Optimized Build Brief
Project Management & Workflow Automation Specialist Edition

Product Description / Presentation
An enterprise project operating system that blends classical PM tooling (Kanban/Gantt/roadmaps) with AI copilots for planning, execution, and governance. It ingests tasks, docs, chats, and metrics, then recommends staffing, dependencies, risk mitigations, and automations. Teams draft plans in plain English; the system converts them into structured epics, timelines, budgets, and OKRs with live health signals. 

Why teams love it:
• Unified source of truth for work, decisions, and context
• Natural‑language planning and updates
• Proactive risk/blocked‑task detection and nudges
• Automation builder ("When X, do Y") to remove busywork
• Deep integrations with Jira/GitHub/Slack/Calendar
Framework Choice & Why
LangGraph (orchestration) atop LangChain (tools/RAG) with pgvector‑backed retrieval. LangGraph gives deterministic, resumable multi‑step flows for planning → execution → review, human‑in‑the‑loop gates, and rollback. RAG grounds AI on tenant docs (requirements, PRDs, runbooks, past retros), eliminating hallucinations. OpenAI + Claude provide complementary strengths: structured generation + cautious reasoning for high‑stakes actions.
1. BACKEND ARCHITECTURE
•	FastAPI (Python 3.11 preferred) with async SQLAlchemy 2.0; modular routers: /projects, /tasks, /sprints, /okr, /automations, /integrations, /reports, /search.
•	AuthN/AuthZ: JWT (access/refresh), optional SSO (OIDC/SAML), tenant‑scoped RBAC (roles: owner, admin, pm, contributor, viewer).
•	Data: PostgreSQL (UUID PKs, row‑level security), pgvector for embeddings; Redis for queues, caching, rate limits, websocket presence.
•	LangGraph Orchestrators: PlanningGraph, RiskGraph, StandupGraph, AutomationGraph with checkpoints, idempotent steps, human approval gates.
•	RAG services: document ingestion (PDF, DOCX, Markdown, Confluence, Notion), chunking with structure‑aware parsers, embeddings store, source snapshots + citations.
•	File pipeline: object storage (S3/GCS), antivirus scan, MIME/type validation, PII redaction, OCR for images/PDFs.
•	Integrations hub: Slack/Teams, Jira/Asana/Trello, GitHub/GitLab/Bitbucket, Google/Outlook Calendar, Drive/OneDrive, Notion/Confluence, Webhooks (HMAC).
•	Real‑time layer: WebSocket endpoints for presence, notifications, live cursors, board updates; server events for long‑running jobs.
•	Search: hybrid semantic + keyword across tasks/docs/comments with filters (assignee, status, labels, sprint).
•	Automation engine: no‑code rules (triggers, conditions, actions) + cron; safe‑exec sandbox; audit logs for every automation run.
•	Scheduling & forecasting: Monte Carlo simulation for delivery dates; critical‑path calculation; capacity & velocity models.
•	Reporting: OKR roll‑ups, burndown/burnup, WIP limits, DORA‑style delivery metrics; export to CSV/PDF.
•	Email service: transactional notifications (SendGrid/SES), digest summaries; templated with Jinja.
•	Observability & ops: structured logging (JSON), request IDs, OpenAPI, health/ready probes, background workers (RQ/Celery).
•	Security: parameterized queries, input validation (Pydantic v2), per‑tenant encryption keys, secrets via env/Key Management Service.
•	Migrations & seeds: Alembic autogenerate with review; seed fixtures for demo tenant; blue/green ready.
•	Cost/limits: per‑tenant quotas (tokens, storage, API calls) with graceful throttling and admin dashboards.
2. FRONTEND ARCHITECTURE
•	Next.js 14 (App Router) + React 18 + TypeScript; SSR/ISR for dashboards, client components for boards and editors.
•	State/query: React Query (server cache) + lightweight Zustand context for UI state; optimistic updates for drag‑drop changes.
•	UI kit: Tailwind + shadcn/ui; accessibility‑first components; theming (dark/light + custom brand tokens).
•	Realtime: socket client for presence/notifications; toasts, activity feed, live cursors on boards and docs.
•	Editors: rich text (MDX), task editor with slash‑commands (/assign, /estimate), diagram lane for dependencies, OKR editor.
•	Views: Kanban, List, Calendar, Timeline/Gantt, Roadmap, Workload heatmap, Risk matrix, Automation builder (If/Then canvas).
•	AI surfaces: plan composer, standup summarizer, PRD/retro generators, natural‑language query bar ("Show blocked tasks in Sprint Alpha due this week").
•	Performance: code‑split routes, lazy load heavy charts, web workers for large board diffs, virtualized lists for 10k+ tasks.
•	I18n & timezones: locale packs, humanized dates, working‑hours calendar awareness; WCAG 2.1 AA color/contrast presets.
•	Files & previews: inline previews for Office/PDF/images; drag‑drop upload with resumable chunks and virus check status.
•	Offline/poor network: background sync, retry queue, stale‑while‑revalidate; keyboard‑first shortcuts palette.
•	Analytics: client events (consent‑aware) for feature usage, funnel metrics; feature‑flag gating via remote config.
3. DESIGN REQUIREMENTS (UI/UX)
•	Information hierarchy optimized for decision‑making: status → risks → actions.
•	Micro‑interactions: drag‑drop with haptics, inline edit, AI suggestions chips; zero‑state guidance in each view.
•	Accessible color system with semantic tokens (success/warn/danger/info); large hit‑areas for touch.
•	Visualization suite: timeline, burndown/burnup, cumulative flow, dependency graph, workload, risk heatmap.
•	Authoring patterns: natural‑language to structure (slash commands, quick‑add), multi‑select bulk operations.
•	Collaboration cues: presence avatars, comment threads with mentions, change history with diff and revert.
•	Brandable themes per tenant; print‑ready exports for exec reports.
4. CORE INTEGRATIONS
•	OpenAI + Claude via LangChain tools for planning, summarization, and risk reasoning (with citations).
•	Identity: JWT first‑party; enterprise SSO (OIDC/SAML) optional; SCIM for user provisioning.
•	Work trackers: Jira, Asana, Trello bi‑directional sync (projects, issues, comments, status).
•	Code & CI: GitHub/GitLab/Bitbucket (PRs, commits), build status; auto‑link tasks to PRs.
•	Chat & meetings: Slack/Teams for notifications and slash‑commands; Google/Outlook Calendar for schedules.
•	Docs: Confluence/Notion/Drive/OneDrive import for RAG; snapshot and version with source links.
•	Email: SendGrid/SES; inbound email to create/comment on tasks; digest summaries.
•	Webhooks/Zapier/Make for long‑tail integrations; signed callbacks with replay protection.
5. DELIVERABLES REQUIRED
•	Next.js 14 frontend (TypeScript, Tailwind, shadcn/ui) with Kanban/Gantt/OKR views and Automation Builder.
•	FastAPI backend with async SQLAlchemy, JWT, LangGraph orchestrators, and integrations hub.
•	PostgreSQL schema + pgvector indices; Redis setup for cache/queues; Alembic migrations.
•	AI integrations (OpenAI/Claude) with guardrails, cost tracking, and citation surfaces; RAG service with ingestion workers.
•	WebSocket real‑time updates (presence, notifications, board changes).
•	File upload pipeline to S3/GCS with antivirus and previewers.
•	Email notification system and daily/weekly digest jobs.
•	Responsive design with dark/light modes; WCAG 2.1 AA passes for core flows.
•	Deployment configs for Vercel (FE) and Render (BE) with env templates; IaC snippets optional.
•	Docs: API (OpenAPI), Architecture ADRs, Runbooks, and Admin guide.
6. SUCCESS CRITERIA
•	Immediate deployability; tenant onboarding via self‑serve flow.
•	Handles 10k+ concurrent project users with real‑time board interactions.
•	Lighthouse ≥95 on core pages; P95 < 2s for dashboard and board interactions.
•	OpenAPI complete and accurate; >90% unit/integration coverage on critical paths.
•	Material improvements: reduce time‑to‑plan by 50%, increase on‑time delivery by 15% (tracked in reports).
7. IMPLEMENTATION GUIDELINES
•	Use dependency‑injected FastAPI services; split domain modules (projects, tasks, automations, insights).
•	Type‑safe end‑to‑end: Pydantic v2 models ↔ TypeScript types (openapi‑ts).
•	Strict input validation; idempotency keys for mutating endpoints and integrations.
•	Prompts as code: versioned prompt files with tests and evaluation datasets; avoid inline strings.
•	Human‑in‑the‑loop: required approvals before high‑impact actions (bulk moves, cross‑project edits).
•	Git hooks: black/ruff/mypy on BE; eslint/tsc/prettier on FE; commitlint + conventional commits.
•	Document ADRs for key choices; keep example env files up to date.
8. SECURITY & COMPLIANCE
•	Multi‑tenant isolation at row level; per‑tenant encryption keys for secrets and webhooks.
•	SSO (OIDC/SAML), SCIM provisioning, RBAC with least privilege; audit trail for every admin/automation action.
•	Data protection: TLS 1.2+, AES‑256 at rest, signed URLs for files, AV scanning, DLP/PII redaction options.
•	Secrets management via environment variables/KMS; rotate keys; IP allow‑lists for admin APIs.
•	Compliance posture: SOC 2‑aligned controls, GDPR (DPA, RTBF, export), data residency options (EU/US).
•	Rate limiting and abuse detection; anomaly alerts on automation loops or mass changes.
Claude — 5 Critical Prompts (Architecture‑Aware)
Prompt 1 — Repository Setup & Scaffolding
You are coding into an existing monorepo with Next.js 14 (frontend) and FastAPI (backend). Do NOT recreate the scaffold. Extend it by adding modules and files only where specified. Tasks:
• Create backend modules: projects, tasks, automations, insights, integrations
• Add Alembic migrations and seed data for a demo tenant
• Wire LangGraph PlanningGraph and RiskGraph
• Expose OpenAPI tags and dependency injection stubs
Output: a tree of new/modified files, code blocks per file, and .env.example updates.
Prompt 2 — Core Backend APIs & Models
Implement async SQLAlchemy 2.0 models and FastAPI routers for /projects, /tasks, /sprints, /okr, /automations. Include RBAC guards, idempotency keys, pagination, filters, and WebSocket events. Add RAG ingestion workers and embeddings writes (pgvector). Provide Alembic migration scripts. Output: code with exact file paths, tests (pytest), and curl examples.
Prompt 3 — Frontend Views & Realtime
In the existing Next.js 14 app (App Router), build Kanban, Timeline/Gantt, OKR editor, and Automation Builder canvas. Use TypeScript, Tailwind, shadcn/ui, React Query, and socket client. Implement optimistic updates and accessibility. Output: component files, route files, hooks, and example screenshots (ASCII layout acceptable).
Prompt 4 — AI Orchestration & Guardrails
Implement LangGraph graphs for planning, standups, and risk detection using OpenAI + Claude tools. Ground responses via RAG on project docs; require citations. Add human‑approval gates before bulk edits. Include prompt templates, tool schemas, and evaluation stubs. Output: graph code, prompt files, and examples.
Prompt 5 — Packaging & Deploy
Provide production deployment artifacts: Vercel config for FE, Render/Docker for BE, env templates, and runbooks. Add seed scripts, demo data, and feature flags. Verify health/ready probes. Output: Dockerfiles, Procfiles, env vars, Makefile targets, and a checklist for go‑live.




FOLLOW THIS 8 STEP PLAN TO PREPARE THE INFRASTRUCTURE
-----------------------------------------------------

# 🚀 Claude Fullstack Repo Prep – Optimized 8 Step Plan

  
The goal: build an extensive frontend + backend scaffold so Claude Code only has to finish ~20% of the work.  
Each step must be **completed and reviewed** before advancing.
IMPORTANT: YOU ARE BUILDING ONLY THE INFRASTRUCTURE OF THE APPLICATION NOT THE APPLICATION ITSELF !!!. FOLLOW THE STEPS IN NUMERICAL ORDER !!! starting from step 1.
You are doing the groundwork for the application, including setting up the folder structure, configuration files, and any necessary boilerplate code.
IMPORTANT: the checklist in each step has to be checked off 100% before moving to the next step

---

## STEP 1 — Build the Rich Infrastructure
Create a **deep scaffold** for both frontend and backend so Claude code can recognize the architecture immediately.

- Build a **frontend app shell** with routing, placeholder pages, components, and styling setup.  
- Build a **backend app shell** with API structure, health endpoint, and config in place.  
- Include `REPO_MAP.md`, `API_SPEC.md`, and a draft `CLAUDE.md` in the `docs/` folder.  (create the docs folder if it does not exist)
- Add **TODO markers and folder-level `_INSTRUCTIONS.md`** files so Claude knows exactly where to add logic.

**Deliverables**
- Frontend app shell with routing, placeholder pages, components, and styling setup  
- Backend app shell with API structure, health endpoint, and config  
- `docs/REPO_MAP.md`, `docs/API_SPEC.md` (stub), and draft `docs/CLAUDE.md`  
- TODO markers + folder-level `_INSTRUCTIONS.md` files  

**Checklist**
- [ ] Frontend scaffold built  
- [ ] Backend scaffold built 
- [ ] Docs folder created with drafts (`REPO_MAP.md`, `API_SPEC.md`, `CLAUDE.md`)  
- [ ] TODO markers and `_INSTRUCTIONS.md` stubs in place  

---

## STEP 2 — Enrich the Scaffold
If the repo looks shallow, enrich it so Claude needs fewer leaps of imagination.  

Add:
- Sample frontend routes and components (`/`, `/about`, `/dashboard`)  
- Domain model stubs and types/interfaces  
- Mock data + fixtures for UI flows  
- README files with quick run instructions for both frontend and backend  
- Instructions embedded in folders (e.g. `CLAUDE_TASK: …`)

**Deliverables**
- Sample routes and pages (`/`, `/about`, `/dashboard`)  
- Domain model stubs and type definitions  
- Mock data and fixtures for UI flows  
- README files for frontend and backend with run instructions  
- Folder-level instructions (`_INSTRUCTIONS.md`)  

**Checklist**
- [ ] At least 2–3 sample routes/pages exist  
- [ ] Domain types/interfaces stubbed out  
- [ ] Mock data + fixtures included  
- [ ] README_FRONTEND.md and README_BACKEND.md added  
- [ ] Each folder has `_INSTRUCTIONS.md` where relevant 

---

## STEP 3 — Audit for Alignment
Check that the scaffold actually matches the product brief, tech specs, and UX goals.
Add additional UI/UX elements (if needed) to make the application visually appealing (and update the design requirements after that)

- Do navigation and pages reflect the product’s main flows?  
- Do API endpoints match the UI needs?  
- Is the chosen tech stack consistent (no unused or conflicting libraries)?  
- Is the UX direction reflected (design tokens, layout, component stubs)?

**Deliverables**
- Alignment review across Product ↔ UI/UX ↔ Tech  
- Identify any missing flows, mismatched libraries, or conflicting instructions  

**Checklist**
- [ ] Navigation structure matches product journeys  
- [ ] Components/pages map to required features  
- [ ] API endpoints cover MVP needs  
- [ ] No contradictory or unused technologies  

---

## STEP 4 — Document the Architecture
Now make the docs **Claude-ready**:

- **REPO_MAP.md**: Full repo breakdown with roles of each folder  
- **API_SPEC.md**: Endpoints, payloads, error handling  
- **CLAUDE.md**: Editing rules, coding conventions, AI collaboration guidelines  

These three files are the **context backbone** Claude will use to understand the repo.

**Deliverables**
- `REPO_MAP.md`: full repo breakdown with folder purposes  
- `API_SPEC.md`: endpoints, models, error conventions  
- `CLAUDE.md`: collaboration rules, editing boundaries  

**Checklist**
- [ ] REPO_MAP.md fully describes structure  
- [ ] API_SPEC.md covers all MVP endpoints and schemas  
- [ ] CLAUDE.md includes project overview, editing rules, examples  

---

## STEP 5 — Improve the Prompt
Enhance the prompt (in `docs/PROMPT_DECLARATION.md`) with details Claude needs:

- FE/BE boundaries and data contracts  
- UX guidelines (states, accessibility, interaction patterns)  
- Performance budgets (bundle size, API latency)  
- Security constraints (auth, rate limits, PII handling)  
- Testing expectations (unit, integration, end-to-end)

**Deliverables**
- FE/BE boundaries and contracts  
- UX guidelines (states, accessibility, patterns)  
- Performance budgets (bundle size, latency targets)  
- Security constraints (auth, PII, rate limits)  
- Testing expectations  

**Checklist**
- [ ] Prompt includes FE/BE division of responsibility  
- [ ] UX principles and design tokens specified  
- [ ] Performance/security/testing requirements added  
- [ ] Prompt is concrete and actionable for Claude  

---

## STEP 6 — Expert Audit of the Prompt
Now do a **meticulous audit** of the one-page prompt declaration.

- Add Frontend Architecture, Backend Architecture, Design requirements, Core Integrations, Success Criteria, Implementation Guidelines and Security & Compliance categories from this Project Brief to the prompt declaration.
- Remove inconsistencies, duplicates, or unused technologies  
- Ensure Tech Stack → Product → Scaffold alignment (no mismatches)  
- Add UI/UX details that make the product visually appealing and usable  
- Double-check frontend and backend folders are ready  
- Confirm editing boundaries are clear (what Claude can/can’t touch)  
- Make the declaration **battle-tested and handoff-ready**

**Deliverables**
- Remove inconsistencies/duplicates  
- Ensure stack ↔ product ↔ scaffold alignment  
- Add UI/UX and accessibility details  
- Clarify file boundaries (editable vs do-not-touch)  
- Confirm prompt uses Claude-friendly syntax  

**Checklist**
- [ ] No unused or contradictory tech remains  
- [ ] UI/UX directives are product-specific and sufficient  
- [ ] Editing boundaries explicitly defined  
- [ ] Prompt syntax uses clear, imperative instructions  

---

## STEP 7 — Bird’s-Eye Repo Review
Do a quick top-level scan for missing pieces:

- All folders contain either code or `_INSTRUCTIONS.md`  
- `.env.example` files exist for both frontend and backend  
- CI/CD config is present and not trivially broken  
- Run scripts (`npm run dev`, `uvicorn …`) work end-to-end  
- No orphan TODOs without clear ownership

**Deliverables**
- Verify all core files exist  
- Confirm environment, CI, and scripts work end-to-end  

**Checklist**
- [ ] Every folder has code or `_INSTRUCTIONS.md`  
- [ ] `.env.example` present for both frontend and backend  
- [ ] CI pipeline triggers and passes basic checks  
- [ ] Dev script (`scripts/dev.sh`) runs both FE and BE  

---

## STEP 8 — Finalize CLAUDE.md
This is where Claude gets its **onboarding pack**. Make sure `CLAUDE.md` includes:

- **Project Overview**: one-paragraph purpose, stack, goals, target users  
- **Folder & File Structure**: what’s editable vs do-not-touch  
- **Coding Conventions**: style guides, naming rules, commenting expectations  
- **AI Collaboration Rules**: response format, edit rules, ambiguity handling  
- **Editing Rules**: full-file vs patches, locked files  
- **Dependencies & Setup**: frameworks, services, env vars  
- **Workflow & Tools**: how to run locally, FE/BE boundary, deployment notes  
- **Contextual Knowledge**: product quirks, domain rules, business logic caveats  
- **Examples**: good vs bad AI answer

**Deliverables**
- Project overview (purpose, stack, goals, users)  
- Folder & file structure with editable vs do-not-touch  
- Coding conventions (style, naming, commenting)  
- AI collaboration rules (response style, edit rules, ambiguity handling)  
- Dependencies and setup instructions  
- Workflow, deployment notes, contextual knowledge  
- Good vs bad answer examples  
- Fill out all the missing information in the CLAUDE.md file

**Checklist**
- [ ] Project overview section filled in  
- [ ] File boundaries clearly defined  
- [ ] Coding/style conventions included  
- [ ] AI collaboration & editing rules written  
- [ ] Dependencies & env notes covered  
- [ ] Workflow & deployment info added  
- [ ] Contextual knowledge documented  
- [ ] Good vs bad examples included  
- [ ] CLAUDE.md file does not miss any important information

---

# ✅ Outcome
When this 8-step plan is followed:
- The repo is a **rich, opinionated scaffold** (80% done).  
- Docs give Claude **clear boundaries + context**.  
- The one-page prompt is **battle-tested** and aligned.  
- Claude Code can safely and efficiently generate the missing 20%.  










