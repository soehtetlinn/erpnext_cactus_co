### Custom Theme

Brand theme for ERPNext v16: the desk (`/app`), the website, the portal and the login page.

- Crimson primary colour for buttons, links, checkboxes, focus rings and active items
- Charcoal sidebar and app dock in the desk, charcoal website footer
- Brand logo on the login page, desk, website navbar and footer, and as the favicon
- Public homepage at `/` with featured products from the online shop (Webshop app)
- Webshop pages (`/all-products`, product pages, cart) restyled to match
- Works in light and dark mode

### Where things are

| File | What it does |
|---|---|
| `custom_theme/public/scss/_brand.scss` | The palette. Change colours here only. |
| `custom_theme/public/scss/_desk.scss` | Maps the palette onto the desk |
| `custom_theme/public/scss/_website.scss` | Maps the palette onto the website, login page, homepage and shop |
| `custom_theme/www/home.py` | Homepage text (hero, features) and the featured-product query |
| `custom_theme/www/home.html` | Homepage layout |
| `custom_theme/public/images/logo.svg` | The logo. Replace it, keeping the file name. |
| `custom_theme/public/js/custom_theme_desk.bundle.js` | Shows the logo for ERPNext in the desk header |
| `custom_theme/install.py` | Sets the brand name and logo in Website, Navbar and System Settings on install |

The `*.bundle.*` files are built by `bench build` into hashed files, so browsers load the new
version after every deploy.

### Installation

```bash
bench get-app <repo-url>
bench --site <site> install-app custom_theme
```

Install it on a site that has `erpnext`, `payments`, `webshop` and `hrms` (all on `version-16`).

Installing sets the brand name **Cactus Tree Co.,Ltd** (`BRAND_NAME` in `install.py`) as the app name
and website copyright, makes `/home` the site's home page, and points the logo fields in Website
Settings and Navbar Settings at the theme logo. Only fields still at their empty or stock values are changed. To apply them all again
(for example after replacing `logo.svg` or changing `BRAND_NAME`):

```bash
bench --site <site> execute custom_theme.install.apply_branding --kwargs "{'force': 1}"
```

### License

mit
