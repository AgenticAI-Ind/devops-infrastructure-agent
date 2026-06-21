"""Configuration management"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""

    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False

    # AWS Credentials
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_DEFAULT_REGION: str = "us-east-1"

    # GCP Credentials
    GCP_PROJECT_ID: Optional[str] = None
    GCP_SERVICE_ACCOUNT_KEY: Optional[str] = None

    # Azure Credentials
    AZURE_SUBSCRIPTION_ID: Optional[str] = None
    AZURE_TENANT_ID: Optional[str] = None
    AZURE_CLIENT_ID: Optional[str] = None
    AZURE_CLIENT_SECRET: Optional[str] = None

    # Kubernetes
    KUBECONFIG: Optional[str] = None

    # Terraform
    TERRAFORM_VERSION: str = "1.5.0"
    TF_STATE_BACKEND: str = "s3"
    TF_STATE_BUCKET: str = "my-terraform-state"
    TF_STATE_REGION: str = "us-east-1"

    # Monitoring
    PROMETHEUS_URL: str = "http://prometheus:9090"
    GRAFANA_URL: str = "http://grafana:3000"

    # Features
    ENABLE_COST_OPTIMIZATION: bool = True
    ENABLE_AUTO_SCALING: bool = True
    COST_OPTIMIZATION_THRESHOLD: int = 100

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
