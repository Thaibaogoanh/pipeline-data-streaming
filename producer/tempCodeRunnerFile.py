import pandas as pd
import json
from kafka import KafkaProducer
import time

# Cấu hình Kafka producer (lưu ý: sử dụng địa chỉ container 'kafka' thay vì 'localhost')
producer = KafkaProducer(
    bootstrap_servers='broker:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    request_timeout_ms=120000
)

# Đọc file CSV (đảm bảo file AIR2301.csv nằm trong thư mục được mount vào container)
df = pd.read_csv('/app/data/AIR2301.csv')  # Sử dụng pd.read_csv() thay vì pd.read_excel()

# Gửi từng dòng dữ liệu vào Kafka topic (ví dụ: 'test-topic')
topic = 'test-topic'
for index, row in df.iterrows():
    data = row.to_dict()
    producer.send(topic, value=data)
    print(f"Sent: {data}")
    time.sleep(1)  # Giả lập gửi dữ liệu theo thời gian

producer.flush()