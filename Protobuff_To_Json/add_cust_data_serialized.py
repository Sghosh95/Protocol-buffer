import customer_pb2 as helper
#import numpy as np

#add product data

product=helper.Product()
product.id="10"
product.name="laptop"
product.price=35000

#add Customer details
customer=helper.Customer()
customer.cust_id="123"
customer.name="Sourav Ghosh"
customer.email="Sourav.gmail.com"

#add oderItem
orderItem=helper.OrderItem()
orderItem.product_id="45436"
orderItem.quantity=234

 #adding Order
order=helper.Order()
order.id="235"
#copying from customer
order.customer.CopyFrom(customer)
order.items.extend([orderItem])

#SERIALIZE THE DATA

product_serialized=product.SerializeToString()
order_serialized=order.SerializeToString()
customer_serialized=customer.SerializeToString()

if __name__=="__main__":
    print("Product data:")
    print(product)
    print("=====================")
    print("product_serialized")
    print("=======>",product_serialized)
    print("===================================")
    print("Customer data:")
    print(customer)
    print("=====================")
    print("customer_serialized")
    print("======>",customer_serialized)

    print("===================================")
    print("Order data:")
    print(order)
    print("=====================")
    print("order_serialized")
    print("======>",order_serialized)