import frappe

BRAND_NAME = "Cactus Co.,Ltd"
LOGO = "/assets/custom_theme/images/logo.svg"

# app_name ships as "Frappe" and ERPNext's installer sets it to "ERPNext": both count as unset
STOCK_APP_NAMES = (None, "", "Frappe", "ERPNext")


def after_install():
	apply_branding()


def apply_branding(force=False):
	"""Set the site's brand name and point its logo settings at the theme logo.

	Only fields still at their empty or stock values are filled, so values changed in the UI are
	kept. Pass force=True to overwrite them:
	bench --site <site> execute custom_theme.install.apply_branding --kwargs "{'force': 1}"
	"""
	website = frappe.get_single("Website Settings")
	for field in ("app_logo", "banner_image", "favicon", "splash_image", "footer_logo"):
		if force or not website.get(field):
			website.set(field, LOGO)
	# app_name is the name on the login page, browser tab and emails; copyright is the footer line
	if force or website.app_name in STOCK_APP_NAMES:
		website.app_name = BRAND_NAME
	if force or not website.copyright:
		website.copyright = BRAND_NAME
	# visitors who are not logged in get the homepage (www/home.html) instead of the login page
	if force or not website.home_page:
		website.home_page = "home"
	if not website.top_bar_items:
		website.append("top_bar_items", {"label": "Shop", "url": "/all-products"})
	website.save(ignore_permissions=True)

	navbar = frappe.get_single("Navbar Settings")
	if force or not navbar.app_logo:
		navbar.app_logo = LOGO
		navbar.save(ignore_permissions=True)

	if force or frappe.db.get_single_value("System Settings", "app_name") in STOCK_APP_NAMES:
		frappe.db.set_single_value("System Settings", "app_name", BRAND_NAME)

	frappe.db.commit()
