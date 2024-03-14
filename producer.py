import json
import random
from faker import Faker
from models_contact import Contact
import pika

fake = Faker()

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue="email_hello_world")

for _ in range(5):
    full_name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    preferred_contact_method = random.choice(["email", "sms"])

    contact = Contact(
        full_name=full_name,
        email=email,
        phone=phone,
        preferred_contact_method=preferred_contact_method,
    )
    contact.save()

    message = {"contact_id": str(contact.id)}
    channel.basic_publish(
        exchange="", routing_key="email_hello_world", body=json.dumps(message)
    )
    print(f"Sent contact {contact.id} to the email queue")

connection.close()


# import json
# import pika
# from datetime import datetime
# from models import Contact
# from mongoengine import connect
#
# # Підключення до MongoDB
# connect(host='mongodb+srv://PythonDB:cud4BUXMwUmTI9A9@cluster0.zv0mgxq.mongodb.net/')
#
# credentials = pika.PlainCredentials('guest', 'guest')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
# channel = connection.channel()
#
# channel.exchange_declare(exchange="web16_exchange", exchange_type="direct")
# channel.queue_declare(queue='web16_queue', durable=True)
# channel.queue_bind(exchange='web16_exchange', queue='web16_queue')
#
#
# def create_contacts(num_contacts: int):
#     for i in range(num_contacts):
#         contact = Contact(
#             full_name=f"John Doe {i}",
#             email=f"john.doe{i}@example.com"
#         )
#         contact.save()
#
#         message = {
#             'contact_id': str(contact.id)
#         }
#
#         channel.basic_publish(exchange="web16_exchange", routing_key='web16_queue', body=json.dumps(message))
#
#     connection.close()
#
# if __name__ == '__main__':
#     create_contacts(10)