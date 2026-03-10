import sys
import re

file_path = r"c:\Users\Korisnik\Desktop\OPG Dine\vinarija dine 2\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    "<title>Vinski podrum Stjepan Šolčić</title>": "<title>Vinarija Dine</title>",
    '<meta content="Vrhunski vinski podrum s tradicijom i strašću za vinarstvo." name="description">': '<meta content="Vina Dine karakteriziraju jednostavnost i izvornost. Vina nastaju u vinogradima Obitelji Sardelić u Blatu na Korčuli." name="description">',
    '<meta content="Vinski podrum Stjepan Šolčić" property="og:title">': '<meta content="Vinarija Dine" property="og:title">',
    '<meta content="Vrhunski vinski podrum s tradicijom i strašću za vinarstvo." property="og:description">': '<meta content="Vina Dine karakteriziraju jednostavnost i izvornost." property="og:description">',
    '<meta content="Vinski podrum Stjepan Šolčić" property="twitter:title">': '<meta content="Vinarija Dine" property="twitter:title">',
    '<meta content="Vrhunski vinski podrum s tradicijom i strašću za vinarstvo." property="twitter:description">': '<meta content="Vina Dine karakteriziraju jednostavnost i izvornost." property="twitter:description">',
    '<div class="home-right-text">Šolčić Bijeli Pinot</div>': '<div class="home-right-text">Dine Pošip</div>',
    '<div class="right-content"><p>Ovo je priča o podrumu Stjepan Šolčić, plod ljubavi rođen iz zajedničkog poštovanja prema umjetnosti i privlačnosti vrhunskih vina. Sve je počelo sa strašću prema kvalitetnom vinu.</p><a href="/about" class="secondary-btn w-button">O nama</a></div>': '<div class="right-content"><p>Vina Dine nastaju i rađaju se u vinogradima Obitelji Sardelić, u blizini naselja Blato na otoku Korčuli, gdje se nalaze i sami podrumi. Na tom se brežuljkastom mjestu, prije početka kolanja sokova u trsu, kaplja znoja od puno truda, neprestanog htjenja i rada, pretvara i postaje kaplja ljubavi, sreće i uspjeha. ...I kao takva dolazi na stol u vinima Dine- bez dodatnog pretvaranja ili popravljanja.</p><a href="/about" class="secondary-btn w-button">O nama</a></div>',
    '<p data-w-id="26792e5d-266f-b6d2-2b3c-548254489132" class="body-small body-gray">Sjeme vinarije Šolčić posađeno je dok je zajednička vizija puštala korijene.</p>': '<p data-w-id="26792e5d-266f-b6d2-2b3c-548254489132" class="body-small body-gray">Sjeme vinarije Dine posađeno je dok je zajednička vizija puštala korijene.</p>',
    '<p>Šolčić Graševina</p>': '<p>Dine Pošip</p>',
    '<p>Šolčić Bijeli Pinot</p>': '<p>Dine Syrah</p>',
    '<p>Šolčić Crni Pinot</p>': '<p>Dine Cetinka</p>',
    '<p>Šolčić Sauvignon Blanc</p>': '<p>Dine Plavac Mali</p>',
    '<p>Šolčić Rajnski Rizling</p>': '<p>Dine Rose</p>',
    '<p>Šolčić Muškat Žuti</p>': '<p>Dine Pošip Selekcija</p>',
    '<p>Šolčić Cabernet Sauvignon</p>': '<p>Dine Syrah Reserva</p>',
    '<p>Šolčić Merlot</p>': '<p>Dine Plavac Mali Barrique</p>',
    '<div class="collection-text"><p>Bilo da se radi o okupljanju oko stola s voljenima, istraživanju novih okusa ili jednostavnom uživanju u trenutku tihog razmišljanja, vino ima moć pretvoriti obične trenutke u izvanredne.</p><p>Vino nije samo piće već kanal za obogaćivanje iskustava i stvaranje trajnih uspomena.</p></div>': '<div class="collection-text"><p>Od svake pojedinačne sorte je napravljeno vino koje je s enološke strane blago popraćeno na putu od loze do boce pa će se u svakom vinu vrlo lako moći prepoznati sortne karakteristike, istodobno uzimajući u obzir vanjske čimbenike koji određuju smjernice tog puta, a u konačnici i samog proizvoda- vina.</p><p>Ponekad nas ova vina iznenađuju jednostavnošću, a onda nas njome i uvjere kako bi baš takva trebala i biti.</p></div>',
    '<div class="collection-btn"><p>Iza svakog gutljaja krije se istraživanje zanatstva, strasti i naslijeđa koje ulazi u svaku bocu koju proizvedemo.</p><p>Otkrijte nijanse okusa vinarije Šolčić dok obilazite naše imanje i upoznajte se s našom praksom, te posvjedočite o mukotrpnom procesu iza svake berbe.</p></div>': '<div class="collection-btn"><p>Iza svakog gutljaja krije se istraživanje zanatstva, strasti i naslijeđa koje ulazi u svaku bocu koju proizvedemo.</p><p>Otkrijte nijanse okusa vinarije Dine dok obilazite naše imanje i upoznajte se s našom praksom, te posvjedočite o mukotrpnom procesu iza svake berbe.</p></div>',
    'Vinski podrum Šolčić': 'Vinariju Dine',
    'images/65fc0184d292e9741e4883ea_review-thumb-01-p-500.jpg': 'images/european_man_1.png',
    'images/65fc0184d292e9741e4883ea_review-thumb-01.jpg': 'images/european_man_1.png',
    'images/65fc019f100eb410bcd07895_review-thumb-02-p-500.jpg': 'images/european_woman_1.png',
    'images/65fc019f100eb410bcd07895_review-thumb-02.jpg': 'images/european_woman_1.png',
    'images/65fc01fb06f822c9e0b69e87_review-thumb-03-p-500.jpg': 'images/european_man_2.png',
    'images/65fc01fb06f822c9e0b69e87_review-thumb-03.jpg': 'images/european_man_2.png',
    '@vinski_podrum_solcic': '@vinarija_dine',
    '<div class="footer-info"><p class="body-small color-light">Adresa: 124B, 34000, Biškupci</p><div class="footer-email"><p class="body-small color-light">Email:</p><a href="mailto:info@example.com" class="footer-links">info@example.com</a></div><div class="footer-email"><p class="body-small color-light">Telefon:</p><a href="tel:098724693" class="footer-links">098 724 693</a></div></div>': '<div class="footer-info"><p class="body-small color-light">Adresa: Mala Krtinja bb, 20271, Blato, Korčula</p><div class="footer-email"><p class="body-small color-light">Email:</p><a href="mailto:vinarijadine@gmail.com" class="footer-links">vinarijadine@gmail.com</a></div><div class="footer-email"><p class="body-small color-light">Telefon:</p><a href="tel:0915685519" class="footer-links">091 568 5519</a></div></div>',
    '© 2024 Vinski podrum Stjepan Šolčić.': '© 2026 Vinarija Dine.',
    'Vinski podrum Stjepan Šolčić.': 'Vinarija Dine.',
    'Vinski podrum Stjepan Šolčić': 'Vinarija Dine'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
print("done")
