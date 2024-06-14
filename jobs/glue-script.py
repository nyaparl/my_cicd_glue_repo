import allimports
import sessionCreation

spark = createSession()

input_path = "s3://mycicdglue-bucket/input/emp.txt"
output_path = "s3://mycicdglue-bucket/output/emp.json"

df = spark.read.format("csv").load(input_path)

df.coalesce(1).write.mode("overwrite").format("json").save(output_path)
