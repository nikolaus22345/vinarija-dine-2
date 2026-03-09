const fs = require('fs');

const htmlFile = 'index.html';
let htmlContent = fs.readFileSync(htmlFile, 'utf8');

const replacements = [
    // Desktop logo
    [`src="fonts/65fbb0b36b1a31822dc0f04e_nav-white-logo.svg"`, `src="fonts/solcic-logo-white.png" style="height: 48px; width: auto;"`],
    // Footer logo
    [`src="fonts/65fa75efb0e23020f34cc46b_footer-logo.svg"`, `src="fonts/solcic-logo-white.png" style="height: 56px; width: auto;"`]
];

for (const [key, value] of replacements) {
    htmlContent = htmlContent.split(key).join(value);
}

fs.writeFileSync(htmlFile, htmlContent, 'utf8');
console.log('Logo replaced successfully!');
