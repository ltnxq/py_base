import time

from paho.mqtt import client as mqtt_client

broker = "192.168.80.128"
port  = 1883
topic = "/test/code"

#服务端连接认证信息
username = 'user'
password = 'jsTh}!2023'

client_id_ = "local_80_128_3"

def connect_mqtt():
    def on_connect(client,userdata,flags,rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect,return code %d\n",rc)
    
    client = mqtt_client.Client(client_id = client_id_)
    # 设置crt证书
    # client.tls_set(ca_certs='./server-ca.crt')
    # 设置用户名和密码
    client.username_pw_set(username, password)  
    client.on_connect = on_connect
    client.connect(broker,port)
    return client

def subscribe(client):
    def on_message(client,userdata,msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == "__main__":
    run()