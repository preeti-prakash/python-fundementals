def unique_colors(palette1, palette2):
    if palette1 == 0 or palette2 == 0:
        return set()
        
    total_palette = palette1 | palette2
    
    unique_palette = (total_palette - palette1) | (total_palette - palette2)
    return unique_palette
    
print(unique_colors({"red", "blue"}, {"blue", "green"}))         
# Output: {"red", "green"}
 
print(unique_colors({"purple", "yellow"}, {"yellow", "pink"}))   
# Output: {'pink', 'purple'}
 
print(unique_colors({"orange", "cyan"}, {"cyan", "magenta"}))    
# Output: {'magenta', 'orange'}
