from importlib.metadata import version

from fastapi import FastAPI

from elochess.api.update import update_router

app = FastAPI(
    title="elochess",
    description="A simple API for calculating chess ratings.",
    version=version("elochess"),
)

app.include_router(update_router)
