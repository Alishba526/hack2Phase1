# Todo App - Hackathon II

## Project Overview
This repository contains the Todo application for Hackathon II, evolving from a console app to a full-stack, cloud-native, AI-powered system using Spec-Driven Development.

## Spec-Kit Structure
Specifications are organized in `specs`:
- `specs/overview.md` - Project overview
- `specs/features/` - Feature specs (what to build)
- `specs/api/` - API endpoint and MCP tool specs
- `specs/database/` - Schema and model specs
- `specs/ui/` - Component and page specs

## How to Use Specs
1. Always read the relevant spec before implementing.
2. Reference specs using paths like `@specs/features/task-crud.md`.
3. Update specs first if requirements change, then regenerate implementation.

## Project Structure
- `frontend/` - Next.js app (Phase II+)
- `backend/`  - FastAPI app (Phase II+)
- `agents/`   - Agentic dev helpers (planner, coder, tester)

## Development Workflow
1. Write or update spec in `specs/`.
2. Ask the AI coding agent to implement based on a specific spec file.
3. Run and test locally.
4. Refine the spec and regenerate if behavior is not correct.

## Commands (suggested)
- Backend: `cd backend && uvicorn main:app --reload`
- Frontend: `cd frontend && npm run dev`


