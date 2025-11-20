import ansible_runner
from celery import shared_task
from app.workers.celery_app import celery_app
import os

# Ansible dosyalarının Docker içindeki yolları
ANSIBLE_DIR = "/infrastructure/ansible"
INVENTORY_PATH = os.path.join(ANSIBLE_DIR, "inventory/hosts.yml")
PLAYBOOK_PATH = "setup_security.yml" # <--- GÜNCELLENDİ (Eskisi setup_web.yml idi)

@celery_app.task(name="run_ansible_playbook")
def task_run_ansible_playbook(playbook_name=PLAYBOOK_PATH):
    """
    Belirtilen Ansible Playbook'unu çalıştırır.
    """
    print(f"--- ANSIBLE: {playbook_name} Çalıştırılıyor ---")
    
    # Ansible Runner'ı çalıştır
    r = ansible_runner.run(
        private_data_dir=ANSIBLE_DIR,
        playbook=os.path.join("playbooks", playbook_name),
        inventory=INVENTORY_PATH,
        quiet=False  # Logları görmek istiyoruz
    )
    
    if r.status == 'successful':
        print(f"--- ANSIBLE BAŞARILI: {playbook_name} ---")
        return {"status": "success", "stats": r.stats}
    else:
        print(f"--- ANSIBLE HATASI: {r.status} ---")
        return {"status": "failed", "rc": r.rc}
