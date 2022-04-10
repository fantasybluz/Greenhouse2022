#! /usr/bin/python3
import threading
import paho.mqtt.client as mqtt
import time
import json
import requests

# config
login_url = 'https://cpe.csie.ncut.edu.tw/user/login'
recv_data_url='https://cpe.csie.ncut.edu.tw/data'

#DEBUG = True
DEBUG = False

json_data = {
    "nodeName": "01",
    "esp11": {
        "topic": "01/1/esp11",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "LightSensor": 0
    },
    "esp111":{
        "topic": "01/1/esp111",
        "status": 0,
        "N": 0,
        "P": 0,
        "K": 0
    },
    "esp12": {
        "topic": "01/1/esp12",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "SoilMoistureSensor2": 0
    },
    "esp21": {
        "topic": "01/2/esp21",
        "status": 0,
        "Co2": 0,
        "SoilMoistureSensor1": 0,
        "TempSensor": 0.0,
        "HumiSensor": 0
    },
    "esp22": {
        "topic": "01/2/esp22",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "SoilMoistureSensor2": 0
    },
    "esp31": {
        "topic": "01/3/esp31",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "LightSensor": 0,
        "AirSensor": {
            "PM10": 0.0,
            "PM25": 0.0,
            "PM100": 0.0,
            "P03": 0.0,
            "P05": 0.0,
            "P10": 0.0,
            "P25": 0.0
        }
    },
    "esp32": {
        "topic": "01/3/esp32",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "SoilMoistureSensor2": 0
    },
    "esp41": {
        "topic": "01/4/esp41",
        "status": 0,
        "Co2": 0,
        "SoilMoistureSensor1": 0,
        "TempSensor": 0.0,
        "HumiSensor": 0
    },
    "esp42": {
        "topic": "01/4/esp42",
        "status": 0,
        "SoilMoistureSensor1": 0,
        "SoilMoistureSensor2": 0,
        "TempSensor": 0.0,
        "HumiSensor": 0
    },
    "esp51":{
        "topic": "01/5/esp51",
        "status": 0,
        "PH": 0
    }
    
}

# node-1
# block-1
# esp11

def debug_use():
    while True:
        # every 5 sec set status back to 0
        # json_data['esp11']['status'] = 0
        # json_data['esp12']['status'] = 0
        # json_data['esp21']['status'] = 0
        # json_data['esp22']['status'] = 0
        # json_data['esp31']['status'] = 0
        # json_data['esp32']['status'] = 0
        # json_data['esp41']['status'] = 0
        # json_data['esp42']['status'] = 0
        # change to request to django by url
        ###########################################
        # while(True):
        #     r=requests.get(url,params=json_data)
        #     if(r.json()=='data recv'):
        #         break
        ###########################################

        print(json.dumps(json_data, indent=4))
        time.sleep(5)

