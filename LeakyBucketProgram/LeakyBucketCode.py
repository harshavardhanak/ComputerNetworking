size = int(input("Enter the size of bucket : "))
output = int(input("Enter the output rate : "))
n = int(input("Enter the number of inputs :" ))
store = 0
for i in range(n):
    incoming = int(input("Enter the incoming packet size : "))
    print("Incoming packet size is : {}".format(incoming))
    if ( incoming <= (size-store)):
        store += incoming
        print("Bucket buffer size {} out of {}".format(store, size))
    else:
        print("Dropped {} number of packets ".format(incoming - (size-store)))
        print("Bucket buffer size is {} out of {}".format(store, size))
        store = size
    store = store - output
    print("After outgoing {} packets left out of {} in buffer ".format(store,size))