import frappe

LOGO = "/assets/custom_theme/images/logo.svg"


def after_install():
	apply_branding()


def apply_branding(force=False):
	"""Point the site's logo settings at the theme logo.

	Only empty fields are filled, so logos uploaded in the UI are kept. Pass force=True to
	overwrite them:  bench --site <site> execute custom_theme.install.apply_branding --kwargs "{'force': 1}"
	"""
	website = frappe.get_single("Website Settings")
	for field in ("app_logo", "banner_image", "favicon", "splash_image", "footer_logo"):
		if force or not website.get(field):
			website.set(field, LOGO)
	website.save(ignore_permissions=True)

	navbar = frappe.get_single("Navbar Settings")
	if force or not navbar.app_logo:
		navbar.app_logo = LOGO
		navbar.save(ignore_permissions=True)

	frappe.db.commit()
