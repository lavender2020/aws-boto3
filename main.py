import boto3
from config import setting
import logging
from botocore.exceptions import ClientError
import os


s3_client = boto3.client('s3')

# Download file from s3
with open('files/download.png', 'wb') as f:
    s3_client.download_fileobj('appen-vbsiv-stage', 'victor/tag.png', f)


# Upload files
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    STAT = upload_file('/app/files/test.txt', setting.BUCKET_NAME)
    if STAT:
        print('upload file successfully.')
    else:
        print('upload failed!')

# list buckets
response = s3_client.list_buckets()

print("Listing Amazon S3 Buckets:")
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")

