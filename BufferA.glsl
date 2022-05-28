vec4 initFromArray(in ivec2 uv)
{
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

    const int repeat = 200;
    ivec2 uv2 = (uv + ivec2(40, 100));

    //Let's introduce some variability
    ivec2 shift = uv2 / repeat;
    shift = ivec2(shift.x * shift.y, shift.x * shift.y);
    uv2 = uv2 % repeat + shift;

    for(int i=0; i != initState.length(); ++i)
        if( uv2 == initState[i] )
            return vec4(1.0, 1.0, 1.0, 1.0);

    return vec4(0.0, 0.0, 0.0, 1.0);
}

const ivec2 bitmapSize = ivec2(162, 162);
const uint[] bitmap = uint[] (BITMAP);

vec4 initFromBitmap(in ivec2 uv)
{
    if( uint(uv.x) >= uint(bitmapSize.x) || uint(uv.y) >= uint(bitmapSize.y) )
        return vec4(0.0, 0.0, 0.0, 1.0);
        
    int pos = uv.y * bitmapSize.x + uv.x;    
    float val = float( (bitmap[pos / 32] >> (pos % 32)) & 0x1u );
    
    return vec4(val, val, val, 1.0);
}

ivec2 rot90(in ivec2 v, in int size)
{
    return ivec2(v.y, size - v.x);
}

const ivec2[] initState = ivec2[](ACTIVE_CELLS0);

vec4 initFromArray2(in ivec2 uv)
{   
    for(int i=0; i != initState.length(); ++i)
        if( uv == initState[i] )
            return vec4(1.0, 1.0, 1.0, 1.0);

    return vec4(0.0, 0.0, 0.0, 1.0);
}

#if 0
    #define IMPL_SYMMETRICAL(uv) initFromArray2(uv)
#else
    #define IMPL_SYMMETRICAL(uv) initFromBitmap(uv)
#endif    

vec4 initFromSymmetrical(in ivec2 uv)
{
    const int w = bitmapSize.x;

    ivec2 centerShift = ivec2(iChannelResolution[0]) / 2 - bitmapSize;
    
    if( uv.x < centerShift.x || uv.y < centerShift.y )
        return vec4(0.0, 0.0, 0.0, 1.0);
        
    uv -= centerShift;

    if( uv.x < w && uv.y < w )  
        return IMPL_SYMMETRICAL(uv);
    else if( uv.y < w )
        return IMPL_SYMMETRICAL(rot90(ivec2(uv.x - (w-1), uv.y), w));
    else if( uv.x < w )
        return IMPL_SYMMETRICAL(rot90(rot90( rot90(ivec2(uv.x, uv.y - (w-1)), w), w), w));
    else
        return IMPL_SYMMETRICAL(rot90( rot90(ivec2(uv.x - (w-1), uv.y - (w-1)), w), w));
}



ivec2 wrap( in ivec2 uv, in vec3 res )
{
    #if 0
        return ivec2( mod(vec2(uv), res.xy) );
    #else
        return uv;
    #endif
}

int readState( in ivec2 uv, in int gen )
{
    return int( texelFetch(iChannel0, wrap(uv, iChannelResolution[0]), 0)[gen] + 0.5);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    const int KEY_LEFT  = 37;
    const int KEY_UP    = 38;
    const int KEY_RIGHT = 39;
    const int KEY_DOWN  = 40;
    const int KEY_SPACE = 32;

    ivec2 uv = ivec2(fragCoord);
    
    if(iFrame == 0 || texelFetch( iChannel1, ivec2(KEY_SPACE,1),0 ).x > 0.0)
    {
        //fragColor = initFromArray(uv);
        //fragColor = initFromArray2(uv);
        //fragColor = initFromBitmap(uv);
        fragColor = initFromSymmetrical(uv);
   
        return;
    }

    int curGen = iFrame % 2;   
    int curState = readState( uv, curGen );
    
    int totalAliveAround = 0;
    
    totalAliveAround += readState( uv + ivec2(-1, -1), curGen );
    totalAliveAround += readState( uv + ivec2( 0, -1), curGen );
    totalAliveAround += readState( uv + ivec2( 1, -1), curGen );
    totalAliveAround += readState( uv + ivec2(-1,  0), curGen );
    totalAliveAround += readState( uv + ivec2( 1,  0), curGen );
    totalAliveAround += readState( uv + ivec2(-1,  1), curGen );
    totalAliveAround += readState( uv + ivec2( 0,  1), curGen );
    totalAliveAround += readState( uv + ivec2( 1,  1), curGen );
     
    //Rules: https://conwaylife.com/wiki/Conway%27s_Game_of_Life 
    int newState = int(totalAliveAround == 2) * curState + int(totalAliveAround == 3);  
            
    ivec2 res;
    int newGen = (iFrame + 1) % 2;
    
    res[newGen] = newState;
    res[curGen] = curState;
    
    fragColor = vec4(res, fragColor.zw );  
}
