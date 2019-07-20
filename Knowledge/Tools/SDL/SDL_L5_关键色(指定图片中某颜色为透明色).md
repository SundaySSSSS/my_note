# SDL_L5_关键色(指定图片中某颜色为透明色)
带有透明通道的png不建议使用此方法
核心代码
``` C++ 
SDL_Surface *load_image( std::string filename ) 
{
    //加载的图像
    SDL_Surface* loadedImage = NULL;
    
    //优化的图像
    SDL_Surface* optimizedImage = NULL;
    
    //加载图像
    loadedImage = IMG_Load( filename.c_str() );
    
    //如果加载成功
    if( loadedImage != NULL )
    {
        //创建一个优化的图像
        optimizedImage = SDL_DisplayFormat( loadedImage );
        
        //释放一开始加载的图像
        SDL_FreeSurface( loadedImage );
		//如果图像优化成功
        if( optimizedImage != NULL )
        {
            //映射关键色
            Uint32 colorkey = SDL_MapRGB( optimizedImage->format, 0, 0xFF, 0xFF );
			//将所有颜色为（R 0, G 0xFF, B 0xFF）的像素设为透明。
            SDL_SetColorKey( optimizedImage, SDL_SRCCOLORKEY, colorkey );
        }
	//返回优化后的图像
    return optimizedImage;
}
```
全代码
``` C++
#include <SDL/SDL.h>
#include <SDL/SDL_image.h>
#include <string>

//窗口属性
const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;
const int SCREEN_BPP = 32;//32位颜色

SDL_Surface *load_image( std::string filename ) 
{
    //加载的图像
    SDL_Surface* loadedImage = NULL;
    
    //优化的图像
    SDL_Surface* optimizedImage = NULL;
    
    //加载图像
    loadedImage = IMG_Load( filename.c_str() );
    
    //如果加载成功
    if( loadedImage != NULL )
    {
        //创建一个优化的图像
        optimizedImage = SDL_DisplayFormat( loadedImage );
        
        //释放一开始加载的图像
        SDL_FreeSurface( loadedImage );
		//如果图像优化成功
        if( optimizedImage != NULL )
        {
            //映射关键色
            Uint32 colorkey = SDL_MapRGB( optimizedImage->format, 0, 0xFF, 0xFF );
			//将所有颜色为（R 0, G 0xFF, B 0xFF）的像素设为透明。
            SDL_SetColorKey( optimizedImage, SDL_SRCCOLORKEY, colorkey );
        }
    }
	//返回优化后的图像
    return optimizedImage;
}

void apply_surface( int x, int y, SDL_Surface* source, SDL_Surface* destination )
{
    //新建一个临时的矩形来保存偏移量
    SDL_Rect offset;
    
    //将传入的偏移量保存到矩形中
    offset.x = x;
    offset.y = y;
    //执行表面的Blit
    SDL_BlitSurface( source, NULL, destination, &offset );
}

int main(int argc, char* argv[])
{
    SDL_Surface *boy = NULL;
    SDL_Surface *background = NULL;
    SDL_Surface *screen = NULL;

	//初始化SDL的所有子系统
    if( SDL_Init( SDL_INIT_EVERYTHING ) == -1 )
    {
        return 1;    
    }
	//设置窗口
    screen = SDL_SetVideoMode( SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BPP, SDL_SWSURFACE );
    //如果设置窗口时出现错误
    if( screen == NULL )
    {
        return 1;    
    }
    boy = load_image( "../res/foo.jpg" );
    background = load_image( "../res/background.jpg" );

	//将背景图片background应用到screen上
    apply_surface( 0, 0, background, screen );

	//将boy表面应用到窗口中
    apply_surface( 100, 100, boy, screen );

	//更新窗口
    if( SDL_Flip( screen ) == -1 )
    {
        return 1;    
    }
    //等待2秒
    SDL_Delay( 2000 );
    //释放表面
    SDL_FreeSurface( boy );
    SDL_FreeSurface( background );
    
    //退出SDL
    SDL_Quit();
    return 0;
}
```