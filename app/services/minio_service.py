from minio import Minio
from app.config import settings

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

def upload_file(file, filename):
    if not client.bucket_exists(settings.MINIO_BUCKET):
        client.make_bucket(settings.MINIO_BUCKET)

    client.put_object(
        settings.MINIO_BUCKET,
        filename,
        file.file,
        length=-1,
        part_size=10*1024*1024
    )

    return filename