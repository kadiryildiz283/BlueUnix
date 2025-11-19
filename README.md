# BlueUnix: The Cyber Security Factory

![Status](https://img.shields.io/badge/Status-Development-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Backend-FastAPI-yellow)
![IaC](https://img.shields.io/badge/IaC-Terraform%20%7C%20Ansible-purple)

**BlueUnix** is not just another installation script; it is a living, manageable, and scalable **SOC Orchestration Engine**.

It serves as a central controller to deploy, configure, and manage a complete Cyber Security stack (SIEM, SOAR, NGFW) using Infrastructure as Code (IaC) principles. BlueUnix allows security engineers to provision a "Defense-in-Depth" architecture programmatically via a unified API and Dashboard.

---

## 🏗 Architecture Overview

BlueUnix automates the deployment of a 4-Layer Open Source Security Architecture:

### Layer 1: Network Security & Perimeter Defense (NGFW)
* **Tool:** OPNsense (managed via API)
* **Role:** Gatekeeper of the network. Handles Traffic Control, VPNs, and IPS (Suricata).
* **Automation:** Dynamic Firewall rules and WireGuard configurations injected via Python.

### Layer 2: Endpoint Security
* **Tools:** Wazuh Agent + ClamAV + osquery
* **Role:** The eyes and ears on the ground.
    * **Wazuh:** Log collection, FIM, SCA, and CVE detection.
    * **osquery:** Advanced Threat Hunting (SQL-based system auditing).
    * **ClamAV:** Malware signature scanning.

### Layer 3: Central Intelligence (SIEM)
* **Tool:** Wazuh Server (Indexer & Dashboard)
* **Role:** The brain. Correlates logs from OPNsense, endpoints, and applications to generate meaningful alerts.

### Layer 4: Automation & Response (SOAR)
* **Tools:** TheHive Project & Cortex
* **Role:** The muscle. Automatically creates cases from Wazuh alerts and executes playbooks (e.g., blocking an IP on OPNsense via API).

---

## 🔧 Technical Stack

BlueUnix uses a modern Controller/Worker architecture to manage the infrastructure:

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Controller** | Python (FastAPI) | Core logic, API, and orchestration trigger. |
| **Task Queue** | Celery + Redis | Handling long-running provisioning tasks asynchronously. |
| **Provisioning** | Terraform | State management and resource creation (VMs, Networks). |
| **Config Mgmt** | Ansible | Dynamic inventory management and service configuration. |
| **Frontend** | React/Vue | Management Dashboard for the SOC Factory. |

---

## 📂 Project Structure

```bash
BlueUnix/
├── backend/                # Python Controller (FastAPI)
│   ├── app/services/       # Wrappers for Terraform, Ansible, and OPNsense APIs
│   └── workers/            # Celery tasks for async deployment
├── frontend/               # Web UI for managing the SOC
├── infrastructure/         # The "Factory" Blueprints
│   ├── terraform/          # Infrastructure provisioning modules
│   └── ansible/            # Playbooks for configuring Wazuh, TheHive, etc.
└── docker-compose.yml      # Orchestrates the Controller stack
---

## 🚀 Getting Started

Follow these instructions to get a local copy of the project up and running for development and testing purposes.

### Prerequisites

To run the **BlueUnix Controller**, you need:
* **Docker & Docker Compose:** To containerize the backend and frontend services.
* **Python 3.11+:** If running outside Docker.
* **Terraform & Ansible:** Must be installed on the host machine (or the worker container) to execute infrastructure tasks.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/kadiryildildiz283/BlueUnix.git](https://github.com/kadiryildildiz283/BlueUnix.git)
    cd BlueUnix
    ```

2.  **Environment Configuration**
    Create a `.env` file in the root directory based on the example:
    ```bash
    cp .env.example .env
    # Edit .env to add your OPNsense API keys, Cloud Provider credentials, etc.
    ```

3.  **Build and Run the Controller Stack**
    This command spins up the FastAPI Backend, React Frontend, Redis, and Celery Workers.
    ```bash
    docker-compose up -d --build
    ```

4.  **Access the Interfaces**
    * **Management Dashboard:** `http://localhost:3000`
    * **API Documentation (Swagger UI):** `http://localhost:8000/docs`
    * **Celery Flower (Task Monitor):** `http://localhost:5555`

---

## 🕹️ Usage Workflow

Here is how **BlueUnix** orchestrates a deployment:

1.  **Define Intent:** The user logs into the Dashboard and selects a template (e.g., *"Standard SOC Lab"*).
2.  **Provisioning (Terraform):** The backend triggers a Celery task that executes `terraform apply`.
    * *Result:* VMs are created, OPNsense interfaces are configured, Network is established.
3.  **Inventory Update:** BlueUnix parses the Terraform state file (`terraform.tfstate`) to build a dynamic Ansible inventory.
4.  **Configuration (Ansible):** The backend triggers Ansible playbooks against the new inventory.
    * *Result:* Wazuh Agent is installed on endpoints, OPNsense firewall rules are injected via API, TheHive is configured.
5.  **Ready:** The Dashboard updates the status to "Active," and the SOC is ready for use.

---

## 🔮 Roadmap

We are actively working on making BlueUnix the standard for Open Source SOC deployment.

* **Phase 1: Foundation (Current)**
    * [x] Core Project Structure & Dockerization.
    * [ ] Basic OPNsense API Wrapper.
    * [ ] Terraform modules for local Docker/Proxmox provisioning.
* **Phase 2: Intelligence Integration**
    * [ ] Wazuh Manager automated setup role.
    * [ ] TheHive + Cortex middleware implementation (`thehive4py`).
* **Phase 3: Advanced Automation**
    * [ ] Windows GPO automation via Ansible for Active Directory environments.
    * [ ] ModSecurity (WAF) auto-deployment module.
* **Phase 4: Threat Intel**
    * [ ] MISP (Malware Information Sharing Platform) integration.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please refer to `CONTRIBUTING.md` for detailed code of conduct and development guidelines.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact & Support

**Project Maintainer:** Kadir Yildiz  
**GitHub:** [@kadiryildildiz283](https://github.com/kadiryildildiz283)

<p align="center">
  <i>Built with ❤️ for Cyber Security Researchers and Engineers.</i>
</p>

