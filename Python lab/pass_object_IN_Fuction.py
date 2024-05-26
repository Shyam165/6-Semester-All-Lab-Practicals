class Customer:

    def __init__(self, name):
        self.name = name


def greet(customer):
    print(id(customer))
    customer.name = "nitish"
    print(customer.name)
    print(id(customer))

cust = Customer("ankita")
print(id(cust))

greet(cust)
print(cust.name)



'''class ke objects are also mutable like lists, dicts and sets
pass by reference me agr hum mutable data types ko send karenge toh original vale change ho jayenge
and pass by reference me immutable data types like tuples ko send karenge toh original data me change nhi hoga'''
