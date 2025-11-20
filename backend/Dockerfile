# Daha kararlı bir sürüm olan Bookworm (Debian 12) tabanını kullanalım
FROM python:3.10-slim-bookworm

WORKDIR /code

# 1. Gerekli temel araçları yükle (Sadece curl ve unzip yeterli)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# 2. Terraform'u Doğrudan İndir ve Kur (HashiCorp Repo'suyla uğraşmadan)
# Terraform sürümünü buraya yazıyoruz (Stabil sürüm)
ENV TERRAFORM_VERSION=1.9.5
RUN curl -LO "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" \
    && unzip "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" \
    && mv terraform /usr/local/bin/ \
    && rm "terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# 3. Python bağımlılıklarını yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kodu kopyala
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
