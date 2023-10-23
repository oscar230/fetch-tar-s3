import boto3
import tarfile
import schedule
import time
import os

def job():
    s3 = boto3.client(
        's3',
        endpoint_url=os.environ['ENDPOINT_URL'],
        aws_access_key_id=os.environ['ACCESS_KEY'],
        aws_secret_access_key=os.environ['SECRET_KEY']
    )

    # List objects in the bucket
    objects = s3.list_objects_v2(Bucket=os.environ['BUCKET_NAME'])

    for obj in objects.get('Contents', []):
        file_name = obj['Key']
        # Download the latest archive
        s3.download_file(os.environ['BUCKET_NAME'], file_name, '/tmp/website.tar.gz')
        
        # Unpack the archive into the shared Docker volume
        with tarfile.open('/tmp/website.tar.gz', 'r:gz') as file:
            file.extractall(path=os.environ['DEST_PATH'])
        
        # Optionally, remove the downloaded archive and the archive from MinIO
        os.remove('/tmp/website.tar.gz')
        s3.delete_object(Bucket=os.environ['BUCKET_NAME'], Key=file_name)

# Schedule the job every hour (adjust as needed)
schedule.every().hour.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
