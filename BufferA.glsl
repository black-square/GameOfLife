#define C ivec2

#define READ_STATE( uv, gen ) \
    (int( texelFetch(iChannel0, (uv), 0)[(gen)] + 0.5))

ivec2[] initState =  ivec2[] (
    C(50,180), C(51,180), C(50,181), C(51,181), C(60,180), 
    C(60,179), C(60,181), C(61,178), C(62,177), C(63,177), 
    C(61,182), C(62,183), C(63,183), C(65,182), C(66,181), 
    C(66,180), C(66,179), C(65,178), C(64,180), C(67,180), 
    C(70,181), C(70,182), C(70,183), C(71,181), C(71,182), 
    C(71,183), C(72,180), C(72,184), C(74,180), C(74,179), 
    C(74,184), C(74,185), C(84,182), C(84,183), C(85,182), 
    C(85,183)
); 


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    ivec2 uv = ivec2(fragCoord);
    
    if(iFrame == 0)
    {
        ivec2 mUv = (uv + ivec2(40, 100)) % 200;
        for(int i=0;i != initState.length(); ++i)
            if( mUv == initState[i] )
            {
                fragColor = vec4(1.0,1.0,1.0,1.0);
                return;
            }
        
        fragColor = vec4(0.0, 0.0, 0.0, 1.0);
        return;
    }

    int curGen = iFrame % 2;   
    int curState = READ_STATE( uv, curGen );
    
    int totalAliveAround = 0;
    
    totalAliveAround += READ_STATE( uv + ivec2(-1, -1), curGen );
    totalAliveAround += READ_STATE( uv + ivec2( 0, -1), curGen );
    totalAliveAround += READ_STATE( uv + ivec2( 1, -1), curGen );
    totalAliveAround += READ_STATE( uv + ivec2(-1,  0), curGen );
    totalAliveAround += READ_STATE( uv + ivec2( 1,  0), curGen );
    totalAliveAround += READ_STATE( uv + ivec2(-1,  1), curGen );
    totalAliveAround += READ_STATE( uv + ivec2( 0,  1), curGen );
    totalAliveAround += READ_STATE( uv + ivec2( 1,  1), curGen );
     
    int newState = 0;
    
    //Rules: https://conwaylife.com/wiki/Conway%27s_Game_of_Life    
    switch( totalAliveAround )
    {
    case 2:
        newState = curState;
        break;
        
    case 3:
        newState = 1;
        break;
    }
    
    ivec2 res;
    
    int newGen = (iFrame + 1) % 2;
    
    res[newGen] = newState;
    res[curGen] = curState;
    
    fragColor = vec4(vec2(res), fragColor.zw );  
}

