# https://pypi.org/project/paho-mqtt/

# -----------
#
# @file     mqtt_class.py
# @date     November, 2024
# @class    CITE 165
# @brief    A class to handle connecting to an online MQTT server.
# 
# ------

try:
    import paho.mqtt.client as paho
    from paho import mqtt
except Exception as e:
    # print(f"error with import: {e}")
    print("Error: please install 'paho.mqtt.client' module.")
    print("Use: pip3 install paho-mqtt")
else:
    pass

import os

class MQTT_Connector:
    def __init__(self, c_id = None, topics = [], debug=False):
        self.client = None
        self.client_id = c_id
        self.topics = topics        # must be list of strings of topics

        if self.client_id == None:
            self.client_id = "NA"
        
        for topic in self.topics:
            if type(topic) != str:
                self.topics.remove(topic)
        
        self.message_queue = []
        self.debug = debug
    
    def connect_MQTT(self):
        """connect to cloud hosted MQTT broker
        """
        if self.debug:
            print("start connecting")
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION1, self.client_id)

        # set up call backs
        self.client.on_connect = self.on_connect
        ip_addr = "453e51c107604519a5fd673fd39f1313.s1.eu.hivemq.cloud"
        port = 8883
        username = "student"
        password = "cs383_students"
        # connect
        self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self.client.username_pw_set(username, password)
        self.client.connect(host=ip_addr, port=port)

        # more callbacks
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.on_disconnect = self.on_disconnect
        self.client.on_publish = self.on_publish

        if self.debug:
            print(f'starting subscribe to: {self.topics}')
        for t in self.topics:
            self.client.subscribe(t)

        # return self.client 
    
    def publishMessage(self, topic, message):
        """Send a message to broker. Will reset all wait variables to False

        :param string topic:    what topic you want to publish to
        :param string message:  what message you are sending to the topic
                                coords must be sent in a list in a string
                                i.e., "[1,2,3,4,5,6]"
        """
        if self.debug:
            print("starting to publish")

        new_msg = f"{self.client_id}: {message}"
        
        # set up error handling of not publishing right away
        res = self.client.publish(topic, new_msg, qos=1)
        res.wait_for_publish()

        if res[0] == 0:
            print("Submission sent!")
        else:
            print("Submission failed.")

    
    def loop_start(self):
        self.client.loop_start()
    
    def loop_stop(self):
        self.client.loop_stop()
    
    def disconnect(self):
        self.client.disconnect()
    
    def loop_forever(self):
        self.client.loop_forever()

    # callbacks

    def on_connect(self, client, userdata, flags, rc, properties=None):
        """When connected to MQTT broker, print connected.
        """
        if rc==0 and self.debug:
            print(f'connected successfuly code={rc}')

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        """When successfully subscribed to a topic, print.
        """
        if self.debug:
            print(f'Subscribed: {mid} {granted_qos}')

    def on_publish(self, client, userdata, mid, properties=None):
        """When message successfully published to MQTT broker, print
        """
        if self.debug:
            print(f'mid: {mid}')

    def on_message(self, client, userdata, msg):
        """When message received from broker, print out message. This is where we can also start synchronizing robots
        """
        if self.debug:
            print("\nmessage received")
        message_string = msg.payload.decode("ascii")
        i = message_string.find(':')
        message_string = message_string[i+2:-1]
        
        
        self.message_queue.append(message_string)
        if self.client_id == "Teacher":
            self.print_all_messages()
        else:
            print(f'{msg.topic}/{message_string}')
            
    def on_disconnect(self, client, userdata, rc, properties=None):
        """When successfully disconnected from broker, print.
        """
        if rc == paho.MQTT_ERR_SUCCESS and self.debug:
            print("Disconnected successfully")
        elif self.debug:
            print("Unexpected disconnect")
    
    def print_all_messages(self):
        os.system('clear')
        print(f"\n{'Time':12} {'Student Name':20} {'Killer':20} {'Next Attack':20} {'Home Base':20} {'Leader':10}")
        print(f"{'----':12} {'------------':20} {'------':20} {'-----------':20} {'---------':20} {'------':10}")
        for m in self.message_queue:
            print(m)


# -- testing --

# connector = MQTT_Connector("Teacher", ["cite165"])

# connector.connect_MQTT()
# connector.loop_start()

# print('listening')

# connector.publishMessage('cite165', 'test message')

# time.sleep(5)

# connector.loop_stop()
# connector.disconnect()