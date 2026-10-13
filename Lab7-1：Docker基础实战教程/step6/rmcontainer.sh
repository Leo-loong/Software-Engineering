#!/bin/bash

#注意如果想在右侧使用命令行模拟操作，请先输入
#service docker start
#否则将不能执行docker命令
#拉取ubuntu ，busybox最新镜像，实际生产中，docker pull 这一步可以省略，docker run的时候会自己去拉取。
docker pull ubuntu
docker pull busybox
#创建两个容器
docker run -itd ubuntu /bin/bash
docker run busybox echo "hello world"
#删除所有容器
#********** Begin *********#
# 停止所有运行中的容器
docker stop $(docker ps -aq)
# 删除所有容器
docker rm $(docker ps -aq)
#********** End **********#

