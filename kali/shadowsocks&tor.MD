### shadowsocks & tor安装与使用

#### pip安装与升级
apt-get install python-pip

pip -V

python -m pip install --upgrade pip

#### 安装shadowsocks
pip install shadowsocks

pip uninstall shadowsocks

创建shadowsocks配置文件
mkdir /etc/shadowsocks

vim /etc/shadowsocks/shadowsocks.json

{
    "server":"1.1.1.1",
    "server_port":1035,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"password",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false,
    "workers": 1
}

ls /etc/shadowsocks/shadowsocks.json 

##### 设置shadowsocks服务并开机启动
sudo vim /etc/init.d/shadowsocks

#!/bin/sh

start(){
        sslocal -c /etc/shadowsocks/shadowsocks.json -d start
}

stop(){
        sslocal -c /etc/shadowsocks/shadowsocks.json -d stop
}

case "$1" in
start)
        start        
        ;;
stop)
        stop        
        ;;
reload)
        stop
        start        
        ;;
*)
        echo "Usage: $0 {start|reload|stop}"
        exit 1        
        ;;
esac

sudo chmod +x /etc/init.d/shadowsocks

sudo update-rc.d shadowsocks defaults

sudo service shadowsocks {start|reload|stop}

##### 设置全局代理
export ALL_PROXY=socks5://127.0.0.1:1080

unset ALL_PROXY

##### 利用proxychains做全局代理
vi /etc/proxychains.conf

#socks4       127.0.0.1 9050

#socks5  127.0.0.1 1080

socks5       127.0.0.1 9050

cp /usr/lib/proxychains3/proxyresolv /usr/bin/

proxyresolv www.target.com

proxyresolv www.google.com

##### 使用ProxyChains 启动firefox
proxychains firefox

proxychains msfconsole //启动msf

proxychains sqlmap //通过代理启动sqlmap

proxychains tor


#### 安装tor
$ sudo apt-get install tor

tor官网下载tor https://www.torproject.org/download/

$ wget https://www.torproject.org/dist/torbrowser/9.0.6/tor-browser-linux64-9.0.6_en-US.tar.xz

$ tar -xvJf tor-browser-linux64-6.5.1_zh-cn.tar.xz

cd tor-browser-linux64-6.5.1_zh-cn/Browser

chown -R root:root *

./start

#### 问题：
1.Kali2.0 update到最新版本后安装shadowsocks服务报错问题
https://www.lstazl.com/kali2-0-update%E5%88%B0%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC%E5%90%8E%E5%AE%89%E8%A3%85shadowsocks%E6%9C%8D%E5%8A%A1%E6%8A%A5%E9%94%99%E9%97%AE%E9%A2%98/
vim /usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/openssl.py

2.kali 为了安全考虑。会禁止使用root用户去执行。
找到解压目录，然后找到tor-browser-linux64-6.5.1_zh-cn/Browser/start-tor-browser文件，打开。找到下图位置。然后把0修改1
if [ "`id -u`" -eq 1 ];then

