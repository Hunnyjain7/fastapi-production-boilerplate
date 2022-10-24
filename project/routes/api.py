from fastapi import APIRouter
from project.endpoints.admin_app import authentication
from project.endpoints.client_app import client_authentication

router = APIRouter()

# --------------------Admin Routing---------------------
router.include_router(authentication.router)

# --------------------Client Routing--------------------
router.include_router(client_authentication.router)
