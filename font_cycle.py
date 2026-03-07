from PIL import Image, ImageDraw, ImageFont
import random
import string

# ===== CONFIGURATION =====

text = "Jacobi Glenn"          # put your name here        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

img_size = (800, 200)          # width, height
bg_color = (0, 0, 0, 0)        # transparent background (RGBA)
text_color = (255, 255, 255)   # white text
font_size = 80

# Font files
font_paths = [
    "fonts/Audiowide.ttf",
    "fonts/Righteous.ttf",
    "fonts/Bangers.ttf",
    "fonts/ShareTechMono.ttf",
    "fonts/Basic.ttf",
    "fonts/STIXTwoText-Regular.otf",
    "fonts/BebasNeue-Regular.ttf",
    "fonts/Unifont.otf",
    "fonts/Carlito.ttf",
    "fonts/CrimsonText.ttf",
    "fonts/KronaOne.ttf",
    "fonts/Limelight.ttf",
    "fonts/Lobster-Regular.ttf",
    "fonts/Outfit-Regular.ttf",
    "fonts/Pacifico-Regular.ttf",
    "fonts/PressStart2P.ttf",
    "fonts/Quantico.ttf",
    "fonts/Rajdhani.ttf",
    "C:/Windows/Fonts/arial.ttf",         
    "C:/Windows/Fonts/calibri.ttf",        
    "C:/Windows/Fonts/verdana.ttf",      
    "C:/Windows/Fonts/times.ttf",        
    "C:/Windows/Fonts/georgia.ttf",      
    "C:/Windows/Fonts/cour.ttf",          
    "C:/Windows/Fonts/consola.ttf",      
    "C:/Windows/Fonts/segoeui.ttf",        
    "C:/Windows/Fonts/tahoma.ttf",         
    "C:/Windows/Fonts/trebuc.ttf",         
    "C:/Windows/Fonts/comic.ttf",        
    "C:/Windows/Fonts/impact.ttf",        
    "C:/Windows/Fonts/cooperb.ttf",        
    "C:/Windows/Fonts/alger.ttf",         
    "C:/Windows/Fonts/broadway.ttf",      
]

# Scramble settings
scramble_duration = 0.2        # seconds of scramble between fonts
scramble_fps = 14               # frames per second for scramble
scramble_frames = int(scramble_duration * scramble_fps)

# Global GIF settings
frame_duration = 1500           # milliseconds each font is shown
loop_forever = 0                # 0 = infinite loop
# =========================

def create_text_image(font_path, text, text_color, bg_color, img_size):
    """Create an image with centered text using given font."""
    img = Image.new("RGBA", img_size, bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        print(f"Warning: Could not load font {font_path}, skipping")
        return None
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2)
    draw.text(position, text, font=font, fill=text_color)
    return img

def create_scramble_frame(seed_value=None):
    """Create a frame with random characters of same length as text."""
    if seed_value is not None:
        if isinstance(seed_value, tuple):
            seed_int = hash(seed_value) % (2**32)
            random.seed(seed_int)
        else:
            random.seed(seed_value)
    
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits + " ") 
                          for _ in range(len(text)))
    
    # Use Courier New from Windows for monospace
    mono_font = ImageFont.truetype("C:/Windows/Fonts/cour.ttf", font_size)
    
    img = Image.new("RGBA", img_size, bg_color)
    draw = ImageDraw.Draw(img)
    
    bbox = draw.textbbox((0, 0), random_chars, font=mono_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2)
    
    draw.text(position, random_chars, font=mono_font, fill=text_color)
    return img

def main():
    frames = []
    
    for i, font_path in enumerate(font_paths):
        print(f"Processing font {i+1}/{len(font_paths)}: {font_path}")
        
        font_frame = create_text_image(font_path, text, text_color, bg_color, img_size)
        if font_frame is None:
            continue
            
        frames.append(font_frame)
        
        if i < len(font_paths) - 1:
            for j in range(scramble_frames):
                scramble_frame = create_scramble_frame(seed_value=(i, j))
                frames.append(scramble_frame)
    
    if not frames:
        print("No fonts loaded successfully!")
        return
    
    durations = []
    cycle_len = 1 + scramble_frames
    for idx in range(len(frames)):
        pos_in_cycle = idx % cycle_len
        if pos_in_cycle == 0:
            durations.append(frame_duration)
        else:
            durations.append(int(1000 / scramble_fps))
    
    frames[0].save(
        "NameFontCycle.gif",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=loop_forever,
        disposal=2
    )
    print(f"GIF created: NameFontCycle.gif with {len(frames)} frames")

if __name__ == "__main__":
    main()