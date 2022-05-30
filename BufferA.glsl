float initFromArray(in ivec2 uv)
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
            return 1.0;

    return 0.0;
}

const ivec2[] initState = ivec2[](ACTIVE_CELLS0);

float initFromArray2(in ivec2 uv)
{   
    for(int i=0; i != initState.length(); ++i)
        if( uv == initState[i] )
            return 1.0;

    return 0.0;
}

const ivec2 bitmapSize = ivec2(162, 162);
const uint[] bitmap = uint[] (BITMAP);

float initFromBitmap(in ivec2 uv)
{
    if( uint(uv.x) >= uint(bitmapSize.x) || uint(uv.y) >= uint(bitmapSize.y) )
        return 0.0;
        
    int pos = uv.y * bitmapSize.x + uv.x;    
    float val = float( (bitmap[pos / 32] >> (pos % 32)) & 0x1u );
    
    return val;
}

const uint[] compBitmapNodes = uint[] (COMPRESSED_BITMAP_NODES);
const uint[] compBitmapIndex = uint[] (COMPRESSED_BITMAP_INDEX);

float initFromCompressedBitmap(in ivec2 uv)
{
    if( uint(uv.x) >= uint(bitmapSize.x) || uint(uv.y) >= uint(bitmapSize.y) )
        return 0.0;
        
    int pos = uv.y * bitmapSize.x + uv.x;
    int wordIdx = pos / 32;
    uint idxNode = (compBitmapIndex[wordIdx / 4] >> (wordIdx % 4) * 8) & 0xFFu;
    float val = float( (compBitmapNodes[idxNode] >> (pos % 32)) & 0x1u );
    
    return val;
}

ivec2 rot90(in ivec2 v, in int size)
{
    return ivec2(v.y, size - v.x);
}

#if 0
    #define IMPL_SYMMETRICAL(uv) initFromArray2(uv)
#elif 0
    #define IMPL_SYMMETRICAL(uv) initFromBitmap(uv)
#else
    #define IMPL_SYMMETRICAL(uv) initFromCompressedBitmap(uv)
#endif    

float initFromSymmetrical(in ivec2 uv)
{
    const int w = bitmapSize.x;

    ivec2 centerShift = ivec2(iChannelResolution[0]) / 2 - bitmapSize;
    
    if( uv.x < centerShift.x || uv.y < centerShift.y )
        return 0.0;
        
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

vec4 readState( in ivec2 uv )
{
    return texelFetch( iChannel0, wrap(uv, iChannelResolution[0]), 0);
}

float keyHit( in int key )
{
    return texelFetch( iChannel1, ivec2(key, 1), 0 ).x;
}

float keyDown( in int key )
{
    return texelFetch( iChannel1, ivec2(key, 0), 0 ).x;
}

float roundEqual( float a, float b )
{
    return step( abs(a - b), 0.5 );
}

float calcCellState(in ivec2 uv, out vec4 buff )
{
    buff = readState( uv );
    
    float curState = floor(buff.x + 0.5);
    float totalAliveAround = 0.0;
    
    totalAliveAround += readState( uv + ivec2(-1, -1) ).x;
    totalAliveAround += readState( uv + ivec2( 0, -1) ).x;
    totalAliveAround += readState( uv + ivec2( 1, -1) ).x;
    totalAliveAround += readState( uv + ivec2(-1,  0) ).x;
    totalAliveAround += readState( uv + ivec2( 1,  0) ).x;
    totalAliveAround += readState( uv + ivec2(-1,  1) ).x;
    totalAliveAround += readState( uv + ivec2( 0,  1) ).x;
    totalAliveAround += readState( uv + ivec2( 1,  1) ).x;
     
    //Rules: https://conwaylife.com/wiki/Conway%27s_Game_of_Life 
    return roundEqual(totalAliveAround, 2.0) * curState + roundEqual(totalAliveAround, 3.0);  
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    const int KEY_LEFT  = 37;
    const int KEY_UP    = 38;
    const int KEY_RIGHT = 39;
    const int KEY_DOWN  = 40;
    const int KEY_SPACE = 32;
    const int KEY_W = 87;
    const int KEY_A = 65;
    const int KEY_S = 83;
    const int KEY_D = 68;

    ivec2 uv = ivec2(fragCoord);
    
    if(iFrame == 0 || keyHit(KEY_SPACE) > 0.0)
    {
        float val = 0.0;
        //val = initFromArray(uv);
        //val = initFromArray2(uv);
        //val = initFromBitmap(uv);
        //val = initFromCompressedBitmap(uv);
        val = initFromSymmetrical(uv);
        fragColor = vec4( val, 0.0, 0.0, 1.0 );
   
        return;
    }
    
    vec4 buff;
    
    float newState = calcCellState(uv, buff);
    
    vec2 cam = buff.yz;
    float zoom = buff.w;
    zoom *= 1.0 - 0.05 * (keyDown(KEY_UP) - keyDown(KEY_DOWN));
    
    //Compensation for zooming around the center of the screen
    const vec2 zoomAround = vec2(0.5);
    cam = zoomAround - (zoomAround - cam) * buff.w / zoom;

    cam.x += (keyDown(KEY_A) - keyDown(KEY_D)) * 0.05;
    cam.y += (-keyDown(KEY_W) + keyDown(KEY_S)) * 0.05;
    
    fragColor = vec4(newState, cam, zoom );  
}
