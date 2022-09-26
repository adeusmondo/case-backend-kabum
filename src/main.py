import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.containers import Container


def create_app():
    app = FastAPI()

    container = Container()

    from src.shipping.routes.health import controllers as health_module
    health_module.configure(app)

    from src.shipping.routes.calculate_shipping import controllers as calculate_shipping_module
    calculate_shipping_module.configure(app)

    from src.shipping.routes.shipping_options import controllers as shipping_options_module
    shipping_options_module.configure(app)

    container.wire(modules=[health_module, calculate_shipping_module, shipping_options_module])

    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])

    app.container = container

    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)
