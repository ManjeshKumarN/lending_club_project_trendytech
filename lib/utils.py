from pyspark.sql import SparkSession
from lib.configreader import get_pyspark_config 

# def get_spark_session(env):
#     if env == "LOCAL":
#         return SparkSession.builder \
#         .config(conf=get_pyspark_config(env)) \    # for spark configurations without logging 
#         .master("local[2]") \
#         .getOrCreate()
#     else:
#         return SparkSession.builder \
#         .config(conf=get_pyspark_config(env)) \
#         .enableHiveSupport() \
#         .getOrCreate()

def get_spark_session(env):
    if env == "LOCAL":
        return SparkSession.builder \
            .config(conf=get_pyspark_config(env)) \
            .config('spark.driver.extraJavaOptions', # providing the specifications of logging 
                    '-Dlog4j.configuration=file:log4j.properties') \
            .master("local[2]") \
            .getOrCreate()
    else:
        return SparkSession.builder \
            .config(conf=get_pyspark_config(env)) \
            .enableHiveSupport() \
            .getOrCreate()