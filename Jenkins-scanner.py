import requests
import sys

ip = sys.argv[1]
port = sys.argv[2]
protocol = sys.argv[3]

response = requests.get(protocol + '://' + ip + ':' + port).status_code
if response == 200:
    print(ip + ' is vulnerable on Port: ' + port)
else:
    print(ip + ' is not vulnerable')

