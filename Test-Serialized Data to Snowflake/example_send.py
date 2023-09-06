from kafka import KafkaProducer
from example_pb2 import MyMessage  # Import the generated Python message class

# Create a KafkaProducer instance with Kafka broker configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Create an instance of MyMessage
message = MyMessage()

for i in range(1000):
# Populate the message
    message.message_text = "test"
    message.message_number = i*3

# Serialize the message to binary format
    serialized_message = message.SerializeToString()

# Send the serialized message to a Kafka topic
    topic = "data_test"  # Replace with the name of your Kafka topic
    producer.send(topic, value=serialized_message)

# Close the producer when done
producer.close()