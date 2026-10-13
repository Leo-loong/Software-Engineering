#创建一个空文件夹，并进入其中
mkdir newdir3
cd newdir3
#创建一个Dockerfile文件
touch Dockerfile

#假设我的Dockerfile文件为
#FROM ubuntu
#RUN mkdir dir1
#可以这么写：
# echo 'FROM ubuntu' > Dockerfile
# echo 'RUN mkdir dir1'>> Dockerfile

#输入Dockerfile文件内容
#********** Begin *********#
#以busybox为基础镜像
echo 'FROM busybox:latest' > Dockerfile

#默认情况下，将启动命令设置为df -Th。要求df命令不能被覆盖，但-Th能够被覆盖。
echo 'ENTRYPOINT ["df"]' >> Dockerfile
echo 'CMD ["-Th"]' >> Dockerfile
#********** End *********#


#文件内容完毕，在当前文件夹中执行
#********** Begin *********#
#以该Dockerfile构建一个名为mydisk:v1的镜像
docker build -t mydisk:v1 .
#********** End *********#