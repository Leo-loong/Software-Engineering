#创建一个空文件夹，并进入其中
mkdir newdir1
cd newdir1
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
echo 'FROM busybox' > Dockerfile

#在基础镜像的基础上，创建一个hello.txt文件
echo 'RUN touch hello.txt' >> Dockerfile
#********** End **********#
#使用Dockerfile创建一个新镜像，镜像名为busybox:v1
docker build -t busybox:v1 .