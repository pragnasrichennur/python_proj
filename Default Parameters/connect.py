def connect(host,port=3306,protocol='TCP'):
    return host,port,protocol

print(connect(host="IPv6"))
print(connect("IPv4"))
