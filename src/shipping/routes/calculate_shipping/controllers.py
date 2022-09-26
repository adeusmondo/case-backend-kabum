from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from src.containers import Container
from src.logger import Logger
from src.shipping.routes.calculate_shipping.schemas import CalculateShippingResponse, ProductPayload
from src.shipping.services.shipping_service import ShippingService

router = APIRouter()


@router.post('/v1/calculate-shipping', response_model=List[CalculateShippingResponse])
@inject
async def calculate_shipping(schema: ProductPayload, logger: Logger = Depends(Provide[Container.logger]),
                             shipping_service: ShippingService = Depends(Provide[Container.shipping_service])):
    try:
        logger.info(f'Calculating shipping for product: {schema}')
        return await shipping_service.validate_product_dimensions(schema.dict())
    except Exception as e:
        logger.error(f'Error while calculating shipping: {e}')
        raise HTTPException(status_code=500, detail=f'Internal Server Error. Erro: {e}')


def configure(app: FastAPI):
    app.include_router(router)
