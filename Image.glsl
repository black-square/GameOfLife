vec4 testColor(in vec2 fragCoord )
{
    // Normalized pixel coordinates (from 0 to 1)
    vec2 uv = fragCoord/iResolution.xy;
    
    // Time varying pixel color
    vec3 col = 0.5 + 0.5*cos(iTime+uv.xyx+vec3(0,2,4));   

    // Output to screen
    return vec4(col,1.0);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	//vec2 uv = (fragCoord.xy + vec2(0,1000)) / iResolution.xy/8.0;
    vec2 uv = fragCoord.xy / iResolution.xy/1.5;
    
    float val = texture(iChannel0, uv )[iFrame %2];
    fragColor = vec4(testColor(fragCoord).xyz * val, 1.0);

    //vec2 mcords = mod(fragCoord/16.0f, 2.0f);

    // Output to screen
    //fragColor = col*mcords.x*mcords.y;
}