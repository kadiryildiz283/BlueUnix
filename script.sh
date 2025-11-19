#!/bin/bash

PROJECT_NAME="BlueUnix"

echo "🚀 $PROJECT_NAME proje yapısı oluşturuluyor..."

# Ana Dizin
mkdir -p $PROJECT_NAME

# --- Backend ---
echo "📂 Backend yapısı kuruluyor..."
mkdir -p $PROJECT_NAME/backend/app/{api,core,db,services,workers}
touch $PROJECT_NAME/backend/Dockerfile
touch $PROJECT_NAME/backend/requirements.txt
touch $PROJECT_NAME/backend/app/__init__.py
touch $PROJECT_NAME/backend/app/main.py

# Backend Services Files
touch $PROJECT_NAME/backend/app/services/__init__.py
touch $PROJECT_NAME/backend/app/services/terraform_svc.py
touch $PROJECT_NAME/backend/app/services/ansible_svc.py
touch $PROJECT_NAME/backend/app/services/opnsense_svc.py

# --- Frontend ---
echo "📂 Frontend yapısı kuruluyor..."
mkdir -p $PROJECT_NAME/frontend/{public,src}
mkdir -p $PROJECT_NAME/frontend/src/{components,services,assets,views}
touch $PROJECT_NAME/frontend/Dockerfile
touch $PROJECT_NAME/frontend/package.json
touch $PROJECT_NAME/frontend/README.md

# --- Infrastructure (IaC) ---
echo "📂 Infrastructure (IaC) katmanı kuruluyor..."

# Terraform
mkdir -p $PROJECT_NAME/infrastructure/terraform/{modules,providers}
touch $PROJECT_NAME/infrastructure/terraform/main.tf
touch $PROJECT_NAME/infrastructure/terraform/variables.tf
touch $PROJECT_NAME/infrastructure/terraform/outputs.tf

# Ansible
mkdir -p $PROJECT_NAME/infrastructure/ansible/{inventory,playbooks,roles,templates}
touch $PROJECT_NAME/infrastructure/ansible/ansible.cfg

# Ansible Roles (Örnek yapılar)
mkdir -p $PROJECT_NAME/infrastructure/ansible/roles/wazuh-agent/{tasks,handlers,templates}
mkdir -p $PROJECT_NAME/infrastructure/ansible/roles/wazuh-manager/{tasks,handlers,templates}
mkdir -p $PROJECT_NAME/infrastructure/ansible/roles/thehive/{tasks,handlers,templates}
mkdir -p $PROJECT_NAME/infrastructure/ansible/roles/windows-gpo/{tasks,handlers,templates}

# Golden Images
mkdir -p $PROJECT_NAME/infrastructure/golden-images/{wazuh-server,thehive}

# --- Root Files ---
touch $PROJECT_NAME/docker-compose.yml
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/.gitignore

echo "✅ $PROJECT_NAME başarıyla oluşturuldu!"
echo "👉 Dizin: ./$PROJECT_NAME"
