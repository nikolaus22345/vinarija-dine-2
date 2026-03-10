import sys
import os

file_path = r"c:\Users\Korisnik\Desktop\OPG Dine\vinarija dine 2\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    'src="fonts/solcic-logo-white.svg"': 'src="fonts/dine-logo-white.svg"'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
print("done")
