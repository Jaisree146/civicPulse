resource "aws_ecr_repository" "backend" {
  name = "civicpulse-backend"

  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project     = "CivicPulse"
    Environment = "Development"
  }
}