import re

# Update publication/index.html
with open('publication/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire <style>...</style> block and replace with link to consolidated CSS
content = re.sub(
    r'    <title>Publications - HKUST CIVAL</title>\s*<style>.*?</style>',
    '    <title>Publications - HKUST CIVAL</title>\n    <link rel="stylesheet" href="../assets/css/style.css" />',
    content,
    flags=re.DOTALL
)

with open('publication/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated publication/index.html")
