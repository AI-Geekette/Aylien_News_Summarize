import sys
import os
thisDir = os.getcwd()
sys.path.append(thisDir)

from pathlib import Path
path = Path(thisDir)
sys.path.append(str(path.parent.absolute()))

from fastapi import APIRouter
from controllers import stories_controllers

custom_search_router = APIRouter(prefix = "/custom")

stories_controller = stories_controllers.aylien_services()
custom_search_router.add_api_route("/{keywords}", stories_controller.post_custom_keywords, methods = ["POST"])