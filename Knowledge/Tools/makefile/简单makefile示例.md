# 简单makefile示例

```
DLL = LaneCtrl.so

#bin在当前目录的相对位置
BIN_PATH_CUR=../$(BIN_PATH)

OBJS += server/server.o server/server_comm.o 
OBJS += client/client.o
OBJS += msg/msg.o 
OBJS += utils/utils.o utils/cjson/cjson.o utils/json_utils.o
OBJS += utils/zlog/zlog_utils.o
OBJS += LaneCtrlClientDll.o
OBJS += LaneCtrlServerDll.o
OBJS += LaneCtrlCommonDll.o

CFLAGS = -g

all: clean $(DLL)
test: clean $(TEST)

$(DLL) : $(OBJS)
	#从bin目录中拷贝nanomsg, zlog动态库到此目录进行编译链接
	cp $(BIN_PATH_CUR)/libnanomsg.so* ./
	cp $(BIN_PATH_CUR)/libzlog.so* ./
	$(CC) $(CFLAGS) -shared -o $(DLL) $(OBJS) -L./ -Wl,-rpath,./ -lnanomsg -lzlog -lpthread -ldl -Xlinker --unresolved-symbols=ignore-in-shared-libs
	#将拷贝过来的nanomsg动态库删除
	rm libnanomsg.so*
	#将拷贝过来的zlog动态库删除
	rm libzlog.so*
	#删除临时文件
	rm *.o
	rm */*.o
	rm */*/*.o
	mv $(DLL) $(BIN_PATH_CUR)

%.o:%.cpp	
	$(CC) $(CFLAGS) -c  -o $@  $<
%.o:%.c
	$(CC) $(CFLAGS) -c  -o $@  $<

clean:
	rm -f *.o
	rm -f */*.o
	rm -f */*/*.o
	rm -f $(SRC_DLL)/$(DLL)
	rm -f obj/*
	rm -f $(BIN_PATH)/$(DLL)

```