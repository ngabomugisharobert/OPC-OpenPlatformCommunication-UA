from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"

client = Client(url)

client.connect()
print("client connected")

while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)
    
    TIME = client.get_node("ns=2;i=4")
    Time = TIME.get_value()
    print(Time)

    time.sleep(4)
