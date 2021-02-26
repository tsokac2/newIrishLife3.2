import os
import boto3, botocore
if os.path.exists("env.py"):
    import env

secret_s3_key_id = os.environ.get("S3_KEY_ID")
secret_s3_secret = os.environ.get("S3_SECRET")
secret_s3_bucket = os.environ.get("S3_BUCKET_NAME")

s3 = boto3.client(
   "s3",
   secret_s3_key_id=S3_KEY_ID,
   aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
                }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e