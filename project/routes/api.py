from fastapi import APIRouter
from project.endpoints.admin_app import authentication

router = APIRouter()
router.include_router(authentication.router)
