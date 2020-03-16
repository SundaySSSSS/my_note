# FFTW使用小结
## FFTW的数据类型

FFTW 有三个版本的数据类型:double、float 和 long double,使用方法如下:
1.链接对应的库(比如 libfftw3-3、libfftw3f-3、或 ibfftw3l-3)
2.包含同样的头文件 fftw3.h
将所有以小写"fftw_"开头的名字替换为"fftwf_"(float 版本)或"fftwl_"(long double 版本)。比如将 fftw_complex 替换为 fftwf_complex,将 fftw_execute
替换为 fftwf_execute 等。
3.所有以大写"FFTW_"开头的名字不变
4.将函数参数中的 double 替换为 float 或 long double
5.最后,虽然 long double 是 C99 的标准,但你的编译器可能根本不支持该类型,或它并不能提供比 double 更高的精度。
6.fftw_malloc 考虑了数据对齐,以便使用 SIMD 指令加速,所以最好不要用 C 函数malloc 替代,而且不要将 fftw_malloc、fftw_free 和 malloc、free、 delete 等混用。
尽量使用 fftw_malloc 分配空间,而不是使用的静态数组,因为静态数组是在栈上分配的,而栈空间较小;还因为这种方式没有考虑数据对齐,不便应用SIMD 指令。

