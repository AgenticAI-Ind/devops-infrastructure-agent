"""Pydantic models for API"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class IaCGenerateRequest(BaseModel):
    """Request to generate Infrastructure-as-Code"""
    provider: str = Field(..., description="Cloud provider: aws, gcp, azure")
    resources: List[Dict[str, Any]]
    output_format: str = Field(default="terraform", description="terraform, cloudformation, pulumi")


class IaCGenerateResponse(BaseModel):
    """Response with generated IaC code"""
    provider: str
    code: str
    resources_count: int
    estimated_cost: Optional[float] = None


class K8sClusterCreateRequest(BaseModel):
    """Request to create Kubernetes cluster"""
    name: str
    provider: str = Field(..., description="gcp, aws, azure")
    region: str
    node_count: int = Field(default=3, ge=1, le=100)
    node_type: str
    version: str = Field(default="1.27")


class K8sClusterResponse(BaseModel):
    """Response for K8s cluster operation"""
    cluster_id: str
    name: str
    status: str
    endpoint: Optional[str] = None
    created_at: datetime


class K8sDeployRequest(BaseModel):
    """Request to deploy application to K8s"""
    cluster_id: str
    image: str
    replicas: int = Field(default=3, ge=1, le=100)
    port: int
    environment: Dict[str, str] = {}


class CostAnalysisRequest(BaseModel):
    """Request for cost analysis"""
    provider: str
    account_id: str
    time_range: str = Field(default="30d", description="7d, 30d, 90d")
    resource_types: Optional[List[str]] = None


class CostRecommendation(BaseModel):
    """Cost optimization recommendation"""
    resource_id: str
    resource_type: str
    recommendation: str
    current_cost: float
    optimized_cost: float
    savings: float
    confidence: float


class CostOptimizationResponse(BaseModel):
    """Response with cost optimization recommendations"""
    total_current_cost: float
    total_optimized_cost: float
    total_savings: float
    recommendations: List[CostRecommendation]


class CICDGenerateRequest(BaseModel):
    """Request to generate CI/CD pipeline"""
    platform: str = Field(..., description="github-actions, gitlab-ci, jenkins")
    repository: str
    language: str
    build_steps: List[str] = []
    deploy_target: Optional[str] = None


class PipelineResponse(BaseModel):
    """Response with pipeline configuration"""
    platform: str
    config: str
    stages: List[str]
