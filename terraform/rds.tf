resource "aws_db_subnet_group" "civicpulse" {

  name = "civicpulse-db-subnet-group"

  subnet_ids = [
    aws_subnet.public.id,
    aws_subnet.public2.id
  ]

  tags = {
    Name = "civicpulse-db-subnet-group"
  }
}

resource "aws_db_instance" "mysql" {

  identifier = "civicpulse-db"

  engine         = "mysql"
  engine_version = "8.0"

  instance_class = "db.t4g.micro"

  allocated_storage = 20
  storage_type      = "gp3"

  db_name  = "civicpulse"
  username = var.db_user
  password = var.db_password

  db_subnet_group_name = aws_db_subnet_group.civicpulse.name

  vpc_security_group_ids = [
    aws_security_group.rds_sg.id
  ]

  publicly_accessible = true

  skip_final_snapshot = true

  deletion_protection = false

  tags = {
    Name = "civicpulse-db"
  }
}