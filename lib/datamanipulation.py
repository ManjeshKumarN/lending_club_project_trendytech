from pyspark.sql.functions import *

def filter_closed_orders(orders_df):
    return orders_df.filter("order_status = 'CLOSED'")

def join_orders_customers(orders_df, customers_df):
    return orders_df.join(customers_df, "customer_id")

def count_orders_state(joined_df):
    return joined_df.groupBy('state').count()

def filter_orders_parameterised(orders_df,status_): # passing the status_ parameter dynamically 
    return orders_df.filter(f"order_status = {status_}")