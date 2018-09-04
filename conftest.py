import pytest

def pytest_addoption(parser):
 parser.addoption(
                 "--cmdopt", action="store", default="dev", help="my option: dev or prod"
                )

@pytest.fixture
def cmdopt(request):
	return request.config.getoption("--cmdopt")
