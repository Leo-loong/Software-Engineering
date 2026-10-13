#创建一个空文件夹，并进入其中
mkdir newdir2
cd newdir2
#创建一个文件夹dir1，将其压缩，然后删除dir1
mkdir dir1 && tar -cvf dir1.tar dir1 && rmdir dir1
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

#并将上下文目录下的dir1.tar“解压提取后”，拷贝到busybox:v3的./
echo 'ADD dir1.tar ./' >> Dockerfile
#********** End **********#

#文件内容完毕，在当前文件夹中执行
#********** Begin *********#
#以该Dockerfile构建一个名为busybox:v3的镜像
docker build -t busybox:v3 .
#********** End **********#