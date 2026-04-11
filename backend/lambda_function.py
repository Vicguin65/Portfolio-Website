from app.main import app
from mangum import Mangum

# Mangum wraps the FastAPI ASGI app as an AWS Lambda handler.
# lifespan="off" disables startup/shutdown events (not needed on Lambda).
handler = Mangum(app, lifespan="off")
