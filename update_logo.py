import re

file_path = r"c:\Users\Korisnik\Desktop\OPG Dine\vinarija dine 2\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

nav_logo_pattern = re.compile(r'<img src="fonts/dine-logo-white\.svg" style="height: 70px; width: 200px; margin-top: -15px;" loading="lazy" alt="Nav Logo White"[^>]*>')
match = nav_logo_pattern.search(html)

if match:
    print(f"Found match: {match.group(0)}")
    new_nav_logo = '''<style>
@media (max-width: 991px) {
  .logo-desktop { display: none !important; }
  .logo-mobile { display: block !important; }
}
@media (min-width: 992px) {
  .logo-desktop { display: block !important; }
  .logo-mobile { display: none !important; }
}
</style>
<img src="fonts/dine-logo-white-horizontal.svg" class="logo-desktop home-nav-img" style="height: 40px; width: auto; margin-top: -5px;" loading="lazy" alt="Dine Winery Logo">
<img src="fonts/dine-logo-white.svg" class="logo-mobile home-nav-img" style="height: 60px; width: auto; margin-top: -5px;" loading="lazy" alt="Dine Winery Logo">'''
    html = html.replace(match.group(0), new_nav_logo)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Replaced!")
else:
    print("Match NOT found.")

