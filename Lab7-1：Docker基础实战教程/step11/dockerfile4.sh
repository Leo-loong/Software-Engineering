#创建一个空文件夹，并进入其中
mkdir newdir4
cd newdir4
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
#以busybox:latest为基础镜像
echo 'FROM busybox:latest' > Dockerfile

#声明暴露3000端口
echo 'EXPOSE 3000' >> Dockerfile

#将变量var1="test"设置为环境变量
echo 'ENV var1="test"' >> Dockerfile

#设置工作目录为/tmp
echo 'WORKDIR /tmp' >> Dockerfile

#在工作目录下创建一个1.txt文件
echo "RUN touch 1.txt" >> Dockerfile
#********** End **********#


#文件内容完毕，在当前文件夹中执行
#********** Begin *********#
#以该Dockerfile构建一个名为testimage:v1的镜像
docker build -t testimage:v1 .
#********** End **********#