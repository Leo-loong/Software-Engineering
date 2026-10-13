#!/bin/bash
#以busybox:latest为基础镜像创建一个容器，容器名为container3
docker run --name container3 busybox echo "hello"
#然后将busybox:latest镜像删除
#********** Begin *********#
docker rm -f container3
docker rmi busybox:latest
#********** End **********#