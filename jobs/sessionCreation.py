from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def createSession():
  return SparkSession.builder.appName('cicd') \
         .master('local[*]').getOrCreate()
