vec3 colorize(in vec2 uv )
{   
    //Time varying pixel color from the default shadertoy shader 
    return 0.8 + 0.2 * cos(iTime + uv.xyx + vec3(0,2,4) );
}

float drawCircle( in vec2 pos, in vec2 center, in float radius, in float eps )
{
    //Efficient circle rendering without sqrt
    vec2 delta = pos - center;
    float distSquared = dot(delta, delta);
	 
    vec2 border = vec2( radius - eps, radius + eps );
    
    border *= border;
    
    return 1.0 - smoothstep(border.x, border.y, distSquared);
}

float DrawRing( in vec2 pos, in vec2 center, in float radius, in float aspectRatio, in float eps )
{
    float res = 1.0;
    
    //We use negative values to simplify alignment to right or bottom border
    center = wrap( center, vec2(1.0, aspectRatio) );
    
    res *= drawCircle(pos, center, radius, eps);
    res *= 1.0 - drawCircle(pos, center, radius * 0.75, eps);
    
    return res;
}

float drawUi( in vec2 uiPos, in float eps, in float aspectRatio )
{
    float res = 1.0;
    
    // A OR B = 1 - (1 - A) * (1 - B)
    res *= 1.0 - DrawRing(uiPos, btnZoomInPos, btnRadius, aspectRatio, eps);
    res *= 1.0 - DrawRing(uiPos, btnZoomOutPos, btnRadius, aspectRatio, eps);
    res *= 1.0 - DrawRing(uiPos, btnResetPos, btnRadius, aspectRatio, eps);
    
    return 1.0 - res;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{  
    //Inverse of Y axis
    fragCoord.y = iResolution.y - fragCoord.y;
    
    //Following multiplications could be faster than division
    vec2 invRes = 1.0 / iResolution.xy;
    
    //Read camera info. It's the same for all texels 
    vec4 buff0 = texture(iChannel0, fragColor.xy * invRes);
    float camZoom = buff0.w;
    vec2 camPan = buff0.yz;
    
    //Camera formula. solve([xy / camZoom + camPan = screenPos], [xy])
    vec2 uv = (fragCoord.xy - camPan) * camZoom;
    float val = texture(iChannel0, uv * invRes).x;
   
    //The SDF border smoothness in screen pixels
    float eps = 1.0;
    
    //Render cell grid as a circle in the world's (grid) space   
    val *= drawCircle( uv, floor(uv) + vec2(0.5), 0.5, eps * camZoom);
    
    //Render UI in the screen space
    vec2 uiPos = fragCoord * invRes.x;
    float epsScreen = eps * invRes.x;
    float uiVal = drawUi(uiPos, epsScreen, invRes.x * iResolution.y);
    
    vec3 res = mix( colorize(fragCoord * invRes) * val, vec3(1.0), 0.5 * uiVal );
    
    fragColor = vec4(res, 1.0); 
}