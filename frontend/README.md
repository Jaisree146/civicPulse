# CivicPulse Frontend

Frontend application for **CivicPulse**, an AI-powered Municipal Complaint Management System.

## Tech Stack

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

## Features

### Authentication

- Citizen Registration
- User Login
- JWT Authentication
- Access Token Refresh
- HttpOnly Refresh Token Cookies
- Route Protection
- Role-based Authorization
- Persistent Login on Refresh

---
## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
npm install
```

Run the application

```bash
npm run dev
```

---

## Available Scripts

Start development server

```bash
npm run dev
```

Build production bundle

```bash
npm run build
```

Preview production build

```bash
npm run preview
```

Lint project

```bash
npm run lint
```

---

## Authentication Flow

```
Login
    │
    ▼
Access Token
    │
    ▼
Auth Context
    │
    ▼
Protected Routes
    │
    ▼
Page Refresh
    │
    ▼
Refresh Token (HttpOnly Cookie)
    │
    ▼
New Access Token
```

---

## Current Modules

- Authentication
- Route Protection
- Role-based Authorization

---

## License

This project is developed for educational and internship purposes.