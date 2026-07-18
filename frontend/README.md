# CivicPulse Frontend

Frontend application for **CivicPulse**, an AI-Powered Municipal Complaint Management System that enables citizens to report civic issues while providing municipal officers with AI-assisted complaint management and monitoring.

---

# Tech Stack

* React 19
* TypeScript
* Vite
* React Router DOM
* TanStack Query
* Axios
* React Hook Form
* Zod
* Tailwind CSS
* Lucide React
* React Hot Toast

---

# Modules

* Authentication
* Dashboard
* Complaint Management
* Issue Management
* AI Chat Assistant
* Route Protection
* Role-based Authorization

---

# Architecture Decisions

## React + TypeScript

Used to build a scalable, type-safe frontend with improved maintainability and developer productivity.

---

## Vite

Chosen for fast development startup, hot module replacement, and optimized production builds.

---

## TanStack Query

Used for server state management.

### Decisions

* Automatic request caching
* Background refetching
* Request deduplication
* Mutation handling
* Automatic cache invalidation
* Reduced manual state management

---

## Axios

Used as the HTTP client because it provides

* Request/Response interceptors
* Centralized API configuration
* Better error handling
* Automatic JSON parsing

---

## React Hook Form + Zod

Used for form handling and validation.

### Decisions

* Minimal re-renders
* Schema-based validation
* Type-safe form data
* Better user experience with instant validation

---

## Authentication Strategy

### JWT Authentication

* Access Token for API authorization
* Refresh Token for session renewal

### Access Token Storage

Access Tokens are stored **only in memory** using React Context.

**Decision**

* Prevents persistent storage of tokens.
* Eliminates risks associated with Local Storage.

### Refresh Token Storage

Refresh Tokens are stored as **HttpOnly Secure Cookies**.

**Decision**

* Cannot be accessed through JavaScript.
* Helps mitigate XSS attacks.
* Automatically included with authenticated requests.

---

## Automatic Token Refresh

When an Access Token expires

1. Request fails with Unauthorized.
2. Axios interceptor calls the refresh endpoint.
3. Backend validates Refresh Token.
4. New Access Token is issued.
5. Original request is retried automatically.

This provides persistent login without requiring users to log in again after refreshing the page.

---

## Route Protection

Protected routes ensure that

* Unauthenticated users cannot access secured pages.
* Authenticated users are redirected appropriately.

---

## Role-Based Authorization

Different dashboards are rendered based on user roles.

### Citizen

* Submit complaints
* View complaint history
* Interact with AI Assistant

### Officer

* View department issues
* Manage complaints
* Update issue status

Authorization is enforced using the role information included in the Access Token.

---

## API Layer

API calls are separated from UI components.

Benefits

* Reusable API functions
* Easier testing
* Better maintainability
* Clear separation of concerns

---

## Folder Structure

The project follows feature-based organization.

```text
src/
│
├── api/
├── components/
├── contexts/
├── hooks/
├── pages/
├── routes/
├── services/
├── types/
├── utils/
└── validations/
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd civicpulse-frontend
```

Install dependencies

```bash
npm install
```

---

# Environment Variables

Create a `.env` file.

```env
VITE_API_BASE_URL=http://localhost:5000/api
```

---

# Running the Application

Development

```bash
npm run dev
```

Production Build

```bash
npm run build
```

Preview Production Build

```bash
npm run preview
```

---

# Authentication Flow

```text
User Login
      │
      ▼
Receive Access Token
      │
      ▼
Store in React Context
      │
      ▼
Access Protected Routes
      │
      ▼
Access Token Expires
      │
      ▼
Refresh Token Cookie
      │
      ▼
Generate New Access Token
      │
      ▼
Retry Original Request
```

---

# Current Features

* Citizen Registration
* User Login
* JWT Authentication
* Persistent Login
* Route Protection
* Role-based Authorization
* Dashboard
* Complaint Management
* Issue Management
* AI Chat Assistant

---

# Future Enhancements

* Real-time Notifications
* WebSocket Integration
* Interactive GIS Maps
* Progressive Web App (PWA)

---

# License

This project is developed as part of the **Presidio Prime Internship Capstone Project** for educational and internship purposes.
