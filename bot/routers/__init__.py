from aiogram import Router

from .test import router as test_router
from .handlers import router_handler

router = Router()
router.include_router(test_router)

router.include_router(router_handler)