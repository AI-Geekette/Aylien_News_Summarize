import sys
import os
thisDir = os.getcwd()
sys.path.append(thisDir)

from pathlib import Path
path = Path(thisDir)
sys.path.append(str(path.parent.absolute()))

from fastapi import APIRouter
from controllers import stories_controllers

countries_router = APIRouter(prefix = "/news")

stories_controller = stories_controllers.aylien_services()

countries_router.add_api_route("/countries", stories_controller.post_all_params, methods = ["POST"])
countries_router.add_api_route("/countries/{country}", stories_controller.post_all_params_with_country, methods = ["POST"])
countries_router.add_api_route("/countries/{general_topic}", stories_controller.post_params_with_topic, methods = ["POST"])                              
countries_router.add_api_route("/countries/test", stories_controller.test_get, methods = ["GET"])