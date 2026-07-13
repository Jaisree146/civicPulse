class Roles:
    CITIZEN = "Citizen"
    MUNICIPAL_OFFICER = "Municipal Officer"
    DEPARTMENT_OFFICER = "Department Officer"


class TokenType:
    ACCESS = "access"
    REFRESH = "refresh"
    
class ComplaintStatus:

    SUBMITTED = "Submitted"


class IssueStatus:

    PENDING_REVIEW = "Pending Review"

    ASSIGNED = "Assigned"

    IN_PROGRESS = "In Progress"

    RESOLVED = "Resolved"

    CLOSED = "Closed"


class Priority:

    LOW = "Low"

    MEDIUM = "Medium"

    HIGH = "High"

    CRITICAL = "Critical"
    
class NumberPrefix:

    COMPLAINT = "CP"

    ISSUE = "ISS"