import boto3

def main(): 
	print("Initializing Boto3 Client")
	
	sqs = boto3.client('sqs', region_name='', aws_access_key_id='', aws_secret_access_key='')
	sqs_url = ''

	print("Consuming Message")
	response = sqs.receive_message(
		QueueUrl=sqs_url,
		AttributeNames=['ALL'],
		MaxNumberOfMessages=1,
		WaitTimeSeconds=1,
		ReceiveRequestAttemptId='string'
	)

	print("Received Message")
	print(response['Messages'])
	print("MessageId: " + response['Messages'][0]['MessageId'])
	print("ReceiptHandle: " + response['Messages'][0]['ReceiptHandle'])
	print("MessageBody: " + response['Messages'][0]['Body'])

	print("Deleting Message")
	sqs.delete_message(
		QueueUrl=sqs_url,
		ReceiptHandle=response['Messages'][0]['ReceiptHandle']
	)

	print("Successfully Deleted Message: " + response['Messages'][0]['MessageId'])
	print("Exiting Main()")


if __name__ == '__main__':
	main()