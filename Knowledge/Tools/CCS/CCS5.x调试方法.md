# CCS5.x调试方法

```
重启电脑，在开机时按F8， 选择禁用XXXXX签名（倒数第二个）

在全英文路径下右键，以管理员权限运行驱动安装程序，安装按成后重启，依然选择禁用XXXXX签名 启动

启动CCS，Target->New Config... 选择SEEDXDS560。。。 和  Ti814X
完成后在设置文件上右键，Launch Current 。。

之后选择要连接的核，如DSP（C674X_0），右键Connect Target
之后Target->Load Symbols

Symbols,
dsp对应
linux的对应：
Z:\NVC200E\ipnc_uc\target\filesys\opt\ipnc_bin\ipnc_rdk_mcfw.out（ipnc_dfserver的）
sys_server,video等（ipnc_app的）

dsp的：
Z:\NVC200E\ipnc_uc\target\filesys\opt\ipnc_bin\firmware\ipnc_rdk_fw_c6xdsp.xe674

m3的：
和dsp在一个文件夹，其他的两个


```
