vec4 colorize(in vec2 fragCoord )
{
    vec2 uv = fragCoord / iResolution.xy;
    vec3 col = 0.8 + 0.2 * cos(iTime + uv.xyx + vec3(0,2,4) );   
    return vec4(col, 1.0);
}

float drawCircle( vec2 pos, vec2 center, float radius, float eps )
{
    vec2 delta = pos - center;
    float distSquared = dot(delta, delta);
	 
    vec2 border = vec2( radius - eps, radius + eps );
    
    border *= border;
    
    return 1.0 - smoothstep(border.x, border.y, distSquared);
}

float drawUi( vec2 uiCord, float eps )
{
    float d = 0.025;
    float res = 1.0;
    
    res *= drawCircle(uiCord, vec2(1.0 - d, d), d, eps);
    res *= 1.0 - drawCircle(uiCord, vec2(1.0 - d, d), d * 0.75, eps);
    
    return res;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{  
    //Inverse of Y axis
    fragCoord.y = iResolution.y - fragCoord.y;

    //Read camera info 
    vec4 buff0 = texture(iChannel0, vec2(0,0));
    float camZoom = buff0.w;
    vec2 camPan = buff0.yz;
    
    vec2 uv = fragCoord.xy / iResolution.xy;
    uv = (uv - camPan) * camZoom;
    
    float val = texture(iChannel0, uv).x;
   
    float eps = 1.0;
    
    //Draw circle in the world's (grid) space   
    uv *= iResolution.xy;
    val *= drawCircle( uv, floor(uv) + vec2(0.5), 0.5, eps * camZoom);
    
    //UI
    vec2 uiCord = fragCoord / iResolution.x;
    float epsScreen = eps / iResolution.x;
    float uiVal = drawUi(uiCord, epsScreen);
    
    vec3 res = mix( colorize(fragCoord).xyz * val, vec3(1.0), 0.5 * uiVal );
    
    fragColor = vec4(res, 1.0); 
}