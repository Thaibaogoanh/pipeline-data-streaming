import pandas as pd
import json
from kafka import KafkaProducer
import time

# Cấu hình Kafka producer (lưu ý: sử dụng địa chỉ container 'kafka' thay vì 'localhost')
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    request_timeout_ms=120000
)

# Đọc file CSV (đảm bảo file AIR2301.csv nằm trong thư mục được mount vào container)
try:
    df = pd.read_csv('..\data\AIR2301.csv')  # Đảm bảo sử dụng đúng đường dẫn
    print(f"File {df.shape[0]} rows loaded successfully.")
except Exception as e:
    print(f"Error loading CSV file: {e}")
    df = None

# Kiểm tra nếu df tồn tại, tiến hành gửi dữ liệu
if df is not None:
    topic = 'test-topic'
    for index, row in df.iterrows():
        data = row.to_dict()
        producer.send(topic, value=data)
        print(f"Sent: {data}")
        time.sleep(1)  # Giả lập gửi dữ liệu theo thời gian

    producer.flush()
else:
    print("No data to send.")
