import pytest
from lib.utils import get_spark_session
from from_root import from_root

# conftest.py is used to create fixtures 

@pytest.fixture
# def spark_s():
#     spark_session_= get_spark_session("LOCAL") 
#     return spark_session_

def spark_s(): 
    """create spark session"""
    spark_session_= get_spark_session("LOCAL") 
    yield spark_session_ # till here the script is ran , teardown yield 
    spark_session_.stop() # after the test case thsi will run 

file_path=from_root("data","test_results","state_aggregate.csv")

@pytest.fixture
def expected_results(spark_s):
    """gives the expected results after reading from csv """ # fixture gives the expected results after reading from files 
    results_schema_="state str , count int"
    return spark_s.read.csv(file_path,schema=results_schema_) 

