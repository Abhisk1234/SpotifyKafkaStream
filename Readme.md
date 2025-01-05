# 🎵 Spotify Data Processing Application

A Python-based application that integrates with the Spotify API to process and analyze music data in real-time.

---

## 🚀 Features
- Fetch music data using Spotify API.
- Real-time processing with Apache Kafka and Spark Streaming.
- Apply filters and transformations on data.
- Save and export processed data in desired formats.

---

## 🔑 Key Terminology
1. **Kafka Producer**: Streams raw music data to the Kafka topic.
2. **Kafka Consumer**: Subscribes to the topic and processes data in real-time.
3. **Spark Streaming**: Processes the data with transformations and analytics.
4. **Spotify API**: Fetches music metadata (e.g., song names, artists, albums).

---

## 🛠 How It Works
1. **Data Flow**: 
   - Producer streams music metadata into Kafka topics.
   - Consumer pulls this data and processes it using Spark.
   - Processed data is stored or analyzed.

2. **Integration**:
   - Uses the Spotify API to fetch music data.
   - Kafka enables efficient real-time data streaming.
   - Spark ensures scalable processing of high-throughput data.

---

## 🛑 Prerequisites
- Python 3.8+
- Apache Kafka
- Apache Spark
- Spotify Developer Account (API credentials)

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/Abhisk1234/SpotifyKafkaStream.git
cd SpotifyKafkaStream
```

## 🔑 Environment Variables

### Create a .env file in the root directory with the following keys:

### Clone the repository
```bash
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_SECRET_KEY=your_secret_key
KAFKA_BROKER_URL=localhost:9092
```

## 🚀 Usage
1. **Start Kafka Broker and Zookeeper**
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```
2. **Run the Producer**
```bash
python producer.py
```

3. **Run the Consumer**
```bash
python consumer.py
```

