from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
output_dir = "assets/publications"
os.makedirs(output_dir, exist_ok=True)

# Define the 2026 publications that need placeholders
publications_2026 = [
    "2026_less_is_more_afar.png",
    "2026_fidelity_driven.png", 
    "2026_manyviews.png",
    "2026_davinci.png",
    "2026_dkmap.png"
]

# Create placeholder images
for filename in publications_2026:
    # Create a 1024x576 white image
    img = Image.new('RGB', (1024, 576), color='white')
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([10, 10, 1014, 566], outline='#0170B9', width=3)
    
    # Add text
    title = filename.replace('.png', '').replace('_', ' ').title()
    
    # Try to use a default font, fallback to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
        font_small = font
    
    # Draw centered text
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1024 - text_width) // 2
    y = (576 - text_height) // 2
    
    draw.text((x, y), title, fill='#0170B9', font=font)
    
    # Add subtitle
    subtitle = "Figure coming soon"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_small)
    text_width_sub = bbox_sub[2] - bbox_sub[0]
    x_sub = (1024 - text_width_sub) // 2
    y_sub = y + text_height + 20
    
    draw.text((x_sub, y_sub), subtitle, fill='#666666', font=font_small)
    
    # Save the image
    filepath = os.path.join(output_dir, filename)
    img.save(filepath, 'PNG')
    print(f"Created: {filepath}")

print("\nAll placeholder images created successfully!")
print("You can replace these with actual publication figures later.")
