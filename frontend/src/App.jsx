import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [logs, setLogs] = useState([])
  const [loading, setLoading] = useState(false)

  // Log ekleme yardımcı fonksiyonu
  const addLog = (msg) => {
    const time = new Date().toLocaleTimeString()
    setLogs(prev => [`[${time}] ${msg}`, ...prev])
  }

  // 1. Terraform Tetikleyici
  const handleInfrastructure = async () => {
    setLoading(true)
    addLog("🚀 Terraform: Altyapı kurulumu isteği gönderiliyor...")
    try {
      const res = await axios.post('http://localhost:8000/infrastructure/apply')
      addLog(`✅ Başarılı! Task ID: ${res.data.task_id}`)
      addLog("ℹ️ İşlem arka planda devam ediyor (Worker loglarını kontrol et).")
    } catch (error) {
      addLog(`❌ Hata: ${error.message}`)
    }
    setLoading(false)
  }

  // 2. Ansible Tetikleyici
  const handleConfiguration = async () => {
    setLoading(true)
    addLog("🔧 Ansible: Konfigürasyon isteği gönderiliyor...")
    try {
      const res = await axios.post('http://localhost:8000/configuration/apply')
      addLog(`✅ Başarılı! Task ID: ${res.data.task_id}`)
      addLog("ℹ️ Sunucu ayarları güncelleniyor...")
    } catch (error) {
      addLog(`❌ Hata: ${error.message}`)
    }
    setLoading(false)
  }

  return (
    <div className="container">
      <header className="header">
        <h1>🛡️ BlueUnix Kontrol Merkezi</h1>
        <p>Siber Güvenlik Otomasyon Fabrikası</p>
      </header>

      <div className="control-panel">
        <div className="card">
          <h2>1. Altyapı (Provisioning)</h2>
          <p>Terraform kullanarak sunucuları ve ağları oluştur.</p>
          <button onClick={handleInfrastructure} disabled={loading} className="btn btn-blue">
            🏗️ Altyapıyı Kur / Onar
          </button>
        </div>

        <div className="card">
          <h2>2. Konfigürasyon (IaC)</h2>
          <p>Ansible ile sunuculara yazılım ve güvenlik ayarı bas.</p>
          <button onClick={handleConfiguration} disabled={loading} className="btn btn-green">
            ⚙️ Ayarları Uygula
          </button>
        </div>
      </div>

      <div className="log-terminal">
        <h3>📡 İşlem Logları</h3>
        <div className="logs">
          {logs.length === 0 ? <p>Henüz bir işlem yapılmadı...</p> : logs.map((log, i) => (
            <div key={i} className="log-line">{log}</div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
