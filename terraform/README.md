# Terraform Infrastructure

This directory contains the Terraform configuration used to provision the AWS infrastructure for **CivicPulse**, an AI-powered Municipal Complaint Management System.

Terraform is responsible for provisioning and managing the cloud infrastructure, while application deployments are automated using GitHub Actions.

---

# Infrastructure Overview

The infrastructure provisions the following AWS resources:

- Amazon VPC
- Public and Private Subnets
- Internet Gateway
- Route Tables and Associations
- Security Groups
- Amazon ECS Cluster
- Amazon ECS Service (AWS Fargate)
- Amazon ECR Repository
- IAM Roles and Policies
- Amazon CloudWatch Log Group
- Amazon RDS MySQL Database
- Amazon S3 Bucket for Frontend Hosting

---

# Directory Structure

```
terraform/
│
├── provider.tf
├── variables.tf
├── outputs.tf
├── networking.tf
├── iam.tf
├── ecr.tf
├── ecs.tf
├── rds.tf
├── s3.tf
└── terraform.tfvars
```

---

# Prerequisites

Ensure the following are installed before using Terraform:

- Terraform (v1.5 or later)
- AWS CLI
- AWS Account
- IAM User with appropriate permissions

Configure AWS credentials:

```bash
aws configure
```

---

# Initialize Terraform

```bash
terraform init
```

---

# Validate Configuration

```bash
terraform validate
```

---

# Preview Infrastructure Changes

```bash
terraform plan
```

---

# Provision Infrastructure

```bash
terraform apply
```

When prompted, enter:

```
yes
```

---

# Destroy Infrastructure

To remove all provisioned resources:

```bash
terraform destroy
```

---

# Configuration

Infrastructure configuration values are defined in:

- `variables.tf`
- `terraform.tfvars`

Example:

```hcl
env          = "development"
db_name      = "civicpulse"
db_user      = "admin"
db_password  = "********"
frontend_url = "http://localhost:5173"
```

---

# Deployment Architecture

Terraform provisions the infrastructure only.

Application deployments are automated using **GitHub Actions**.

```
                    GitHub Repository
                           │
            ┌──────────────┴──────────────┐
            │                             │
     Backend Changes              Frontend Changes
            │                             │
            ▼                             ▼
     GitHub Actions                GitHub Actions
            │                             │
            ▼                             ▼
 Build Docker Image            Build React Application
            │                             │
            ▼                             ▼
 Push Image to Amazon ECR      Upload dist/ to Amazon S3
            │
            ▼
 Force New ECS Deployment
            │
            ▼
 Amazon ECS Fargate
```

---

# AWS Resources
| **AWS Resource**            | **Purpose**                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| Amazon VPC                  | Provides an isolated virtual network for all CivicPulse resources. |
| Public Subnets              | Hosts the ECS Fargate tasks with internet access.                  |
| Private Subnets             | Reserved for secure deployment of the Amazon RDS database.         |
| Internet Gateway            | Enables internet connectivity for resources in public subnets.     |
| Route Tables                | Defines routing rules for traffic within the VPC.                  |
| Security Groups             | Acts as virtual firewalls to control inbound and outbound traffic. |
| Amazon ECS Cluster          | Manages and orchestrates the backend containers.                   |
| Amazon ECS Service          | Maintains the desired number of running backend tasks.             |
| Amazon ECR Repository       | Stores Docker images for the backend application.                  |
| Amazon RDS (MySQL)          | Provides the managed relational database for the application.      |
| Amazon S3 Bucket            | Hosts the React frontend as a static website.                      |
| Amazon CloudWatch Log Group | Collects and stores backend application logs.                      |
| IAM Roles & Policies        | Grants secure permissions for ECS tasks to access AWS services.    |


---

# Deployment Workflow

Terraform is intended for infrastructure provisioning only.

Application deployments are handled separately:

### Backend

- Build Docker image
- Push image to Amazon ECR
- Trigger ECS Force New Deployment

### Frontend

- Build React application
- Upload `dist/` to Amazon S3

---

# Notes

- Terraform provisions and manages cloud infrastructure.
- Backend deployments are automated using GitHub Actions.
- Frontend deployments are automated using GitHub Actions.
- ECS pulls the latest Docker image from Amazon ECR during deployment.
- CloudWatch is used for backend application logs.
- Infrastructure changes should be applied using Terraform, while application updates should be deployed through the CI/CD pipeline.

---

# Technologies Used

- Terraform
- AWS VPC
- Amazon ECS (Fargate)
- Amazon ECR
- Amazon RDS (MySQL)
- Amazon S3
- IAM
- CloudWatch
- GitHub Actions