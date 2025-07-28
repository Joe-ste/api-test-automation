import pytest
import yaml
from pathlib import Path
from typing import Any, Dict

from api.image_api import ImagesAPI

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        help="Environment name (loads config/configurations/<env>.yaml)"
    )

@pytest.fixture(scope="session")
def env_config(pytestconfig) -> Dict[str, Any]:
    """Loads environment-specific YAML config as a dict."""
    env = pytestconfig.getoption("env").lower()
    config_path = (Path(__file__).parent.parent / "configurations" / f"{env}.yaml").resolve()
    if not config_path.exists():
        pytest.exit(f"Config file not found for env: {config_path}")
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def images_api(env_config) -> ImagesAPI:
    """Fixture for API client, constructed with config's BASE_URL."""
    return ImagesAPI(env_config["BASE_URL"])

@pytest.fixture(scope="session")
def data(request):
    """Parametrized fixture for data-driven tests."""
    return request.param