from fastapi import FastAPI

from port.adapter.resource.health import health_resource
from port.adapter.resource.item import item_resource


api = FastAPI(title="Greeedy API")
api.include_router(item_resource.router)
api.include_router(health_resource.router)
