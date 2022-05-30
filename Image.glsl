vec4 testColor(in vec2 fragCoord )
{
    vec2 uv = fragCoord / iResolution.xy;
    
    vec3 col = 0.8 + 0.2 * cos(iTime + uv.xyx + vec3(0,2,4) );   

    return vec4(col, 1.0);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 uv = fragCoord.xy / iResolution.xy;

    vec4 buff0 = texture(iChannel0, uv);

    float zoom = buff0.w;
    vec2 cam = buff0.yz;
    
    uv = (uv - cam) * zoom;
    
    float val = texture(iChannel0, uv).x;
    
    fragCoord.y = iResolution.y - fragCoord.y;
    
    fragColor = vec4(testColor(fragCoord).xyz * val, 1.0);
}