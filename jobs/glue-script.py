from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark =  SparkSession.builder.appName("cicd").master("local[*]").getOrCreate()

input_path = "s3://mybuck-yap01/input/emp.csv"
output_path = "s3://mybuck-yap01/output/emp.json"

df = spark.read.format("csv").load(input_path)

df.coalesce(1).write.mode("overwrite").format("json").save(output_path)

output_path = "s3://mybuck-yap01/output/dept"

df1 = df.groupBy(col("DEPARTMENT_ID")).count().alias("no_of_emps")

df1.coalesce(1).write.mode("overwrite").format("csv").save(output_path)
