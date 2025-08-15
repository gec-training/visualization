from pyspark.sql import SparkSession
from pyspark.sql.types import *
import matplotlib.pyplot as plt
import pandas

spark = SparkSession.builder.appName("matPlotLib1").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("Error")

schema = StructType([
    StructField("Product",StringType(),False),
    StructField("Quantity",IntegerType(),True),
    StructField("Sales",IntegerType(),False)
])

df = spark.read.csv("../dataset/sales.csv", header=True, sep=",",schema=schema)
df.show()

## First mat plot.[Line chat]
dfMatPlot = df.groupBy("Product").sum("Sales")
dfMatPlot.show()
x = dfMatPlot.toPandas()["Product"].values.tolist()
y = dfMatPlot.toPandas()["sum(Sales)"].values.tolist()
plt.plot(x, y)
plt.show()

plt.bar(x,y)
plt.show()