# esp11
def on_connect_0(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp11")
def on_message_0(client, userdata, msg):
    json_data['esp11']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp11']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "LightSensor":
        json_data['esp11']['LightSensor'] = 98

# esp12
def on_connect_1(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp12")
def on_message_1(client, userdata, msg):
    json_data['esp12']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp12']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "SoilMoistureSensor2":
        json_data['esp12']['SoilMoistureSensor2'] = x[1]

# esp21
def on_connect_2(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp21")
def on_message_2(client, userdata, msg):
    json_data['esp21']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "Co2":
        json_data['esp21']['Co2'] = x[1]
    elif x[0] == "SoilMoistureSensor1":
        json_data['esp21']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "TempSensor":
        json_data['esp21']['TempSensor'] = x[1]
    elif x[0] == "HumiSensor":
        json_data['esp21']['HumiSensor'] = x[1]

# esp22
def on_connect_3(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/2/esp22")
def on_message_3(client, userdata, msg):
    json_data['esp22']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp22']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "SoilMoistureSensor2":
        json_data['esp22']['SoilMoistureSensor2'] = x[1]

# esp31
def on_connect_4(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp31")
def on_message_4(client, userdata, msg):
    json_data['esp31']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp31']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "LightSensor":
        json_data['esp31']['LightSensor'] = 98

    x = msg.payload.decode().split()
    if x[0] == "PM10":
        json_data['esp31']["AirSensor"]['PM10'] = x[1]
    elif x[0] == "PM25":
        json_data['esp31']["AirSensor"]['PM25'] = x[1]

# esp32
def on_connect_5(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/3/esp32")
def on_message_5(client, userdata, msg):
    json_data['esp32']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp32']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "SoilMoistureSensor2":
        json_data['esp32']['SoilMoistureSensor2'] = x[1]

# esp41
def on_connect_6(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp41")
def on_message_6(client, userdata, msg):
    # print(msg.payload.decode())
    json_data['esp41']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "Co2":
        json_data['esp41']['Co2'] = x[1]
    elif x[0] == "SoilMoistureSensor1":
        json_data['esp41']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "TempSensor":
        json_data['esp41']['TempSensor'] = x[1]
    elif x[0] == "HumiSensor":
        json_data['esp41']['HumiSensor'] = x[1]

# esp42
def on_connect_7(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/4/esp42")
def on_message_7(client, userdata, msg):
    json_data['esp42']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "SoilMoistureSensor1":
        json_data['esp42']['SoilMoistureSensor1'] = x[1]
    elif x[0] == "SoilMoistureSensor2":
        json_data['esp42']['SoilMoistureSensor2'] = x[1]
    elif x[0] == "TempSensor":
        json_data['esp42']['TempSensor'] = x[1]
    elif x[0] == "HumiSensor":
        json_data['esp42']['HumiSensor'] = x[1]

# esp111
def on_connect_8(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/1/esp111")
def on_message_8(client, userdata, msg):
    json_data['esp111']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "N":
        json_data['esp111']['N'] = x[1]
    elif x[0] == "P":
        json_data['esp111']['P'] = x[1]
    elif x[0] == "K":
        json_data['esp111']['K'] = x[1]

# esp51
def on_connect_9(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("01/5/esp51")
def on_message_9(client, userdata, msg):
    json_data['esp51']['status'] = 1
    x = msg.payload.decode().split()
    if x[0] == "PH":
        json_data['esp51']['PH'] = x[1]

def run_all_mqtt_recv():
    for i in range(10):

        exec('client'+str(i)+" = mqtt.Client()")
        exec("client"+str(i)+".connect('localhost', 1883, 60)")
        exec("client"+str(i)+".on_connect = on_connect_"+str(i))
        exec("client"+str(i)+".on_message = on_message_"+str(i))
        exec("client"+str(i)+".loop_start()")
##################################
# Sending to server

def login():
    acc = {
        'username': 'mqtt',
        'password': 'Mqtt8718'
    }
    r = requests.post(login_url, json=acc, verify=False)
    token = r.json()['token']
    return token

def send_data_to_server(token):
    headers={'Authorization': f'Token {token}'}
    r = requests.post(recv_data_url,json = json_data,headers=headers, verify=False)
    status=r.status_code
    return status


def run():
    token=login()
    while True:
        try:
            status=send_data_to_server(token)
            #save_database()
            print(status)
            # not yet login
            if status == 401:
                token=login()
                # no rest 5 sec straight to new loop
                continue
            time.sleep(5)
        except Exception as e:
            print(e)
            time.sleep(5)


# 等到0秒時開始
def wait_till_time():
    local_time = time.localtime().tm_sec
    time.sleep(60-local_time)

def save_database():
    print(json.dumps(json_data, indent=4))



if __name__ == "__main__":
    if not DEBUG:
        wait_till_time()
        run_all_mqtt_recv()
        run()
    else:
        run_all_mqtt_recv()
        debug_use()
