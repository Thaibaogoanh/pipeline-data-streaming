# pipeline-data-streaming
Spark Kafka MinIO Iceberg Nessie Dremio

## 📌 Yêu cầu hệ thống
- Cài đặt [Docker](https://docs.docker.com/get-docker/)
- Cài đặt [Docker Compose](https://docs.docker.com/compose/install/) (nếu sử dụng `docker-compose.yml`)

## 🚀 Cách chạy dự án

docker compose up -d
docker cp KafkaSparkApp.py spark-master:/opt/bitnami/spark/
docker exec -it spark-master spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.13:3.3.2 KafkaSparkApp.py