from pyspark.sql.session import SparkSession
from delta import configure_spark_with_delta_pip, DeltaTable


builder = SparkSession.builder.appName('deltatest') \
    .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension') \
    .config('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog') \
    .config('spark.databricks.delta.legacy.allowAmbiguousPathsInCreateTable', True) \
    .config('spark.driver.host', 'localhost')
spark = configure_spark_with_delta_pip(builder).getOrCreate()

DeltaTable.createIfNotExists(spark) \
    .addColumn("id", "LONG").location("/tmp/deltatest").execute()

df = spark.createDataFrame([(1,), (2,), (3,)], ["id"])
df.write.format("delta").mode("append").save("/tmp/deltatest")

spark.read.format("delta").load("/tmp/deltatest").show()
