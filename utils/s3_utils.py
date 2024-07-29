import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def upload_file_to_s3(file, filename):
    try:
        s3_client.upload_fileobj(file, BUCKET_NAME, filename)
        return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
    except NoCredentialsError:
        return None
