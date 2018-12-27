import boto3

def main():
	print("Initializing Boto3 Client")
	
	sqs = boto3.client('sqs', region_name='', aws_access_key_id='', aws_secret_access_key='')
	sqs_url = ""

	print("Queues Available: ")
	print(sqs.list_queues())

	message = message_payload(
		'XXX Bot', 
		'999-abc-000', 
		'XXX@stowbots.com', 
		'DEV', 
		'{images : [\'Shinji\', \'Misato\', \'Rei\', \'Asuka\']}'
	)

	response = sqs.send_message(
		QueueUrl=sqs_url,
		DelaySeconds=10,
		MessageAttributes={
			'NameOfBot': {
				'DataType': 'String',
				'StringValue': message.name
			},
			'RequestId': {
				'DataType': 'String',
				'StringValue': message.request_id
			},
			'User': {
				'DataType': 'String',
				'StringValue': message.user
			},
			'Mode': {
				'DataType': 'String',
				'StringValue': message.mode
			}
		},
		MessageBody=(message.body)
	)

	print(response['MessageId'])

	print ("Exiting Main()")


class message_payload(object):

	def __init__(self, name, request_id, user, mode, body):
		self.name = name
		self.request_id = request_id
		self.user = user
		self.mode = mode
		self.body = body

	def print_name(self):
		print(self.name)

	def print_request_id(self):
		print(self.request_id)

	def print_user(self):
		print(self.user)

	def print_mode(self):
		print(self.mode)

	def print_body(self):
		print(self.body)


if __name__ == '__main__':
	main()