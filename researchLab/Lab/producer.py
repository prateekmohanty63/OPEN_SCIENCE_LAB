import pika,json


params=pika.URLParameters('amqps://ezcylmyw:UGkZ_27NHbYN8-WCyTLXWQlfKYN1KGGs@cow.rmq2.cloudamqp.com/ezcylmyw')

connection=pika.BlockingConnection(params)

channel=connection.channel()

def publish(method,body):
    properties=pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='expirement_queue',body=json.dumps(body),properties=properties)