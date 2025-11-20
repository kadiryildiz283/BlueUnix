from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List
from app.services.opnsense_svc import task_create_alias
from app.services.terraform_svc import task_apply_infrastructure
from app.services.ansible_svc import task_run_ansible_playbook
from fastapi.middleware.cors import CORSMiddleware # <--- EKLE 1

app = FastAPI(title="BlueUnix Core", version="0.2.0")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veri Modeli (Gelen isteğin şekli)
class AliasRequest(BaseModel):
    name: str
    ips: List[str]

@app.get("/")
def read_root():
    return {"sistem": "BlueUnix", "durum": "Hazir"}

@app.post("/network/alias")
def create_firewall_alias(request: AliasRequest):
    """
    OPNsense üzerinde yeni bir Alias (IP Listesi) oluşturur.
    İşlem arka planda (Celery) yapılır.
    """
    # Celery Task'ını tetikle (.delay() asenkron çalıştırır)
    task = task_create_alias.delay(request.name, request.ips)
    
    return {
        "mesaj": "Alias oluşturma emri alındı.",
        "task_id": task.id,
        "durum": "İşleniyor..."
    }

@app.post("/infrastructure/apply")
def apply_infrastructure():
    """
    Terraform'u tetikler ve altyapıyı kurar.
    """
    task = task_apply_infrastructure.delay()
    return {
        "mesaj": "Altyapı kurulum işlemi başlatıldı.",
        "task_id": task.id
    }

@app.post("/configuration/apply")
def apply_configuration():
    """
    Ansible Playbook'unu tetikler.
    """
    task = task_run_ansible_playbook.delay()
    return {
        "mesaj": "Konfigürasyon yönetimi başlatıldı.",
        "task_id": task.id
    }
