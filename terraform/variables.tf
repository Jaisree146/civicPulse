variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-south-1"
}

variable "env" {
  type = string
}

variable "debug" {
  type = string
}

variable "secret_key" {
  type      = string
  sensitive = true
}

variable "db_host" {
  type = string
}

variable "db_port" {
  type = string
}

variable "db_name" {
  type = string
}

variable "db_user" {
  type = string
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "jwt_secret_key" {
  type      = string
  sensitive = true
}

variable "jwt_access_expiry" {
  type = string
}

variable "jwt_refresh_secret_key" {
  type      = string
  sensitive = true
}

variable "jwt_refresh_days" {
  type = string
}

variable "gemini_api_key" {
  type      = string
  sensitive = true
}

variable "frontend_url" {
  type = string
}

variable "frontend_bucket_name" {
  type = string
}