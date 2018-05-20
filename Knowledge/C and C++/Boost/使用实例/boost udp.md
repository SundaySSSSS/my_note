# boost udp
1. 发送端
```C++
#include "stdafx.h"
#include <iostream>
#include <boost/array.hpp>
#include <boost/asio.hpp>
#include <boost\thread.hpp>
using boost::asio::ip::udp;
int _tmain(int argc, _TCHAR* argv[])
{
try
{


boost::asio::io_service io_service;

boost::asio::ip::address addr = boost::asio::ip::address::from_string("127.0.0.1");
udp::endpoint receiver_endpoint(addr, 10060);


udp::socket socket(io_service, udp::endpoint(udp::v4(), 10061));


// 发送一个字节给服务器，让服务器知道我们的地址
for (;;)
{
socket.send_to(boost::asio::buffer("hello world"), receiver_endpoint);
boost::thread::sleep(boost::get_system_time() + boost::posix_time::seconds(1));
}

}
catch (std::exception& e)
{
std::cerr << e.what() << std::endl;
}
return 0;
}
```

2. 接收端
```C++
static void run()
{
boost::asio::io_service io_service;
// 在本机13端口建立一个socket
udp::socket socket(io_service, udp::endpoint(udp::v4(), 10060));


for (;;)
{
boost::array<char, 1024> recv_buf;
udp::endpoint remote_endpoint;
boost::system::error_code error;
// 接收一个字符，这样就得到了远程端点(remote_endpoint)
socket.receive_from(boost::asio::buffer(recv_buf),
remote_endpoint, 0, error);


if (error && error != boost::asio::error::message_size)
throw boost::system::system_error(error);


cout << recv_buf.data() << "\n";
}
}

boost::thread th(&run);
th.join();
```