####################################
# Application Load Balancer
####################################

resource "aws_lb" "backend" {

  name               = "civicpulse-alb"
  internal           = false
  load_balancer_type = "application"

  security_groups = [
    aws_security_group.alb_sg.id
  ]

  subnets = [
    aws_subnet.public.id,
    aws_subnet.public2.id
  ]
}

####################################
# Target Group
####################################

resource "aws_lb_target_group" "backend" {

  name        = "civicpulse-tg"
  port        = 5000
  protocol    = "HTTP"
  target_type = "ip"

  vpc_id = aws_vpc.civicpulse.id

  health_check {

    path = "/health"

    protocol = "HTTP"

    matcher = "200"

    interval = 30

    timeout = 5

    healthy_threshold = 2

    unhealthy_threshold = 2
  }
}

####################################
# Listener
####################################

resource "aws_lb_listener" "backend" {

  load_balancer_arn = aws_lb.backend.arn

  port = 80

  protocol = "HTTP"

  default_action {

    type = "forward"

    target_group_arn = aws_lb_target_group.backend.arn
  }
}