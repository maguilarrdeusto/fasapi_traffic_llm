from pydantic import BaseModel
from typing import Dict, Any

class OptimizationInput(BaseModel):
    data: Dict[str, float]  # Los valores a optimizar (weights)

class OptimizationOutput(BaseModel):
    optimized_data: Dict[str, float]  # KPI optimizados
