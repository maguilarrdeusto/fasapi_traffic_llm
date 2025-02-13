import httpx
from app.config import settings
from app.schemas import OptimizationInput, OptimizationOutput

async def optimize_data(input_data: OptimizationInput) -> OptimizationOutput:
    async with httpx.AsyncClient() as client:
        response = await client.post(settings.OPTIMIZATION_SERVICE_URL, json=input_data.dict())
        if response.status_code == 200:
            return OptimizationOutput(optimized_data=response.json())
        else:
            raise Exception("Error en la optimización: " + response.text)

