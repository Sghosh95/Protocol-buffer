import customer_pb2 as helper
import json
from google.protobuf.json_format import MessageToJson
from add_data import order_serialized,customer_serialized,product_serialized


deserialized_order=helper.Order()
deserialized_order.ParseFromString(order_serialized)
order_json=MessageToJson(deserialized_order)
print(order_json)

deserialized_customer=helper.Customer()
deserialized_customer.ParseFromString(customer_serialized)
customer_json=MessageToJson(deserialized_customer)
print("===============")
print(customer_json)