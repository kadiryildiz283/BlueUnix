import requests
import json
from celery import shared_task
from app.workers.celery_app import celery_app

class OpnsenseClient:
    def __init__(self, url, api_key, api_secret, verify_ssl=False):
        self.url = url.rstrip('/')
        self.auth = (api_key, api_secret)
        self.verify_ssl = verify_ssl
        self.headers = {'Content-Type': 'application/json'}

    def check_connection(self):
        """OPNsense'e basit bir ping atar (Mock durumunda her zaman True döner)"""
        # Gerçek bağlantı için: 
        # response = requests.get(f"{self.url}/api/core/firmware/status", auth=self.auth, verify=self.verify_ssl)
        # return response.status_code == 200
        return True

    def add_firewall_alias(self, name, ip_list):
        """Firewall'a yeni bir IP listesi (Alias) ekler"""
        endpoint = f"/api/firewall/alias/addItem"
        payload = {
            "alias": {
                "name": name,
                "type": "host",
                "content": "\n".join(ip_list),
                "description": "BlueUnix tarafindan olusturuldu"
            }
        }
        # Mocking the request for now
        print(f"[OPNsense] Alias ekleniyor: {name} -> {ip_list}")
        # requests.post(f"{self.url}{endpoint}", json=payload, auth=self.auth...)
        return {"status": "success", "uuid": "mock-uuid-1234"}

# --- Celery Görevleri (Asenkron İşler) ---

@celery_app.task(name="create_network_alias")
def task_create_alias(name: str, ips: list):
    """
    Bu fonksiyon arka planda çalışır. API'yi bekletmez.
    """
    # Konfigürasyonu ilerde veritabanından veya env'den çekeceğiz
    client = OpnsenseClient(
        url="https://192.168.1.1", 
        api_key="mock_key", 
        api_secret="mock_secret"
    )
    
    print(f"--- GÖREV BAŞLADI: Alias Oluşturuluyor ({name}) ---")
    result = client.add_firewall_alias(name, ips)
    print(f"--- GÖREV TAMAMLANDI: {result} ---")
    return result
