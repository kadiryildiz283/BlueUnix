import os
from celery import Celery

# Redis URL'ini ortam değişkenlerinden al, yoksa varsayılanı kullan
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "blueunix_worker",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

# Task'ların (görevlerin) bulunacağı modülleri tanımla
celery_app.conf.imports = (
    "app.services.opnsense_svc",  # OPNsense görevleri burada olacak
    "app.services.terraform_svc", # <--- Bunu ekle
"app.services.ansible_svc",   # <--- BU SATIRIN OLDUĞUNA EMİN MİSİN?
    )

# Ayarlar
celery_app.conf.task_routes = {
    "app.services.opnsense_svc.*": {"queue": "network_ops"}, # Ağ işlerini ayrı kuyruğa at
}
