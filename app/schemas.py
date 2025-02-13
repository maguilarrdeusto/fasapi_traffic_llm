from pydantic import BaseModel
from typing import Dict, Any

class OptimizationInput(BaseModel):
    data: Dict[str, Any]  # JSON de entrada con valores a optimizar

class OptimizationOutput(BaseModel):
    optimized_data: Dict[str, Any]  # JSON de salida con valores optimizados
