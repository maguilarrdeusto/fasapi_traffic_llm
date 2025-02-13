from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import OptimizedResult
from app.schemas import OptimizationInput, OptimizationOutput
from app.services.optimization import optimize_data
from sqlalchemy.future import select

router = APIRouter()

@router.post("/optimize/", response_model=OptimizationOutput)
async def optimize(input_data: OptimizationInput, db: AsyncSession = Depends(get_db)):
    try:
        optimized_result = await optimize_data(input_data)
        
        # Guardar en la base de datos
        new_result = OptimizedResult(
            input_data=input_data.dict(),
            optimized_data=optimized_result.optimized_data
        )
        db.add(new_result)
        await db.commit()
        await db.refresh(new_result)

        return optimized_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/optimized_results/")
async def get_results(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(OptimizedResult))
    return results.scalars().all()
