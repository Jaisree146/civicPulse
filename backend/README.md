# CivicPulse Backend

Backend service for **CivicPulse**, an AI-Powered Municipal Complaint Management System that enables citizens to report civic issues while assisting municipal officers through AI-powered duplicate detection, complaint management, and an intelligent chat assistant.

---

# Tech Stack

- Python
- Flask
- SQLAlchemy ORM
- MySQL
- Flask-Migrate
- JWT Authentication
- Google Gemini API
- Google Gemini Embedding API
- LangGraph
- FAISS
- bcrypt

---
# Monolithic Architecture

The backend is implemented as a modular monolithic architecture, where all modules are deployed as a single application while remaining logically separated into independent components. This architecture was chosen because the application's modules are closely related and share a common database and business domain, making development, testing, deployment, and transaction management simpler. At the same time, the system follows a modular design through layered architecture and separation of concerns, allowing individual modules to be extracted into microservices in the future if scalability or independent deployment becomes necessary.

# Layered Architecture

The backend follows a layered architecture to ensure scalability, maintainability, and separation of concerns.

```
Routes
    │
Controllers
    │
Services
    │
Repositories
    │
Database
```

### Design Decisions

- Business logic is isolated in the Service layer.
- Controllers only coordinate requests and responses.
- Database operations are performed exclusively through Repository classes.
- SQLAlchemy models are never accessed directly from Controllers.
- Shared exception handling is implemented globally.
- Common API responses are standardized across all modules.

---

# Authentication Module

## Overview

JWT-based authentication secures all protected APIs while supporting secure session management using Access Tokens and Refresh Tokens.

## Key Design Decisions

- JWT Authentication is implemented using Access Tokens and Refresh Tokens.
- Access Tokens are returned in API responses.
- Refresh Tokens are stored as HTTP-only cookies.
- Refresh Tokens are hashed using SHA-256 before database storage.
- Plain Refresh Tokens are never persisted.
- Passwords are securely hashed using bcrypt.
- Only one active Refresh Token is maintained per user.
- Every login revokes previously active Refresh Tokens.
- Citizens can self-register.
- Municipal Officers and Department Officers are created only by the administrator.
- Global exception handling provides consistent API error responses.
- Request validation is separated from business logic.
- Role-Based Access Control (RBAC) restricts API access based on user roles.

---

# Complaint Module

## Overview

Citizens can register and monitor civic complaints through secured APIs.

Each complaint represents an individual citizen report and is uniquely identified using a complaint number.

## Key Design Decisions

- Complaint numbers are generated automatically.
- Every complaint belongs to the authenticated citizen.
- Complaint ownership is verified before allowing access.
- Geographic coordinates (Latitude and Longitude) are stored for every complaint.
- Complaint creation and complaint processing are intentionally separated.
- Complaint information serves as input for duplicate detection.
- Validation is performed before business logic execution.

---

# Duplicate Detection Module

## Overview

The Duplicate Detection module prevents multiple issues from being created for the same real-world civic problem.

Instead of treating every complaint as a new issue, semantically similar complaints are grouped under a single Issue.

## Key Design Decisions

- Duplicate detection is performed against Issues rather than Complaints.
- Google Gemini Embedding API (`gemini-embedding-001`) generates semantic embeddings.
- FAISS performs efficient nearest-neighbor similarity search.
- Issue embeddings are stored persistently after issue creation.
- Only newly submitted complaints require embedding generation.
- Similarity Threshold determines whether an Issue should be reused.
- Duplicate complaints increase the Issue Report Count.
- Individual complaints remain preserved for citizen tracking.
- Semantic similarity is used instead of keyword matching.

---

# Issue Module

## Overview

Issues represent unique civic problems identified from one or more citizen complaints.

Multiple complaints may reference the same Issue.

## Key Design Decisions

- Issues are independent of complaints.
- Multiple complaints can be linked to a single Issue.
- Every Issue receives a unique Issue Number.
- Municipal Officers review newly created Issues.
- Department assignment occurs at the Issue level.
- Department Officers update Issue status until resolution.
- Report Count reflects the number of affected citizens.

---

# Dashboard Module

## Overview

Role-specific dashboards provide summarized operational insights.

Implemented dashboards:

- Citizen Dashboard
- Municipal Officer Dashboard
- Department Officer Dashboard

## Key Design Decisions

- Dashboard statistics are generated using aggregate SQL queries.
- Dashboard data is filtered according to the authenticated user's role.
- RBAC prevents unauthorized dashboard access.
- Only required summary data is returned to improve performance.

---

# AI Chat Assistant Module

## Overview

The AI Chat Assistant enables citizens to interact with CivicPulse using natural language.

The chatbot is implemented as a **Skill-Based Agent** using **LangGraph**.

Rather than allowing the LLM to make business decisions, backend services execute all application logic while Gemini generates user-friendly responses.

## Supported Skills

- Complaint Status
- Municipal Policy Query
- Complaint Registration Guidance
- General Assistance

## Key Design Decisions

- LangGraph orchestrates the complete conversational workflow.
- User requests are routed using rule-based intent detection.
- Each business capability is implemented as an independent Skill.
- Skills communicate with backend services through Tool classes.
- Google Gemini API is responsible only for response generation.
- Business logic is never delegated to the LLM.
- Complaint retrieval, authorization, SLA evaluation, notification triggering, and policy retrieval are deterministic backend operations.
- Session-level conversational context is maintained using LangGraph MemorySaver.
- Persistent conversation storage was intentionally not implemented because only session-level context is required.
- Each conversation is isolated using a unique Thread ID.
- New skills can be introduced without modifying existing chatbot functionality.

---

# Retrieval-Augmented Generation (RAG)

## Overview

The RAG module enables the chatbot to answer municipal policy questions using dynamically retrieved policy documents.

## Key Design Decisions

- Municipal policies are maintained outside application code.
- Policies are converted into vector embeddings using Google Gemini Embedding API.
- FAISS stores policy embeddings for efficient semantic retrieval.
- Original policy documents are stored separately because FAISS stores only vectors.
- Policy embeddings are generated once and persisted.
- User queries are embedded and matched against the FAISS index.
- Retrieved policy context is supplied to Gemini.
- Dynamic retrieval reduces hallucinations and improves maintainability.

---

# Dashboard Security

The application enforces Role-Based Access Control.

### Citizen

- Register
- Login
- Submit Complaints
- View Own Complaints
- Chat with AI Assistant

### Municipal Officer

- Review Issues
- Assign Departments
- View Municipal Dashboard

### Department Officer

- View Assigned Issues
- Update Issue Status
- View Department Dashboard

---

# Master Data

The following master data is seeded during application setup.

### Roles

- Citizen
- Municipal Officer
- Department Officer

### Departments

- Roads
- Drainage
- Water Supply
- Solid Waste Management
- Street Lighting

### Categories

- Road Damage
- Garbage Overflow
- Water Leakage
- Drainage Issue
- Street Light Failure

---

# API Design Principles

- Layered Architecture
- Repository Pattern
- Service Layer Pattern
- Role-Based Access Control
- JWT Authentication
- Standardized API Responses
- Global Exception Handling
- Request Validation
- Separation of Concerns
- Modular Design
- AI-assisted Duplicate Detection
- Retrieval-Augmented Generation
- Skill-Based Agent Architecture

---

# Future Enhancements

- Automatic complaint categorization using AI.
- AI-assisted department assignment.
- Complaint priority prediction.
- Multilingual chatbot support.
- Voice-enabled complaint registration.
- Real-time notification services.
- Conversation persistence using Redis or Database-backed memory.
- Analytics and reporting dashboards.