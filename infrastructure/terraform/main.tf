terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Hedef: Şirket Uygulama Sunucusu (Python tabanlı bir Linux)
resource "docker_image" "app_server" {
  name         = "python:3.10-slim-bookworm"
  keep_locally = false
}

resource "docker_container" "corporate_server" {
  image = docker_image.app_server.image_id
  name  = "blueunix_target_server"
  
  # Konteynerin hemen kapanmaması için sonsuz döngü komutu
  command = ["tail", "-f", "/dev/null"]
}
