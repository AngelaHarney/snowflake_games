from pytest import fixture
from snowflake.snowpark import Session
from snowflake.snowpark.functions import lit
from streamlit.testing.v1 import AppTest

@fixture
def session():
    session = Session.builder.config('local_testing', True).create()
    yield session
    session.close()