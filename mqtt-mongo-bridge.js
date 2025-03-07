const mqtt = require('mqtt');
const mongodb = require('mongodb');

const MongoClient = mongodb.MongoClient;
const url = 'mongodb+srv://genial:genial@cluster0.znvt9lz.mongodb.net/'; // Change this URL to your MongoDB connection string
const dbName = 'iot_db'; // Change this to your MongoDB database name
const collectionName = 'ActualData'; // Change this to your MongoDB collection name

const mqttServer = 'mqtt://test.mosquitto.org'; // Change this to your MQTT broker URL
const mqttPort = 1883;
const mqttClient = mqtt.connect(`${'mongodb+srv://genial:genial@cluster0.znvt9lz.mongodb.net/'}:${1883}`)
const mqttTopics = ['Temperature', 'Humidity', 'Sound', 'Light']; // Change this to your MQTT topics

MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true }, (err, client) => {
  if (err) throw err;

  const db = client.db(dbName);
  const collection = db.collection(collectionName);

  const mqttClient = mqtt.connect(mqttServer);

  mqttClient.on('connect', () => {
    console.log('Connected to MQTT broker');
    mqttClient.subscribe(mqttTopics);
  });

  mqttClient.on('message', (topic, message) => {
    const sensorData = {
      topic: topic,
      value: parseFloat(message.toString()),
      timestamp: new Date(),
    };

    // Insert data into MongoDB
    collection.insertOne(sensorData, (err, result) => {
        if (err) {
            console.error('Error inserting data into MongoDB:', err);
          } else {
            console.log('Data inserted into MongoDB:', sensorData);
          }
    });
  });
});
