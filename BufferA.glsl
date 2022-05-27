#if 1
    #define WRAP_AROUND( uv, res ) \
        (ivec2( mod(vec2(uv), vec2(res)) ))
#else
     #define WRAP_AROUND( uv, res ) (uv)
#endif

#define READ_STATE( uv, gen ) \
    ( int( texelFetch(iChannel0, WRAP_AROUND(uv, iChannelResolution[0]), 0)[(gen)] + 0.5))


const ivec2[] initState = ivec2[] (
    ivec2(50,180), ivec2(51,180), ivec2(50,181), ivec2(51,181), ivec2(60,180), 
    ivec2(60,179), ivec2(60,181), ivec2(61,178), ivec2(62,177), ivec2(63,177), 
    ivec2(61,182), ivec2(62,183), ivec2(63,183), ivec2(65,182), ivec2(66,181), 
    ivec2(66,180), ivec2(66,179), ivec2(65,178), ivec2(64,180), ivec2(67,180), 
    ivec2(70,181), ivec2(70,182), ivec2(70,183), ivec2(71,181), ivec2(71,182), 
    ivec2(71,183), ivec2(72,180), ivec2(72,184), ivec2(74,180), ivec2(74,179), 
    ivec2(74,184), ivec2(74,185), ivec2(84,182), ivec2(84,183), ivec2(85,182), 
    ivec2(85,183)
);

vec4 initFromArray(in ivec2 uv)
{
    const int repeat = 200;
    ivec2 mUv = (uv + ivec2(40, 100));

    //Let's introduce some variability
    ivec2 shift = mUv / repeat;
    shift = ivec2(shift.x * shift.y, shift.x * shift.y);
    mUv = mUv % repeat + shift;

    for(int i=0; i != initState.length(); ++i)
        if( mUv == initState[i] )
            return vec4(1.0,1.0,1.0,1.0);

    return vec4(0.0, 0.0, 0.0, 1.0);
}


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    ivec2 uv = ivec2(fragCoord);
    
    if(iFrame == 0)
    {
        fragColor = initFromArray(uv);
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
     
    //Rules: https://conwaylife.com/wiki/Conway%27s_Game_of_Life 
    int newState = int(totalAliveAround == 2) * curState + int(totalAliveAround == 3);  
            
    ivec2 res;
    int newGen = (iFrame + 1) % 2;
    
    res[newGen] = newState;
    res[curGen] = curState;
    
    fragColor = vec4(res, fragColor.zw );  
}
