/* 
    Title:  Game of Life Computes Pi
    Author: Dmitrii Shesterkin

    Description:
        Demonstrates Conway’s Game of Life with a pattern that geometrically 
        computes a value related to Pi.

        "An arrangement of four breeders that produce Gosper glider guns that 
        fire at each other so as to invert each others’ streams"

        Looks best in fullscreen (press space to reset) on high-resolution 
        displays (> 1080p)

    Controls:
        [W, A, S, D, mouse drag] - camera move
        [UP, DOWN, top-right screen corner] - camera zoom
        [SPACE, botom-right screen corner] - reset

    Features:
        * Initialized with an interesting Game Of Life pattern
        * Mobile-friendly: 60FPS on 2016's Android phone (Mali-G71 MP8)
        * Implements data compression to overcome constant values limit 
          (it is especially low on mobiles)
        * Relatively efficient branchless code
        * SDF rendering of the cells

    The pattern source:
        "FIGURE 6.43: LIFE COMPUTES PI" "A pattern with population in 
        generation t equal to approximately (pi-2)t^2/720"
        from "Nathaniel Johnston and Dave Greene - "Conway’s Game of Life: 
        Mathematics and Construction" 

        https://conwaylife.com/book/periodic_circuitry
*/

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
    
    //We use negative values to simplify alignment to the right or the bottom border
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
    
    //Texture lookup by the cell center eliminates borders 
    //artifacts at the very close zoom
    vec2 cellCenter = floor(uv) + vec2(0.5);
    float val = texture(iChannel0, cellCenter * invRes).x;
   
    //The SDF border smoothness in screen pixels
    float eps = 1.0;
    
    //Render the cell as a circle in the world's (grid) space   
    val *= drawCircle( uv, cellCenter, 0.5, eps * camZoom);
    
    //Render UI in the screen space
    vec2 uiPos = fragCoord * invRes.x;
    float epsScreen = eps * invRes.x;
    float uiVal = drawUi(uiPos, epsScreen, invRes.x * iResolution.y);
    
    vec3 res = mix( colorize(fragCoord * invRes) * val, vec3(1.0), 0.5 * uiVal );
    
    fragColor = vec4(res, 1.0); 
}