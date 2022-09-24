import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI()

    from shipping.routes.health import controllers as health_module
    health_module.configure(app)

    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])

    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
