#注意如果想在右侧使用命令行模拟操作，请先输入
#service docker start
#否则将不能执行docker命令

#基于ubuntu镜像创建并在后台启动一个名为container2的容器
#拉取ubutun 最新镜像，实际生产中，docker pull ubutun可以省略，docker run的时候会自己去拉取。
docker pull ubuntu
docker run -itd --name container2 ubuntu /bin/bash
#由于测试环境不允许从终端输入，所以请使用docker exec完成任务
#********** Begin *********#
docker exec container2 touch 1.txt
#********** End **********#
