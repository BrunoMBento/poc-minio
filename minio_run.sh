#!/bin/bash

docker run -d -p 9000:9000 -p 9001:9001 \
    -v /media/bruno/hdd/minio-data:/data \
    quay.io/minio/minio server /data --console-address ":9001"