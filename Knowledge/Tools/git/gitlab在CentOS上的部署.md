# gitlab在CentOS上的部署
## 1， 配置yum源
vi /etc/yum.repos.d/gitlab-ce.repo
填入以下内容：
```
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/e17/
gpgcheck=0
enabled=1
```
备注“baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/e17/”是测试出来的结果，目前这个网址可用， 如果不可用后， 需要再尝试其他网址

## 2，更新本地yum缓存

sudo yum makecache

## 3，安装gitlab
sudo yum install gitlab-ce

## 之后因为提示需要policycoreutils-python而放弃
policycoreutils-python使用yum无法安装， 后放弃