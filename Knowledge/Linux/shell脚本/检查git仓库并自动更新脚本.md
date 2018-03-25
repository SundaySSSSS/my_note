# 检查git仓库并自动更新脚本

```
echo "*************************"
cd ~/.emacs.d
echo "Checking Emacs Config Status"
if git status | grep 'nothing to commit' ; then
    echo "clean, try to pull from github"
    git pull origin
else
    echo "not clean, please check git status"
    exit
fi

echo "*************************"

cd ~/note/MyNote/
echo "Checking MyNote Status"
if git status | grep 'nothing to commit' ; then
    echo "clean, try to pull from github"
    git pull origin
else
    echo "not clean, please check git status"
    exit
fi

echo "Finished!!!"

```