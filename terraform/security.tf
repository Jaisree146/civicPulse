resource "aws_security_group" "backend_sg" {

  name        = "civicpulse-backend-sg"
  description = "Backend Security Group"

  vpc_id = aws_vpc.civicpulse.id

  ingress {

    from_port = 5000
    to_port   = 5000
    protocol  = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  egress {

    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

resource "aws_security_group" "rds_sg" {

  name        = "civicpulse-rds-sg"
  description = "RDS Security Group"

  vpc_id = aws_vpc.civicpulse.id

  ingress {

    from_port = 3306
    to_port   = 3306
    protocol  = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }

  egress {

    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}