#无论任何输入都会认为正确，本关的目的是学习ONBUILD和VOLUME指令
FROM busybox
ONBUILD RUN touch 1.txt