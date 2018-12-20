# openmp基本用法

``` C++
#pragma omp parallel for
for (int i = 0; i < 100; +i)
{
    // Do Something
}
```

指定使用的线程数， 使用

``` C++
#pragma omp parallel for num_threads(4)
```