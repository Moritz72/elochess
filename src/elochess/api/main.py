import uvicorn

from elochess.api.app import app


def main() -> None:
    """Run the app instance."""
    uvicorn.run(app, host="127.0.0.1", port=8000)
