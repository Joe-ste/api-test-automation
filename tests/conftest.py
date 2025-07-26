import pytest
import yaml
from pathlib import Path
from api.image_api import ImagesAPI
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="Environment name")

@pytest.fixture(scope="session")
def env_config(pytestconfig):
    env = pytestconfig.getoption("env").lower()
    config_path = (Path(__file__).parent.parent / "configurations" / f"{env}.yaml").resolve()
    if not config_path.exists():
        pytest.exit(f"Config file not found for env: {config_path}")
    with config_path.open() as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def images_api(env_config):
    return ImagesAPI(env_config["BASE_URL"])

@pytest.fixture(scope="session")
def data(request):
    return request.param