# Protocol-buffer
Test for sample protocol buffer serializer - deserializer

# Steps:
    1. Install Protocol Buffers Compiler
        https://github.com/protocolbuffers/protobuf
    2. VS CODE expension protobuf
    3. Add protoc to the System PATH:
        Environment Variables : edit path and add the folder where protoc compiler exists.
        Check: protoc --version
    4. Optional: 
        Install Protocol Buffers for Python
        Restart terminal : validate version
    5. Create .proto file
    6. Compile it : generates class file 
    7. Import that in another python scrpit :
        add message
        serialize
        deserialize 
