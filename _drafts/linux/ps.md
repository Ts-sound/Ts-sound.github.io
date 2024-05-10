
# ps
> Linux中的ps命令是Process Status的缩写。ps命令用来列出系统中当前运行的那些进程。ps命令列出的是当前那些进程的快照，就是执行ps命令的那个时刻的那些进程，如果想要动态的显示进程信息，就可以使用top命令。
> ps 可以通过用户名、进程名 等信息查找对应的进程；
```bash
# 在一个终端运行top
top

# 在另一个终端 
ps -aux | grep top

root@ecs-d3d0:~/tong/test# ps -aux | grep top
root     24093  0.1  0.0  41928  3852 pts/12   S+   11:52   0:00 top
root     24274  0.0  0.0  14220   936 pts/18   S+   11:52   0:00 grep --color=auto top
# USER    PID   %CPU %MEM  VSZ    RSS TTY      STAT START   TIME COMMAND

```