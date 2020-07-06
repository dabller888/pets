### kali安装docker
Add Docker PGP key:
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' | sudo tee /etc/apt/sources.list.d/docker.list

kali上安装docker可以参考：
https://medium.com/@airman604/installing-docker-in-kali-linux-2017-1-fbaa4d1447fe

Update APT:
sudo apt-get update

Install Docker
sudo apt-get remove docker docker-engine docker.io
sudo apt-get install docker-ce

Test:
sudo docker run hello-world

sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

##### 安装kali
可以去官网https://www.kali.org/news/official-kali-linux-docker-images/ 下载kali docker镜像自行构建

install kali on docker:
docker pull kalilinux/kali-linux-docker
docker run -it –rm kalilinux/kali-linux-docker /bin/bash


##### 安装dvwa
拉取镜像
docker pull infoslack/dvwa

创建容器
docker run -dit -p 8080:80 --name dvwa infoslack/dvwa
或者
docker run -d -p 8080:80 -p 3306:3306 -e MYSQL_PASS="mypass" infoslack/dvwa

打开浏览器，这是dvwa
http://192.168.0.111:8080/setup.php
用户名：admin
密码：password

    容器停止/开启/删除
    docker stop dvwa
    docker start dvwa
    docker rm dvwa
    
    查看容器状态
    docker ps -a
    
    删除镜像
    docker rmi infoslack/dvwa



##### 安装vulnhub

https://github.com/vulhub/vulhub


