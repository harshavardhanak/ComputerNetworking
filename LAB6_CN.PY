def CRC(l,p,r):
    c = []
    c = l.copy()
    for i in p:
        c.append("0")
    for i in range(len(l)):
        if (int(c[i]) == 1):
            for j in range(len(p)):
                if ( int(c[i+j]) == int(p[j])):
                    c[i+j] = '0'
                else:
                    c[i+j] = '1'
    for i in range(len(l)):
        c[i] = l[i]
    print("Transmitted bit is : ")
    print("".join(c))
    if (c == r):
        print("There's no error in transmission ..")
    else:
        print("There is error in transmission ...")

in_bit = input("Enter input bit : ")
l = [(in_bit[i:i+1]) for i in range(0, len(in_bit))]
polynomial_bit = input("Enter the polynomial : ")
p = [(polynomial_bit[i:i+1]) for i in range(0, len(polynomial_bit))]
received_bit = input("Received bit : ")
r = [(received_bit[i:i+1]) for i in range(0,len(received_bit))]
CRC(l,p,r)