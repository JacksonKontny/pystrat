from io import BytesIO

from pytest import fixture


@fixture
def upload_request_context(flask_app):
    with flask_app.test_request_context(
        "/upload",
        method="POST",
        data={"file": (BytesIO(b"my file contents"), "file_name")},
    ) as context:
        yield context
