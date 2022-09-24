from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get('v1/health')
async def health():
    return {'api': 'looks like everything is ok'}


def configure(app: FastAPI):
    app.include_router(router)
