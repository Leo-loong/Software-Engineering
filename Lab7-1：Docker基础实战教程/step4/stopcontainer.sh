#!/bin/bash

#注意如果想在右侧使用命令行模拟操作，请先输入
#service docker start
#否则将不能执行docker命令

#以ubuntu镜像为基础，创建并在后台启动了一个名为firstContainer的容器（-d看不懂没关系，下一关会介绍的）
#拉取ubutun 最新镜像，实际生产中，docker pull ubutun可以省略，docker run的时候会自己去拉取。
docker pull ubuntu
docker run -itd --name firstContainer ubuntu /bin/bash
#将firstContainer容器停止！
#********** Begin *********#
docker stop firstContainer
#********** End **********#

