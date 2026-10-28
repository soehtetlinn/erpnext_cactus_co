### Custom Theme

Brand theme for ERPNext v16: the desk (`/app`), the website, the portal and the login page.

- Crimson primary colour for buttons, links, checkboxes, focus rings and active items
- Charcoal sidebar and app dock in the desk, charcoal website footer
- Brand logo on the login page, desk, website navbar and footer, and as the favicon
- Works in light and dark mode

### Where things are

| File | What it does |
|---|---|
| `custom_theme/public/scss/_brand.scss` | The palette. Change colours here only. |
| `custom_theme/public/scss/_desk.scss` | Maps the palette onto the desk |
| `custom_theme/public/scss/_website.scss` | Maps the palette onto the website and login page |
| `custom_theme/public/images/logo.svg` | The logo. Replace it, keeping the file name. |
| `custom_theme/public/js/custom_theme_desk.bundle.js` | Shows the logo for ERPNext in the desk header |
| `custom_theme/install.py` | Sets the logo in Website Settings and Navbar Settings on install |

The `*.bundle.*` files are built by `bench build` into hashed files, so browsers load the new
version after every deploy.

### Installation

```bash
bench get-app <repo-url>
bench --site <site> install-app custom_theme
```

Installing fills in the logo fields in Website Settings and Navbar Settings that are still empty.
To point them all at the theme logo again (for example after replacing `logo.svg`):

```bash
bench --site <site> execute custom_theme.install.apply_branding --kwargs "{'force': 1}"
```

The brand name shown on the login page and in emails is **Website Settings → App Name**.

### License

mit
