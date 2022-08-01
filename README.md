# README

The project was created and run as follows on Ubuntu 20.04:

```Bash
poetry init
poetry add pyspark==3.2.2
poetry add delta-spark==2.0.0
poetry add ptpython==3.0.20
poetry run pyspark --packages io.delta:delta-core_2.12:2.0.0
```

Then try this on the Spark console:

```Spark
data = spark.range(1,5)
data.write.format("delta").mode("overwrite").save("delta_sample")
new_data = spark.range(5,10)
new_data.write.format("delta").mode("append").save("delta_sample")
```

Exit and then run a Python console:

```Python
export SPARK_HOME=$PWD/.venv/lib/python3.8/site-packages/pyspark
poetry run ptpython
from pyspark.sql.session import SparkSession
from delta.tables import DeltaTable
spark = SparkSession.builder.appName('delta test').getOrCreate()
deltatable = DeltaTable.forPath(spark, 'delta_sample')
```

Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/project-area/jw4/deltatest/.venv/lib/python3.8/site-packages/delta/tables.py", line 352, in forPath
    jdt = jvm.io.delta.tables.DeltaTable.forPath(jsparkSession, path)
TypeError: 'JavaPackage' object is not callable

'JavaPackage' object is not callable
```

# External links

* [Getting hands dirty in Spark Delta Lake](https://medium.com/analytics-vidhya/getting-hands-dirty-in-spark-delta-lake-1963921e4de6)
* [Delta compatibility with Apache Spark](https://docs.delta.io/latest/releases.html)
* [Delta Lake's Python documentation page](https://docs.delta.io/latest/api/python/index.html)
* [Delta Lake quick start](https://docs.delta.io/latest/quick-start.html#set-up-apache-spark-with-delta-lake)
