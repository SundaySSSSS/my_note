# 删除xcode脚本
将如下内容存为文件, 赋予可执行权限, 执行即可
```
echo Removing your Xcode...
sudo rm -rf /Applications/Xcode.app
sudo rm -rf /Library/Preferences/com.apple.dt.Xcode.plist
rm -rf ~/Library/Preferences/com.apple.dt.Xcode.plist
rm -rf ~/Library/Caches/com.apple.dt.Xcode
rm -rf ~/Library/Application\ Support/Xcode
rm -rf ~/Library/Developer/Xcode
rm -rf ~/Library/Developer/CoreSimulator
rm -rf ~/Library/Developer/XCPGDevices
echo Your Xcode has been removed completely.
```