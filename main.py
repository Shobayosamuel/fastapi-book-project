import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your API router
app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

# if __name__ == "__main__":
#     import uvicorn
#     # Get port from environment variable or default to 8000
#     port = int(os.getenv("PORT", 8000))
#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=port,
#         reload=False,  # Disable reload in production
#         workers=4  # Number of worker processes
#     )