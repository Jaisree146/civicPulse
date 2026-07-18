resource "aws_ecs_cluster" "backend" {
  name = "civicpulse-cluster"
}

resource "aws_ecs_task_definition" "backend" {
  family                   = "civicpulse-backend"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"

  cpu    = "256"
  memory = "512"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name = "backend"

      image = "${aws_ecr_repository.backend.repository_url}:latest"

      essential = true

      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
          protocol      = "tcp"
        }
      ]

      environment = [
        { name = "ENV", value = var.env },
        { name = "DEBUG", value = var.debug },
        { name = "SECRET_KEY", value = var.secret_key },

        { name = "DB_HOST", value = var.db_host },
        { name = "DB_PORT", value = var.db_port },
        { name = "DB_NAME", value = var.db_name },
        { name = "DB_USER", value = var.db_user },
        { name = "DB_PASSWORD", value = var.db_password },

        { name = "JWT_SECRET_KEY", value = var.jwt_secret_key },
        { name = "JWT_ACCESS_TOKEN_EXPIRY_MINUTES", value = var.jwt_access_expiry },

        { name = "JWT_REFRESH_SECRET_KEY", value = var.jwt_refresh_secret_key },
        { name = "JWT_REFRESH_TOKEN_EXPIRY_DAYS", value = var.jwt_refresh_days },

        { name = "GEMINI_API_KEY", value = var.gemini_api_key },
        { name = "FRONTEND_URL", value = var.frontend_url }
      ]

      logConfiguration = {
        logDriver = "awslogs"

        options = {
          awslogs-group         = aws_cloudwatch_log_group.backend.name
          awslogs-region        = "ap-south-1"
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

resource "aws_ecs_service" "backend" {
  name            = "civicpulse-backend-service"
  cluster         = aws_ecs_cluster.backend.id
  task_definition = aws_ecs_task_definition.backend.arn

  desired_count = 1
  launch_type   = "FARGATE"

  lifecycle {
    ignore_changes = [
      task_definition
    ]
  }

  network_configuration {
    subnets = [
      aws_subnet.public.id
    ]

    security_groups = [
      aws_security_group.backend_sg.id
    ]

    assign_public_ip = true
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecs_task_execution_role_policy
  ]
}