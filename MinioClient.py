
from minio import Minio

class MinioClient:

    def __init__(self):
        self.client = Minio(
            "localhost:9000",
            access_key="app-user",
            secret_key="app-user",
            secure=False
        )

    def listObjects(self, bucket_name):
        objects = self.client.list_objects(bucket_name)
        print(f"Number of objects in bucket: {len(list(objects))}")
        for obj in objects:
            print(obj)

    def putObject(self, file_path, bucket_name, object_name, content_type):
        result = self.client.fput_object(bucket_name, object_name, file_path, content_type)
        
        print(f"created {result.object_name} object; etag: {result.etag}, version-id: {result.version_id}")

    def getObject(self, bucket_name, object_name, file_path_to_save):
        result = self.client.fget_object(bucket_name, object_name, file_path_to_save)
