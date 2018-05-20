# boost基本使用方法
```C++
#include <boost/timer.hpp>

int main()
{
	boost::timer tmr;
	cout << tmr.elapsed_max() / 36000 << "h" << endl;
	cout << tmr.elapsed() << "s" << endl;

	return 0;
}
```