BUCKET_NAME = "test-app-data"
FILENAME = "the_adventures_of_sherlock_holmes.epub"

from MinioClient import MinioClient

client = MinioClient()

# List all bucket objects
client.listObjects(BUCKET_NAME)

# Upload an object to a bucket from a local file
client.putObject(FILENAME, BUCKET_NAME, FILENAME, "application/epub+zip")

# List objects to check if upload was made
client.listObjects(BUCKET_NAME)

# Get object from bucket and write it to a local file
client.getObject(BUCKET_NAME, FILENAME, "downloaded_" + FILENAME)