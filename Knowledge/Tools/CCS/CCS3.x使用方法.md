# CCS3.x使用方法

```
1. 快捷键操作
	Ctrl+F6
	Ctrl+Shift+F6
2. 设置显示行号和高亮显示当前行
	Option->Editor->View Setups->General->Line Numbers
	Option->Editor->View Setups->General->Highlight Current Line
3. 解决自动提示失效问题
	删除工程目录下的“NDC300.CS_”文件夹，重新编译即可
4. 点击某个文件，右键选择“File Specific Options”，指定优化选项
5. 点击工程文件，右键选择“Build Options”,选择“Compiler”,选择
	“Preprocessor”，查看Pre-Define Symbol (-d)，指定宏开关
6. 使用CCS调试程序
	6.1 连接好硬件，上电按住“Alt+C”，连接开发器，提示连接成功
		注：如果不成功，则查看设备管理器是否有“SEED XDS560
		PLUS JTAG Emulator”如果没有则重新连接开发器。
	6.2 点击“File”->“Load Program”加载程序，点击绿色的“单步执行”
		然后点击小人“run”，程序开始运行
	6.3 点击“halt”停止调试，即可修改代码，然后“build”重新编译，
		重
7. 使用CCS烧写boot程序
CHIP_DM642;_DSP_DM642;DEBUG;DM642;DSP_ISRAM;_DEBUG;NDC300L_MBU;NDC300L_AV;NDC560_13;NOPC;DEVICE
8. 配置选择
	启动配置
	642平台--NDC300L/NDC300L-AV

	Setup CCStudio V3.3中添加对应的设置项
		-Family 选择C64xx
		-PlatForm 选择xds560 emulator
		-Endianness 选择All
	即可

在相机启动时，按下Alt+C进行加载（连接CCS和相机？）
然后单步运行几下，之后再Run（左侧边线上的按钮）
编译：在工程上右键Build
然后把编译出来的东西Load到相机里，File->Load Program
```
