vec4 testColor(in vec2 fragCoord )
{
    vec2 uv = fragCoord / iResolution.xy;
    
    vec3 col = 0.8 + 0.2 * cos(iTime + uv.xyx + vec3(0,2,4) );   

    return vec4(col, 1.0);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    const float zoom = 1.0;
    
    fragCoord.y = iResolution.y - fragCoord.y;
    
    vec2 uv = fragCoord.xy / iResolution.xy / zoom;
    
    float val = texture(iChannel0, uv).x;
    fragColor = vec4(testColor(fragCoord).xyz * val, 1.0);

    //vec2 mcords = mod(fragCoord/16.0f, 2.0f);

    // Output to screen
    //fragColor = col*mcords.x*mcords.y;
}