# SDL_L8_键盘事件
核心代码
``` C++
//如果有一个事件需要处理
if( SDL_PollEvent( &event ) )
{
    //If a key was pressed
    if( event.type == SDL_KEYDOWN )
    {
		switch( event.key.keysym.sym )
        {
            case SDLK_UP: message = upMessage; break;
            case SDLK_DOWN: message = downMessage; break;
            case SDLK_LEFT: message = leftMessage; break;
            case SDLK_RIGHT: message = rightMessage; 
		}
    }            
    //如果用户点击了窗口右上角的关闭按钮
    else if( event.type == SDL_QUIT )
    {
        //退出程序
        quit = true;
    }
}
```