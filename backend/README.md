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
