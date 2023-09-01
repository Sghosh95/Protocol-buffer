import vacation_demo_pb2

# Create an Address instance
address = vacation_demo_pb2.Address()
address.street = "123 Main Street"
address.city = "Cityville"

# Create a Person instance with the nested Address
person = vacation_demo_pb2.Person()
person.name = "Alice"
person.age = 30
person.address.CopyFrom(address)

# Serialize the Person instance
serialized_data = person.SerializeToString()
print(serialized_data)

# Deserialize the serialized data
deserialized_person = vacation_demo_pb2.Person()
deserialized_person.ParseFromString(serialized_data)

# Print the deserialized person
print("Deserialized Person:")
print("Name:", deserialized_person.name)
print("Age:", deserialized_person.age)
print("Address Street:", deserialized_person.address.street)
print("Address City:", deserialized_person.address.city)
