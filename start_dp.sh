#!/bin/bash

/home/pi/Share/dp/zookeeper/bin/zkServer.sh start;
echo 'Zookeeper Started'

/home/pi/Share/dp/kafka/bin/kafka-server-start.sh -daemon /home/pi/Share/dp/kafka/config/server.properties;
echo 'Kafka Started'

sleep 30

sudo service grafana-server start;
echo 'Grafana Started'


nohup python3.7 /home/pi/Share/dp/generate.py &
echo 'Data Generator Started'

sleep 30

/home/pi/Share/dp/kafka/bin/connect-standalone.sh -daemon /home/pi/Share/dp/kafka/config/dp-standalone.properties /home/pi/Share/dp/kafka/config/dp-file-source.properties ;
echo 'Kafka worker Started'

sleep 60

nohup python3.7 /home/pi/Share/dp/consumer.py &

sleep 5

echo 'Consumer Started'

echo 'Platform Started'

#echo 'Go and start consumer... '

