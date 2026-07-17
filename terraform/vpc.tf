resource "aws_vpc" "civicpulse" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "civicpulse-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.civicpulse.id

  tags = {
    Name = "civicpulse-igw"
  }
}

# -----------------------------
# Existing Public Subnet
# -----------------------------

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.civicpulse.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-south-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "civicpulse-public-subnet"
  }
}

# -----------------------------
# NEW Public Subnet
# -----------------------------

resource "aws_subnet" "public2" {
  vpc_id                  = aws_vpc.civicpulse.id
  cidr_block              = "10.0.4.0/24"
  availability_zone       = "ap-south-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "civicpulse-public-subnet-2"
  }
}

# -----------------------------
# Existing Private Subnets
# -----------------------------

resource "aws_subnet" "private1" {
  vpc_id            = aws_vpc.civicpulse.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "ap-south-1a"

  tags = {
    Name = "civicpulse-private-subnet-1"
  }
}

resource "aws_subnet" "private2" {
  vpc_id            = aws_vpc.civicpulse.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "ap-south-1b"

  tags = {
    Name = "civicpulse-private-subnet-2"
  }
}

# -----------------------------
# Route Table
# -----------------------------

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.civicpulse.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "civicpulse-public-route-table"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public2" {
  subnet_id      = aws_subnet.public2.id
  route_table_id = aws_route_table.public.id
}