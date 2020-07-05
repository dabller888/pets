### kali linux

##### 介绍
Kali Linux是基于Debian的Linux发行版， 设计用于数字取证操作系统。由Offensive Security Ltd维护和资助。最先由Offensive Security的Mati Aharoni和Devon Kearns通过重写BackTrack来完成，BackTrack是他们之前写的用于取证的Linux发行版 。
Kali Linux预装了许多渗透测试软件，包括nmap 、Wireshark 、John the Ripper，以及Aircrack-ng.[2] 用户可通过硬盘、live CD或live USB运行Kali Linux。Kali Linux既有32位和64位的镜像。可用于x86 指令集。同时还有基于ARM架构的镜像，可用于树莓派和三星的ARM Chromebook
2020年Kali Linux的最新版本为2020.2。

##### 安装
可以到kali linux官方网站 https://www.kali.org/ 下载对应平台镜像文件进行安装.

##### 安装后需要做的事情
###### PC版本kali linux更新
修改apt为清华大学软件源
$vim /etc/apt/source.list

deb https://mirrors.tuna.tsinghua.edu.cn/kali/ kali-rolling contrib main non-free

更新

$apt-get clean && apt-get update && apt-get upgrade && apt-get dist-upgrade

###### nethunter更新
$wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add

修改apt源
$vim /etc/apt/source.list

deb https://mirrors.tuna.tsinghua.edu.cn/kali/ kali-rolling contrib main non-free

更新

$apt-get clean && apt-get update && apt-get upgrade && apt-get dist-upgrade

###### 开启服务
$service apache2 start/stop/status

$service ssh start/stop

$update-rc.d -f ssh defaults 

###### 设置快捷键
设置→设备→键盘 中新建一个快捷键就好
名称：开启终端 
命令：gnome-terminal 
快捷键： Ctrl + Alt + T （这个自己按就好）

###### rdesktop
$apt-get install rdesktop
用法： rdesktop[options] server[:port]    
   命令参数常用的有：
    -u用户名
    -p密码
    -n客户端主机名（显示windows任务管理器中的连接客户端名）
    -g桌面大小（ 宽＊ 高）[也可以用 x(小写的X)]
     -f全屏模式,从全屏模式切换出来按Ctrl+Alt+Enter
    -a连接颜色深度（最高到16位），一般选16才会显示真彩色（window7支持32位）
    -0数字0表示连接上windows控制台，等效mstsc/console命令

$rdesktop -g 800x600 -a 16 -u administrator -p 123456-0 192.168.0.110:3389
退出全屏的方法：cttl + alt + enter

###### kali关闭iptables
安装：
$apt-get install ufw
关闭
$ufw disable # To disable the firewall
开启
$ufw enable # To enable the firewall

###### 安装googlepinyin
https://www.cnblogs.com/python-wen/p/9718534.html
$apt-cache search googlepinyin

$apt-get install fcitx-googlepinyin 

$apt-get install im-config 

$im-config 

$dpkg -l|grep googlepinyin

im-config设置默认为fcitx

###### 安装google chrome
下载安装包https://www.google.com/chrome/?brand=CHBD&gclid=EAIaIQobChMIlfOl6aSA6gIVxBx9Ch3lGgnhEAAYASAAEgJ-xvD_BwE&gclsrc=aw.ds
$dpkg -i google-chrome-stable_current_amd64.deb 
https://technowikis.com/11668/how-to-install-tor-or-google-chrome-on-kali-linux-2020

修改启动配置
#vim /opt/google/chrome/google-chrome 
exec -a "$0" "$HERE/chrome" "$@" --user-data-dir --no-sandbox

###### 安装WPS
下载安装包https://www.wps.cn/product/wpslinux/

###### 添加标准用户
$useradd -m user1

$passwd user1

$usermod -a -G sudo user1

$chsh -s /bin/bash user1

###### 安装File Roller（归档管理器）
$apt-get install unrar unace rar unrar p7zip zip unzip p7zip-full p7zip-rar file-roller -y

###### 屏幕录制 & 远程客户端
$apt install simplescreenrecorder remmina -y

###### 安装Filezilla FTP客户端
$apt-get install filezilla filezilla-common -y

###### 安装HTOP和NetHogs
$apt-get install htop nethogs -y

$htop

$nethogs eth0
  
###### 安装多终端工具terminator
$apt-get install terminator

快捷键：
1.Ctrl+Shift+e 垂直平分窗口 这样你就有了两个独立的工作区见,对于大屏幕的人是...
2.Ctrl+Shift+o 水平平分窗口 如果你分了两个垂直的工作区间之后发现宽度不够了...
3.Ctrl+Shift+s 隐藏/恢复滚动条 一般到了这里,我会去掉鸡肋的滚动条,果然清爽...
4.F11 进入退出全屏幕 到了这里你会发现,如果屏幕不够大,终端显示都挤在了一起,这时你...
5.Ctrl+Tab 在不同的工作区间循环 经过上面的操作,不出意外的话,我们现在已经

######  安装zsh并设置终端主题
$apt-get install zsh

$chsh -s /bin/zsh

或者$chsh -s /usr/bin/zsh root

$echo $SHELL

$sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

$ls -a ~/.oh-my-zsh/themes 

$vim ~/.zshrc

ZSH_THEME="gnzh"

$reboot












































