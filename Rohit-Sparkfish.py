# Databricks notebook source
import urllib

ACCESS_KEY = "xxxxxxxxxxx"
SECRET_KEY = "xxxxxxxxxxx"
ENCODED_SECRET_KEY = urllib.quote(SECRET_KEY, "")
AWS_BUCKET_NAME = "rohit-sparkfish"
MOUNT_NAME = "sparkfish"
dbutils.fs.mount("s3n://%s:%s@%s" % (ACCESS_KEY, ENCODED_SECRET_KEY, AWS_BUCKET_NAME), "/mnt/%s" % MOUNT_NAME)
display(dbutils.fs.ls("/mnt/sparkfish"))

# COMMAND ----------

# MAGIC %python
# MAGIC from pyspark.sql import functions as F
# MAGIC from pyspark.sql.functions import datediff, to_date, lit, unix_timestamp,split
# MAGIC from pyspark.sql.types import *
# MAGIC 
# MAGIC # Build DataFrame dataset to work with. 
# MAGIC formatPackage = "csv" if sc.version > '1.6' else "com.databricks.spark.csv"
# MAGIC df = sqlContext.read.format(formatPackage).options(header='true', delimiter = ',').load("dbfs:/mnt/sparkfish/titanic.csv")
# MAGIC data_df=df.withColumn("Age", df["Age"].cast(IntegerType()))
# MAGIC data_df.printSchema()
# MAGIC data_df.write.saveAsTable('sparkfishTable', format='parquet', mode='overwrite',path='dbfs:/mnt/sparkfish/sparkfishTable/')

# COMMAND ----------

from pyspark import SparkContext, HiveContext
hiveContext = HiveContext(sc)
display(hiveContext.sql("SELECT percentile(Age, 0.75) FROM sparkfishTable"))


# COMMAND ----------

from pyspark import SparkContext, HiveContext
hiveContext = HiveContext(sc)
display(hiveContext.sql("SELECT avg(Age) FROM sparkfishTable"))
