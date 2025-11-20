from python_terraform import Terraform
from celery import shared_task
from app.workers.celery_app import celery_app
import os

# Terraform dosyalarının Docker içindeki yolu (Compose'da mount etmiştik)
TF_WORKING_DIR = "/infrastructure/terraform"

@celery_app.task(name="apply_infrastructure")
def task_apply_infrastructure():
    """
    Terraform init ve apply komutlarını çalıştırır.
    """
    print("--- TERRAFORM: Altyapı Kurulumu Başlıyor ---")
    
    tf = Terraform(working_dir=TF_WORKING_DIR)
    
    # 1. Init (Pluginleri indir)
    return_code, stdout, stderr = tf.init()
    if return_code != 0:
        return {"status": "error", "stage": "init", "error": stderr}
        
    print("--- TERRAFORM: Init Başarılı ---")

    # 2. Apply (Onay beklemeden kur - auto-approve)
    return_code, stdout, stderr = tf.apply(skip_plan=True)
    
    if return_code != 0:
        print(f"--- TERRAFORM HATASI: {stderr} ---")
        return {"status": "error", "stage": "apply", "error": stderr}
    
    print("--- TERRAFORM: Kurulum Tamamlandı ---")
    return {"status": "success", "output": stdout}
