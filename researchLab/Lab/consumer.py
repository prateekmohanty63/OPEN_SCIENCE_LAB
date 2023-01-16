import pika


params=pika.URLParameters('amqps://ezcylmyw:UGkZ_27NHbYN8-WCyTLXWQlfKYN1KGGs@cow.rmq2.cloudamqp.com/ezcylmyw')

connection=pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue='expirement_queue')


def callback(ch,method,properties,body):
    
    print('Received in admin')
    print(body)

channel.basic_consume(queue='expirement_queue',on_message_callback=callback,auto_ack=True)
print('Started Consuming')

channel.start_consuming()

channel.close()