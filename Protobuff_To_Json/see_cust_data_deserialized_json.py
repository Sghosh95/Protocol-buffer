import customer_pb2 as helper
from add_cust_data_serialized import product_serialized,order_serialized,customer_serialized
from google.protobuf.json_format import MessageToJson

#Customer instance
deserialized_customer=helper.Customer()
deserialized_customer.ParseFromString(customer_serialized)
print(deserialized_customer)

#Order instance
deserialized_order=helper.Order()
deserialized_order.ParseFromString(order_serialized)
print(deserialized_order)

#Product instance
deserialized_product=helper.Product()
deserialized_product.ParseFromString(product_serialized)
print(deserialized_product)

# Convert Customer to JSON
customer_json = MessageToJson(deserialized_customer, preserving_proto_field_name=True)
print("Customer JSON:")
print(customer_json)

# Convert Order to JSON
order_json = MessageToJson(deserialized_order, preserving_proto_field_name=True)
print("Order JSON:")
print(order_json)


# Convert Product to JSON
product_json = MessageToJson(deserialized_product, preserving_proto_field_name=True)
print("Product JSON:")
print(product_json)