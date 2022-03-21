import os
import boto3
from dotenv import load_dotenv
load_dotenv()


username = 'admin@gmail.com'
password = '#Admin1234'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
response = client.sign_up(
    ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
    Username=username,
    Password=password
)

print(response)