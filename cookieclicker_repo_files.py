import os
import zipfile

# Folder structure
folder_name = 'CookieClicker'
files = {
    'index.html': '<!DOCTYPE html>\n<html>\n<head>\n<base href="./">\n<link href="style.css" rel="stylesheet">\n<script src="base64.js"></script>\n<script src="main.js"></script>\n<script src="showads.js"></script>\n</head>\n<body>\n<!-- Your HTML content here -->\n</body>\n</html>',
    'style.css': '/* Add your styles here */\nbody {\n    background-color: #f2f2f2;\n    font-family: "Merriweather", serif;\n}',
    'main.js': '// Your JS code here',
    'base64.js': '// base64.js placeholder',
    'showads.js': '// showads.js placeholder',
}
folders = ['img', 'snd']
readmes = {
    'img/README.md': '# Add images here\nPlace all .png, .jpg, or other image files here.',
    'snd/README.md': '# Add sounds here\nPlace all .mp3 or other audio files here.',
}

# Create folders and files
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
for f, content in files.items():
    with open(os.path.join(folder_name, f), 'w') as file:
        file.write(content)
for sub in folders:
    os.mkdir(os.path.join(folder_name, sub))
for f, content in readmes.items():
    with open(os.path.join(folder_name, f), 'w') as file:
        file.write(content)

# Zip it
zip_name = folder_name + '.zip'
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, fs in os.walk(folder_name):
        for f in fs:
            zipf.wr