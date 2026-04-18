from PIL import Image
import os

# Configuration
MAX_WIDTH = 400  # Maximum width for thumbnails

# Files to optimize
files_to_optimize = [
    "assets/publications/2025_DKMap.png",
    "assets/publications/2026_facade_vqa.png"
]

print("Optimizing large publication images...\n")

for image_path in files_to_optimize:
    if not os.path.exists(image_path):
        print(f"✗ File not found: {image_path}")
        continue
    
    try:
        # Get original size
        original_size = os.path.getsize(image_path)
        
        # Open and resize image
        img = Image.open(image_path)
        width, height = img.size
        
        if width > MAX_WIDTH:
            ratio = MAX_WIDTH / width
            new_width = MAX_WIDTH
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
            print(f"Resized: {width}x{height} → {new_width}x{new_height}")
        
        # Save with optimization
        img.save(image_path, 'PNG', optimize=True, compress_level=9)
        
        # Get new size
        optimized_size = os.path.getsize(image_path)
        saved = original_size - optimized_size
        
        print(f"✓ {os.path.basename(image_path)}")
        print(f"  Original: {original_size/1024:.1f}KB → Optimized: {optimized_size/1024:.1f}KB")
        print(f"  Saved: {saved/1024:.1f}KB ({(saved/original_size*100):.1f}% reduction)\n")
        
    except Exception as e:
        print(f"✗ Error processing {image_path}: {e}\n")

print("Optimization complete!")
