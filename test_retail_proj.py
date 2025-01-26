import pytest 
from lib.datareader import read_customers, read_orders 
from lib.datamanipulation import filter_closed_orders,count_orders_state , filter_orders_parameterised
from lib.configreader import get_app_config 

# fixtures are picked automatically from conftest.py files  
@pytest.mark.datareading# marking as datareading test cases 
def test_read_customers(spark_s): # function should start with test    
    customers_count=read_customers(spark_s,"LOCAL").count() # as one need to test the functions or logic wrote with pre caculated values 
    assert customers_count == 12435 # assert to check the true condition 

@pytest.mark.datareading 
def test_read_orders(spark_s): # function should start with test  
    orders_count=read_orders(spark_s,"LOCAL").count()
    assert orders_count == 68884 # checking on the number of records  

@pytest.mark.datamanipulation
def test_filtered_orders(spark_s): # function should start with test    
    df_=filter_closed_orders(read_orders(spark_s,"LOCAL")).count()
    assert df_ == 7556  

@pytest.mark.skip("work in progress") # skip is system defined marker 
def test_app_config():
    dict_value_returned_=get_app_config("LOCAL") 
    assert dict_value_returned_["customers.file.path"] == "data/customers.csv" # testing any one value 

@pytest.mark.datamanipulation # marking as data manipulation test cases ,name can be user defined 
def test_count_orders_state(spark_s, expected_results): # expected_results is a fixture , which gives the expected results from csv 
    df__=read_customers(spark=spark_s,env="LOCAL")
    results_=count_orders_state(df__)
    assert results_.collect() == expected_results.collect() # collect() is used to get he list 

@pytest.mark.parametric
def test_filter_closed_orders_generic(spark_s):
    df__=read_orders(spark_s,"LOCAL")
    cnt=filter_orders_parameterised(df__,"CLOSED")
    assert cnt == 7756 

@pytest.mark.parametric
def test_filter_complete_orders_generic(spark_s):
    df__=read_orders(spark_s,"LOCAL")
    cnt=filter_orders_parameterised(df__,"COMPLETE")
    assert cnt == 22900 

@pytest.mark.parametric
def test_filter_pending_orders_generic(spark_s):
    df__=read_orders(spark_s,"LOCAL")
    cnt=filter_orders_parameterised(df__,"PENDING")
    assert cnt == 7610 

@pytest.mark.parametric
def test_filter_processing_orders_generic(spark_s):
    df__=read_orders(spark_s,"LOCAL")
    cnt=filter_orders_parameterised(df__,"PROCESSING")
    assert cnt == 8275 


@pytest.mark.parametrize(  # to pass the parameters 
        "status_,count_",
        [("COMPLETE",22900),
         ("PENDING",7610),
         ("PROCESSING",8275)]
)

@pytest.mark.parametric
def test_filter_orders_generic(spark_s,status_,count_): # to test by passing the parameters using parametrize defined aboves 
    df__=read_orders(spark_s,"LOCAL")
    cnt=filter_orders_parameterised(df__,f"{status_}")
    assert cnt == count_ 