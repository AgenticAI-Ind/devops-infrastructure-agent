# DevOps & Infrastructure Agent

Production-grade DevOps automation agent that generates Infrastructure-as-Code, manages Kubernetes clusters, optimizes cloud costs (30-40% savings), and automates CI/CD pipelines.

## Features

- **Infrastructure-as-Code Generation**: Auto-generate Terraform, CloudFormation, Pulumi
- **Kubernetes Management**: Cluster provisioning, scaling, monitoring
- **Cloud Cost Optimization**: Identify and eliminate waste (30-40% savings)
- **CI/CD Automation**: Pipeline generation for GitHub Actions, GitLab CI, Jenkins
- **Multi-Cloud Support**: AWS, GCP, Azure, DigitalOcean
- **Security Compliance**: CIS benchmarks, security scanning
- **Monitoring & Alerting**: Prometheus, Grafana dashboards

## Tech Stack

- **FastAPI** - REST API framework
- **Terraform** - Infrastructure provisioning
- **Kubernetes** - Container orchestration
- **AWS/GCP/Azure SDKs** - Cloud provider APIs
- **Prometheus** - Monitoring
- **Docker** - Containerization

## Architecture

```
┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  User/CLI    │────▶│  FastAPI    │────▶│  Terraform   │
│              │     │  Endpoints  │     │  Generator   │
└──────────────┘     └─────────────┘     └──────────────┘
                            │                     │
                            ▼                     ▼
                     ┌─────────────┐      ┌──────────────┐
                     │ Kubernetes  │      │   Cloud      │
                     │  Manager    │      │  Providers   │
                     └─────────────┘      └──────────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │    Cost     │
                     │  Optimizer  │
                     └─────────────┘
```

## Quick Start

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Terraform 1.5+
- kubectl 1.27+
- Cloud provider credentials (AWS/GCP/Azure)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AgenticAI-Ind/devops-infrastructure-agent.git
cd devops-infrastructure-agent
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your cloud credentials
```

5. Run the application:
```bash
python src/main.py
```

6. Access the API:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## API Endpoints

### Infrastructure-as-Code
- `POST /iac/generate` - Generate Terraform/CloudFormation code
- `POST /iac/validate` - Validate IaC templates
- `POST /iac/apply` - Apply infrastructure changes
- `GET /iac/state` - Get infrastructure state

### Kubernetes Management
- `POST /k8s/cluster/create` - Create K8s cluster
- `POST /k8s/deploy` - Deploy application
- `GET /k8s/cluster/status` - Get cluster status
- `POST /k8s/scale` - Scale deployments

### Cost Optimization
- `GET /cost/analyze` - Analyze cloud costs
- `POST /cost/optimize` - Get optimization recommendations
- `GET /cost/report` - Generate cost report

### CI/CD Pipelines
- `POST /cicd/generate` - Generate pipeline configuration
- `GET /cicd/status` - Get pipeline status

## Usage Examples

### Generate Terraform Code

```python
import requests

response = requests.post(
    "http://localhost:8000/iac/generate",
    json={
        "provider": "aws",
        "resources": [
            {
                "type": "ec2_instance",
                "name": "web-server",
                "instance_type": "t3.medium"
            }
        ]
    }
)

print(response.json()["terraform_code"])
```

### Create Kubernetes Cluster

```python
response = requests.post(
    "http://localhost:8000/k8s/cluster/create",
    json={
        "name": "production-cluster",
        "provider": "gcp",
        "node_count": 3,
        "node_type": "n1-standard-4"
    }
)
```

## Project Structure

```
devops-infrastructure-agent/
├── src/
│   ├── main.py                      # FastAPI application
│   ├── config.py                    # Configuration
│   ├── models/
│   │   └── schemas.py               # Pydantic models
│   ├── services/
│   │   ├── k8s_manager.py           # Kubernetes operations
│   │   ├── cost_optimizer.py        # Cost optimization
│   │   └── cicd_automation.py       # CI/CD pipeline gen
│   ├── generators/
│   │   └── terraform_generator.py   # Terraform code gen
│   └── utils/
│       └── cloud_clients.py         # Cloud SDK clients
├── templates/                       # IaC templates
├── tests/
├── docker-compose.yml
└── requirements.txt
```

## Cost Optimization

### Optimization Strategies
1. **Right-sizing**: Downsize over-provisioned resources (15-25% savings)
2. **Reserved Instances**: Recommend RI purchases (30-40% savings)
3. **Spot Instances**: Identify spot-eligible workloads (70-90% savings)
4. **Storage Optimization**: Delete unused volumes (10-20% savings)

**Total potential: 30-40% cost reduction**

## License

MIT License - see LICENSE file

## Support

- Documentation: https://useagenticai.in/agents/devops-infrastructure-agent.html
- Issues: https://github.com/AgenticAI-Ind/devops-infrastructure-agent/issues
- Email: info@useagenticai.in
