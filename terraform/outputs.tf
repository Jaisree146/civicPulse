output "ecr_repository_url" {
  value = aws_ecr_repository.backend.repository_url
}
output "rds_endpoint" {
  value = aws_db_instance.mysql.endpoint
}

output "database_name" {
  value = aws_db_instance.mysql.db_name
}

output "cloudfront_url" {
  description = "CloudFront Distribution URL"
  value       = "https://${aws_cloudfront_distribution.frontend.domain_name}"
}
output "alb_dns_name" {
  value = aws_lb.backend.dns_name
}

output "target_group_arn" {
  value = aws_lb_target_group.backend.arn
}