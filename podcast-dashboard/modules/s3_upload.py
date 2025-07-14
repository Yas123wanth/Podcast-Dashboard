import boto3

def upload_to_s3(file_path, bucket_name, object_name, aws_key, aws_secret, region, use_presigned_url=False):
    """
    Uploads a file to AWS S3 and returns the public URL or a presigned URL based on configuration.

    Parameters:
        file_path (str): Local path to file
        bucket_name (str): Target S3 bucket
        object_name (str): Desired path/name in S3
        aws_key (str): AWS access key
        aws_secret (str): AWS secret key
        region (str): AWS region
        use_presigned_url (bool): Whether to return a presigned URL

    Returns:
        str or None: S3 URL or presigned URL if successful, None if upload fails
    """
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret,
            region_name=region
        )

        # Upload file to S3
        s3.upload_file(file_path, bucket_name, object_name)

        if use_presigned_url:
            # Generate a presigned URL valid for 1 hour
            url = s3.generate_presigned_url(
                ClientMethod="get_object",
                Params={"Bucket": bucket_name, "Key": object_name},
                ExpiresIn=3600
            )
        else:
            # Construct public URL
            url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"

        return url

    except Exception as e:
        print(f"❌ S3 upload failed: {e}")
        return None

