import mysql.connector
from kafka import KafkaConsumer

while True:
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', database='dp', password='xxxxxxx')
    cursor = cnx.cursor()
    consumer = KafkaConsumer('cpu_temp')
    records = []

    for msg in consumer:
        curr = str(msg[6])
        records.append(curr)
        if len(records) % 2 == 0:
            break

    cursor = cnx.cursor()
    for r in records:
        r = r.replace("b'", "").replace(",","").split("|")
        command = "INSERT INTO cpu_temp VALUES ('" + r[0] + "','" + r[1] +  ")"
        print(command)
        cursor.execute(command)
    cursor.execute('select count(1) as cnt from cpu_temp')

    for cnt in cursor:
        print(cnt)

    cnx.commit()
    cursor.close()
    cnx.close()

