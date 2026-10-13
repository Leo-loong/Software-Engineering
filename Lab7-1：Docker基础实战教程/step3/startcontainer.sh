#注意如果想在右侧使用命令行模拟操作，请先输入
#service docker start
#否则将不能执行docker命令

#创建并启动一个容器，容器名为firstContainer，具备busybox的运行环境。并输出hello world
#拉取busybox最新镜像
docker pull busybox
#********** Begin *********#
docker run --name firstContainer busybox echo "hello world"
#********** End **********#

