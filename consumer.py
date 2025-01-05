from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SpotifyRealTimeProcessing") \
    .getOrCreate()

# Read data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "spotify-data") \
    .load()

# Process data (convert JSON string to structured data)
processed_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
    .selectExpr("from_json(json, 'track_name STRING, artist_name STRING, album_name STRING, played_at LONG') as data") \
    .select("data.*")

# Output to console
query = processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
