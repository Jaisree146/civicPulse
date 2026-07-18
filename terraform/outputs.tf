output "ecr_repository_url" {
  value = aws_ecr_repository.backend.repository_url
}
output "rds_endpoint" {
  value = aws_db_instance.mysql.endpoint
}

output "database_name" {
  value = aws_db_instance.mysql.db_name
}