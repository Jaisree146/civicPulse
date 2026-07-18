resource "aws_cloudwatch_log_group" "backend" {
  name              = "/ecs/civicpulse-backend"
  retention_in_days = 7

  tags = {
    Name = "civicpulse-backend-logs"
  }
}