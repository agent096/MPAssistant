from .default import router as default_router
from .buttons import router as buttons_router

routers = [default_router, buttons_router]


__all__ = ["routers"]