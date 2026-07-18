# CivicPulse Frontend

Frontend application for **CivicPulse**, an AI-Powered Municipal Complaint Management System that enables citizens to report civic issues while providing municipal and department officers with AI-assisted complaint management.

---

# Tech Stack

- React 19
- TypeScript
- Vite
- React Router DOM
- TanStack Query
- Axios
- React Hook Form
- Zod
- Tailwind CSS
- Lucide React
- React Hot Toast

---

# Features

### Authentication
- Citizen Login
- Municipal Officer Login
- Department Officer Login
- JWT Authentication
- Persistent Login

### Complaint Management
- Submit Complaint
- Complaint History
- Complaint Details

### Issue Management
- Pending Review
- Department Assignment
- Department Issues
- Update Issue Status

### AI Assistant
- Complaint Status Assistant
- Policy-based Responses

---

# Frontend Architecture

The application follows a **Feature-Based Architecture** to improve modularity, scalability, and maintainability.

```text
src
│
├── api
├── assets
├── components
├── constants
├── contexts
├── features
├── hooks
├── layouts
├── pages
├── routes
├── services
├── types
├── utils
└── validations
```

Each feature owns its own

- Components
- Hooks
- API functions
- Types
- Validation
- Pages

This reduces coupling and keeps related functionality together.

---

# Architecture Decisions

## React + TypeScript

Chosen to build a scalable, maintainable and type-safe application.

### Benefits

- Compile-time type checking
- Better IDE support
- Easier refactoring
- Improved code quality

---

## Vite

Used as the build tool because it provides

- Fast startup
- Hot Module Replacement (HMR)
- Optimized production builds

---

## Feature-Based Folder Structure

Instead of organizing files by type, the application is organized by business features.

Example

```text
features
│
├── auth
├── complaints
├── issues
├── chatbot
└── profile
```

### Decision

- Better scalability
- Easier maintenance
- High cohesion
- Low coupling

---

## React Router

React Router is used for client-side routing.

### Decision

- Nested layouts
- Protected routes
- Role-based navigation
- Lazy page navigation

---

## TanStack Query

Used for server-state management.

### Decisions

- Request caching
- Automatic refetching
- Cache invalidation
- Mutation handling
- Background synchronization
- Reduced boilerplate

Application data is always fetched from the server instead of being duplicated in local state.

---

## Axios

Axios is used as the HTTP client.

### Decisions

- Centralized API client
- Request interceptors
- Response interceptors
- Automatic token refresh
- Global error handling

---

## React Context

React Context manages authentication state.

Stores

- Current user
- Access token
- Authentication status

### Decision

Authentication state is shared globally without introducing additional state-management libraries.

---

## Authentication Strategy

### JWT Authentication

Two-token strategy

- Access Token
- Refresh Token

---

## Access Token Storage

Access Tokens are stored only in **memory** using React Context.

### Decision

- No Local Storage
- No Session Storage
- Reduces token exposure
- Cleared automatically after browser close

---

## Refresh Token Storage

Refresh Tokens are stored as **HttpOnly Secure Cookies**.

### Decision

- Not accessible through JavaScript
- Helps mitigate XSS attacks
- Automatically sent by the browser

---

## Automatic Token Refresh

When the Access Token expires

```text
Request
    │
401 Unauthorized
    │
Axios Interceptor
    │
Refresh Endpoint
    │
New Access Token
    │
Retry Original Request
```

### Decision

Provides seamless user experience without requiring repeated logins.

---

## Route Protection

Protected routes ensure

- Only authenticated users access secured pages
- Unauthorized users are redirected to Login

---

## Role-Based Authorization

Each role has access only to permitted pages.

### Citizen

- Dashboard
- Submit Complaint
- Complaint History
- AI Assistant
- Profile

### Municipal Officer

- Dashboard
- Pending Issues
- Department Assignment
- Issue Details
- Profile

### Department Officer

- Dashboard
- Assigned Issues
- Update Issue Status
- Profile

Role information is obtained from the authenticated user.

---

## Form Management

React Hook Form is used for form state.

### Decisions

- Minimal re-renders
- Better performance
- Cleaner form handling

---

## Validation

Zod provides schema-based validation.

### Decisions

- Runtime validation
- Type-safe forms
- Shared validation rules

---

## API Layer

Business logic is separated from UI.

```text
Component
     │
Hook
     │
API
     │
Axios
     │
Backend
```

### Decision

- Better separation of concerns
- Reusable APIs
- Easier testing

---

## UI Design

Tailwind CSS is used for styling.

### Decisions

- Utility-first approach
- Responsive layouts
- Consistent design system
- Faster development

Lucide React provides lightweight SVG icons.

---

# Environment Variables

```env
VITE_API_BASE_URL=http://localhost:5000/api
```

---

# Installation

```bash
git clone <repository-url>

cd civicpulse-frontend

npm install
```

---

# Running

Development

```bash
npm run dev
```

Production Build

```bash
npm run build
```

Preview

```bash
npm run preview
```

---

# Authentication Flow

```text
Login
   │
   ▼
Access Token
   │
React Context
   │
Protected Routes
   │
API Requests
   │
Access Token Expired
   │
Axios Interceptor
   │
Refresh Token Cookie
   │
Generate New Access Token
   │
Retry Request
```

---

# Current Features

- User Authentication
- Persistent Login
- Route Protection
- Role-Based Authorization
- Complaint Management
- Issue Management
- AI Assistant
- Profile Management

---

# Future Enhancements

- Real-time Notifications
- WebSocket Integration
- Interactive GIS Maps
- Progressive Web App (PWA)

---

# License

Developed as part of the **Presidio Prime Internship Capstone Project**.