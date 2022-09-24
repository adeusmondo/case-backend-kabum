from typing import List

from containers import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from logger import Logger
from shipping.routes.shipping_options.schemas import ShippingOptionResponse
from shipping.services.shipping_service import ShippingService

router = APIRouter()


@router.get('/v1/shipping-options', response_model=List[ShippingOptionResponse])
@inject
async def shipping_options(shipping_service: ShippingService = Depends(Provide[Container.shipping_service]),
                           logger: Logger = Depends(Provide[Container.logger]),):
    try:
        return await shipping_service.get_shipping_options()
    except Exception as e:
        logger.error(f'Error while calculating shipping: {e}')
        raise HTTPException(status_code=500, detail=f'Internal Server Error. Erro: {e}')


def configure(app: FastAPI):
    app.include_router(router)
