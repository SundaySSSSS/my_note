# SDL_L2_更好的方式显示BMP
核心代码
```C++
//加载一个BMP图片
loadedImage = SDL_LoadBMP( filename.c_str() );
//创建一个优化了的图像
optimizedImage = SDL_DisplayFormat( loadedImage );
//释放临时的图像
SDL_FreeSurface( loadedImage );
```
全代码
```C++
#include <SDL/SDL.h>
#include <string>

//窗口属性
const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;
const int SCREEN_BPP = 32;//32位颜色

SDL_Surface *load_image( std::string filename ) 
{
    //临时的空间，用于存储刚刚加载好的图像
    SDL_Surface* loadedImage = NULL;
    
    //优化后的图像，实际使用的是这个图像
    SDL_Surface* optimizedImage = NULL;
    //加载图像
    loadedImage = SDL_LoadBMP( filename.c_str() );
    //如果加载图片没有出错
    if( loadedImage != NULL )
    {
        //创建一个优化了的图像
        optimizedImage = SDL_DisplayFormat( loadedImage );
        //释放临时的图像
        SDL_FreeSurface( loadedImage );
    }
    //返回优化后的表面
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
    SDL_Surface *message = NULL;
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
    message = load_image( "../res/hello.bmp" );
    background = load_image( "../res/background.bmp" );

	//将背景图片background应用到screen上
    apply_surface( 0, 0, background, screen );

	//将message表面应用到窗口中
    apply_surface( 180, 140, message, screen );

	//更新窗口
    if( SDL_Flip( screen ) == -1 )
    {
        return 1;    
    }
    //等待2秒
    SDL_Delay( 2000 );
    //释放表面
    SDL_FreeSurface( message );
    SDL_FreeSurface( background );
    
    //退出SDL
    SDL_Quit();
    return 0;
}
```