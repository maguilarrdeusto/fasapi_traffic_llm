import time
import httpx
from app.config import settings

async def optimize_kpis(weights: dict) -> dict:
    """
    Lógica para optimizar los KPI en función del modo seleccionado.
    """
    if settings.OPTIMIZATION_MODE == "test":
        return await optimize_kpis_test(weights)
    else:
        return await optimize_kpis_real(weights)

async def optimize_kpis_test(weights: dict) -> dict:
    """
    Simulación de la optimización de KPI con normalización.
    """
    time.sleep(1)  # Simula un retraso en la optimización

    # Generamos valores arbitrarios para la simulación
    optimized_kpis = {
        "optimized_PublicTransport": weights["weight_PublicTransport"] * 1.1,
        "optimized_Congestion": weights["weight_Congestion"] * 0.9,
        "optimized_Emissions": weights["weight_Emissions"] * 0.8,
        "optimized_OperationalCost": weights["weight_OperationalCost"] * 1.2,
    }

    # Normalizar los KPI para que la suma sea 1.0
    total = sum(optimized_kpis.values())
    if total > 0:
        optimized_kpis = {key: value / total for key, value in optimized_kpis.items()}

    return optimized_kpis

async def optimize_kpis_real(weights: dict) -> dict:
    """
    Llama al servicio de optimización real mediante una solicitud HTTP.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(settings.OPTIMIZATION_SERVICE_URL, json={"weights": weights})
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return {"error": f"Error en la consulta al servicio de optimización: {e}"}


