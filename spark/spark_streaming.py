from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkStream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()


# Đọc dữ liệu từ Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9094") \
    .option("subscribe", "test-topic") \
    .load()

# Chuyển đổi dữ liệu từ Kafka thành DataFrame với kiểu dữ liệu phù hợp
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Viết dữ liệu ra console
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Chờ cho đến khi streaming query kết thúc
query.awaitTermination()
