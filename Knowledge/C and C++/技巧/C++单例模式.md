# C++单例模式
```C++
class Singleton{
    public:
        static Singleton *instance();
    private:
        Singleton();
        virtual ~Singleton();
        Singleton(const Singleton&){};
        Singleton& operator=(const Singleton&){};
    private:
        class CGarbo{
            public:
                ~CGarbo()
                {
                    if(Singleton::m_pInstance){
                        delete m_pInstance;
                    }
                }
        };
    private:
        static Singleton *m_pInstance;
        static CGarbo Garbo;
};
//Singleton.h

Singleton::CGarbo Singleton::Garbo;
Singleton* Singleton::m_pInstance = new Singleton();

Singleton::Singleton()
{
    printf("contructure funcation\n");
}

Singleton::~Singleton()
{
    printf("deconstructure funcation\n");
}

Singleton* Singleton::instance()
```

简单解释:
CGarbo是个私有的类, 利用私有的Garbo对象的析构函数来进行释放资源, 并且是线程安全的
