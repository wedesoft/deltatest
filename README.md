# README

The project was created and run as follows on Ubuntu 20.04:

```Bash
poetry init
poetry add pyspark==3.2.2
poetry add delta-spark==2.0.0
poetry add ptpython==3.0.20
```

Then run a Python console:

```Python
poetry run ptpython
from pyspark.sql.session import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName('deltatest') \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

data = spark.range(1, 5)
data.write.format('delta').mode('overwrite').save('delta_sample')

new_data = spark.range(5,10)
new_data.write.format('delta').mode('append').save('delta_sample')

df = spark.read.format('delta').load('delta_sample')
df.show()
```

Output:

```
+---+
| id|
+---+
|  7|
|  2|
|  4|
|  1|
|  5|
|  9|
|  8|
|  6|
|  3|
+---+
```

# External links

* [Getting hands dirty in Spark Delta Lake](https://medium.com/analytics-vidhya/getting-hands-dirty-in-spark-delta-lake-1963921e4de6)
* [Delta compatibility with Apache Spark](https://docs.delta.io/latest/releases.html)
* [Delta Lake's Python documentation page](https://docs.delta.io/latest/api/python/index.html)
* [Delta Lake quick start](https://docs.delta.io/latest/quick-start.html#set-up-apache-spark-with-delta-lake)
