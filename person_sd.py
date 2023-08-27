import person_pb2
import base64

def main():
    # Create a person
    person = person_pb2.Person()
    person.name = "Sourav Ghosh"
    person.age = 28
    person.email = "sourav.g.1995@gmail.com"

    # Serialize the person to bytes
    serialized_person = person.SerializeToString()

    # Convert the serialized bytes to base64 for display
    serialized_person_base64 = base64.b64encode(serialized_person).decode("utf-8")

    # Print the serialized encrypted message
    print("Serialized Encrypted Message (Base64):")
    print(serialized_person_base64)

    # Deserialize the bytes back to a person
    deserialized_person = person_pb2.Person()
    deserialized_person.ParseFromString(serialized_person)

    # Print the deserialized person's information
    print("\nDeserialized Person:")
    print("Name:", deserialized_person.name)
    print("Age:", deserialized_person.age)
    print("Email:", deserialized_person.email)

if __name__ == "__main__":
    main()
