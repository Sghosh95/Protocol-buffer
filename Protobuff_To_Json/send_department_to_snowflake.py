#import kafka producer
import customer_pb2 as helper
import revenue_pb2 as helper_2
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import KafkaError

#import dependent data tables / dict / list
from add_cust_data_serialized import product,customer,orderItem,order
from add_rev_data import departments

# Kafka broker configuration
bootstrap_servers = 'localhost:9092'

#topic name
topic="snowflake_department_topic"

#admin client to create a topic
#--> check that if the topic is created running list command
admin_client=KafkaAdminClient(bootstrap_servers=bootstrap_servers)

#topic configuration
new_topic=NewTopic(name=topic,num_partitions=1,replication_factor=1)
#error handling to create the topic
try:
    admin_client.create_topics([new_topic],validate_only=False)
    print("kafka topic named {} created".format(topic))
except KafkaError as error:
    print("Failed creating topic: {}".format(error))

#############################################################################
#PRODUCER
producer=KafkaProducer(bootstrap_servers=bootstrap_servers)
for department in departments:
    serialized_department=department.SerializeToString()
    producer.send(topic,value=serialized_department)
    print("Sent:",serialized_department)

producer.close()