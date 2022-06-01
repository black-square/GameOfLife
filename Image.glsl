vec4 colorize(in vec2 fragCoord )
{
    vec2 uv = fragCoord / iResolution.xy;
    vec3 col = 0.8 + 0.2 * cos(iTime + uv.xyx + vec3(0,2,4) );   
    return vec4(col, 1.0);
}

float drawCircle( in vec2 pos, in vec2 center, in float radius, in float eps )
{
    vec2 delta = pos - center;
    float distSquared = dot(delta, delta);
	 
    vec2 border = vec2( radius - eps, radius + eps );
    
    border *= border;
    
    return 1.0 - smoothstep(border.x, border.y, distSquared);
}

float DrawRing( in vec2 pos, in vec2 center, in float radius, in float aspectRatio, in float eps )
{
    float res = 1.0;
    
    center = wrap( center, vec2(1.0, aspectRatio) );
    
    res *= drawCircle(pos, center, radius, eps);
    res *= 1.0 - drawCircle(pos, center, radius * 0.75, eps);
    
    return res;
}

float drawUi( in vec2 uiPos, in float eps, in float aspectRatio )
{
    float res = 1.0;
    
    res *= 1.0 - DrawRing(uiPos, btnZoomInPos, btnRadius, aspectRatio, eps);
    res *= 1.0 - DrawRing(uiPos, btnZoomOutPos, btnRadius, aspectRatio, eps);
    res *= 1.0 - DrawRing(uiPos, btnResetPos, btnRadius, aspectRatio, eps);
    
    return 1.0 - res;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{  
    //Inverse of Y axis
    fragCoord.y = iResolution.y - fragCoord.y;
    
    vec2 invRes = 1.0 / iResolution.xy;
    
    //Read camera info 
    vec4 buff0 = texture(iChannel0, fragColor.xy * invRes);
    float camZoom = buff0.w;
    vec2 camPan = buff0.yz;
    
    vec2 uv = (fragCoord.xy - camPan) * camZoom;
    float val = texture(iChannel0, uv * invRes).x;
   
    //Border smoothness in pixels
    float eps = 1.0;
    
    //Draw circle in the world's (grid) space   
    val *= drawCircle( uv, floor(uv) + vec2(0.5), 0.5, eps * camZoom);
    
    //UI
    vec2 uiPos = fragCoord * invRes.x;
    float epsScreen = eps * invRes.x;
    float uiVal = drawUi(uiPos, epsScreen, invRes.x * iResolution.y);
    
    vec3 res = mix( colorize(fragCoord).xyz * val, vec3(1.0), 0.5 * uiVal );
    
    fragColor = vec4(res, 1.0); 
}