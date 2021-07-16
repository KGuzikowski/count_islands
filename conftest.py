from io import StringIO

import pytest


@pytest.fixture()
def file():
    def _foo(content):
        return StringIO(content)

    return _foo
