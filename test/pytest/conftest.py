
import pytest

from jjpine.tool.filter import Filter as JJFilter


@pytest.yield_fixture(scope="function")
def jjfilter_fixture():
    yield JJFilter()
