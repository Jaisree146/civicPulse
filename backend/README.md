## Authentication Module

## 1. Layered Architecture

* Followed a layered architecture:

  * Routes
  * Controllers
  * Services
  * Repositories
  * Models
* Business logic is implemented in the Service layer.
* Database operations are handled only by the Repository layer.


## 2. Repository Pattern

* Controllers and Services do not access SQLAlchemy models directly.
* All database operations are performed through repositories.



## 3. Authentication Mechanism

* JWT is used for authentication.
* Two tokens are generated:

  * Access Token
  * Refresh Token


## 4. Token Storage Strategy

* Access Token is returned in the API response.
* Refresh Token is stored as an HTTP-only cookie.
* Refresh Token is never exposed to frontend JavaScript.



## 5. Refresh Token Persistence

* Refresh Tokens are stored in the database.
* Only the SHA-256 hash of the refresh token is stored.
* Plain refresh tokens are never stored.



## 6. Password Security

* User passwords are hashed using bcrypt before storing.
* Plain text passwords are never stored in the database.



## 7. Single Active Session

* Only one active refresh token is allowed per user.
* On every new login:

  * Existing active refresh token is revoked.
  * A new refresh token is generated and stored.



## 8. Role Management

* Citizens can self-register.
* Municipal Officers and Department Officers cannot self-register.
* Officer accounts are created by the Admin.
* Roles are predefined in the database.



## 9. Standard API Response

* All APIs follow a common response format.

Success Response:

```json
{
    "success": true,
    "message": "...",
    "data": {}
}
```

Error Response:

```json
{
    "success": false,
    "message": "...",
    "error_code": "...",
    "errors": {}
}
```



## 10. Global Exception Handling

* Introduced a Global Exception Handler.
* Created a base `AppException`.
* Module-specific exceptions inherit from `AppException`.
* Controllers do not contain repetitive exception handling code.



## 11. Request Validation

* Request validation is performed before entering the Service layer.
* Validation logic is separated from business logic.


## 12. Authorization

* Role-Based Access Control (RBAC) will be used.
* Authentication verifies user identity.
* Authorization will determine access based on user roles.


## 13. HTTP Status Codes

* Standard HTTP status codes are used consistently.
* Example:

  * 200 - OK
  * 201 - Created
  * 400 - Bad Request
  * 401 - Unauthorized
  * 404 - Not Found
  * 409 - Conflict
  * 500 - Internal Server Error

# Complaint Module

## 1. Complaint Creation

* Citizens can submit complaints through a secured API.
* Every complaint is associated with the authenticated citizen.
* Each complaint is assigned a unique complaint number (e.g., `CP000001`).

---

## 2. Complaint Information

Each complaint contains:

* Complaint Number
* Title
* Description
* Latitude
* Longitude
* Status
* Processed Flag
* Created At
* Updated At

---

## 3. Complaint Tracking

Implemented APIs to:

* Create a complaint
* View all complaints submitted by the authenticated citizen
* View a specific complaint by its ID

---

## 4. Complaint Ownership

* Citizens can access only their own complaints.
* Unauthorized access to another citizen's complaint is restricted.

---

## 5. Request Validation

The following validations are performed before processing a complaint:

* Required field validation
* Title length validation
* Description length validation
* Latitude validation
* Longitude validation

---

## 6. Business Logic

The Service layer is responsible for:

* Generating unique complaint numbers
* Creating complaints
* Retrieving citizen complaints
* Retrieving complaint details
* Validating complaint ownership

---

## 7. Repository Operations

The Complaint Repository provides:

* Create Complaint
* Get Latest Complaint
* Get Complaint by ID
* Get Complaints by Citizen ID
* Update Complaint

---

## 8. API Endpoints

| Method | Endpoint                         | Description                                          |
| ------ | -------------------------------- | ---------------------------------------------------- |
| POST   | `/api/complaints`                | Create a new complaint                               |
| GET    | `/api/complaints/my`             | Retrieve all complaints of the authenticated citizen |
| GET    | `/api/complaints/{complaint_id}` | Retrieve details of a specific complaint             |

---

## 9. Security

* JWT Authentication is required for all Complaint APIs.
* Role-Based Access Control (RBAC) is enforced.
* Complaint ownership is verified before returning complaint details.

---
## Issue Module

1. Issue Management
Issues represent unique civic problems identified from one or more complaints.
Each issue is assigned a unique issue number (e.g., ISS000001).
Multiple complaints can be linked to the same issue.
2. Issue Information

Each issue contains:

Issue Number
Category
Department
Summary
Priority
Status
Report Count
Created At
Updated At

3. Issue Workflow
Newly created issues are marked as Pending Review.
Municipal Officers review and assign issues to departments.
Department Officers update the issue status until resolution.

4. Business Logic
The Service layer is responsible for:

Creating issues
Generating unique issue numbers
Assigning departments
Updating issue status
Incrementing report count
Retrieving issues by department

5. Repository Operations
The Issue Repository provides:

Create Issue
Get Latest Issue
Get Issue by ID
Get All Issues
Get Pending Review Issues
Get Issues by Department
Update Issue

6. API Endpoints
Method	        Endpoint	                     Description
GET	          api/issues	             Retrieve all issues (Municipal Officer)
GET	         /api/issues/pending	     Retrieve issues pending review
GET	         /api/issues/{issue_id}	   Retrieve issue details
GET	         /api/issues/my	           Retrieve issues assigned to the logged-in department
PUT	    /api/issues/{issue_id}/assign  Assign issue to a department
PUT	    /api/issues/{issue_id}/status	 Update issue status

7. Security
JWT Authentication is required.
Municipal Officers can:
View all issues
View pending issues
Assign departments
Department Officers can:
View assigned issues
Update issue status

## Dashboard Module

1. Dashboard Overview

The Dashboard module provides summarized statistics based on the authenticated user's role.

Three dashboards are implemented:

Citizen Dashboard
Municipal Officer Dashboard
Department Officer Dashboard
2. Citizen Dashboard

Displays:

Total Complaints
Resolved Complaints
Five most recent complaints
3. Municipal Dashboard

Displays:

Total Issues
Pending Review Issues
4. Department Dashboard

Displays:

Assigned Issues
Resolved Issues
5. Database Queries

Dashboard statistics are generated using:

SQLAlchemy ORM
Aggregate Functions (COUNT)
JOIN operations
Filtering
Ordering
Limiting results

6. API Endpoints
Method	     Endpoint	                  Description
GET	    /api/dashboard/citizen	    Citizen dashboard
GET	    /api/dashboard/municipal	  Municipal Officer dashboard
GET	    /api/dashboard/department	  Department Officer dashboard

7. Security
JWT Authentication is required.
Dashboard access is restricted using Role-Based Access Control (RBAC).
Each role can access only its respective dashboard.
Master Data
1. Roles

The following roles are predefined:

Citizen
Municipal Officer
Department Officer

2. Departments

Departments are pre-populated using seed scripts.

Examples include:

Roads
Drainage
Water Supply
Solid Waste Management
Street Lighting

3. Categories

Complaint categories are also seeded.

Examples include:

Road Damage
Garbage Overflow
Water Leakage
Drainage Issue
Street Light Failure

4. Seed Scripts

Implemented database seed scripts for:

Roles
Departments
Categories