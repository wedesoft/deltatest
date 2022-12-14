# README

The project was created and run as follows on Ubuntu 20.04:

```Bash
curl -sSL https://install.python-poetry.org | python3 -
poetry init
poetry add pyspark==3.2.2
poetry add delta-spark==2.0.0
poetry add ptpython==3.0.20
```

Then run a Python console:

```Python
poetry run ptpython

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
```

Output:

```
+---+
| id|
+---+
|  1|
|  2|
|  3|
+---+
```

# External links

* [Getting hands dirty in Spark Delta Lake](https://medium.com/analytics-vidhya/getting-hands-dirty-in-spark-delta-lake-1963921e4de6)
* [Delta compatibility with Apache Spark](https://docs.delta.io/latest/releases.html)
* [Delta Lake's Python documentation page](https://docs.delta.io/latest/api/python/index.html)
* [Delta Lake quick start](https://docs.delta.io/latest/quick-start.html#set-up-apache-spark-with-delta-lake)
