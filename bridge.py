import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime
import pytz
import json

# MQTT configuration
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883 
mqtt_topics = ["TemperatureAI", "HumidityAI", "SoundAI", "LightAI"]  

# MongoDB configuration
mongo_uri = "mongodb+srv://genial:genial@cluster0.znvt9lz.mongodb.net/" 
mongo_db_name = "iot_db"  
mongo_collection_name = "Room_100"  

sensor_readings = {"TemperatureAI": None, "HumidityAI": None, "SoundAI": None, "LightAI": None}


# MQTT callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    # Subscribe to MQTT topics
    for topic in mqtt_topics:
        client.subscribe(topic)



# MQTT callback when a message is received
def on_message(client, userdata, msg):
    payload_str = msg.payload.decode()
    print(f"Received MQTT message - Topic: {msg.topic}, Message: {payload_str}")

    unified_packet = {}
   
    try:
        sensor_value = float(payload_str)
    except ValueError:
        print(f"Error converting payload '{payload_str}' to float for topic '{msg.topic}'")
        return
    #print("Sensor value:", sensor_value)
    
    sensor_readings[msg.topic] = sensor_value

    if all(sensor_readings.values()):
        cet_timezone = pytz.timezone("Europe/Paris")
        timestamp_str = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(cet_timezone).strftime("%Y-%m-%d %H:%M:%S")
       
        # Create a unified JSON packet
        unified_packet = {
            "timestamp": f'{timestamp_str}',
            "temperature": sensor_readings["TemperatureAI"],
            "humidity": sensor_readings["HumidityAI"],
            "sound": sensor_readings["SoundAI"],
            "light": sensor_readings["LightAI"],
            "room_name" : mongo_collection_name ,
        }
        #json_data = json.dumps(unified_packet)

        #print("unified_data:", unified_packet)

    # MongoDB connection and insertion
    with MongoClient(mongo_uri) as client:
        db = client[mongo_db_name]
        collection = db[mongo_collection_name]

        # Insert unified data into MongoDB
        collection.insert_one(unified_packet)
        print("Unified data inserted into MongoDB:", unified_packet)

# Create MQTT client instance
mqtt_client = mqtt.Client()

# Set MQTT callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT broker
mqtt_client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop
mqtt_client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Script terminated by user")


