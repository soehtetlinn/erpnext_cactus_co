import frappe
from frappe import _
from frappe.utils import fmt_money

# The public homepage (route /home, set as the site's home page by install.py).
# Text lives here so it can be edited without touching the layout in home.html.

no_cache = 1

HERO = {
	"eyebrow": _("Welcome to Cactus Co.,Ltd"),
	"title": _("Quality products, delivered across Thailand"),
	"subtitle": _("Browse our catalogue, order online and track every order and invoice in your customer account."),
}

FEATURES = [
	{"icon": "truck", "title": _("Nationwide delivery"), "text": _("Fast shipping to every province in Thailand.")},
	{"icon": "shield", "title": _("Trusted quality"), "text": _("Every product is checked before it leaves our warehouse.")},
	{"icon": "file", "title": _("Tax invoices"), "text": _("VAT invoices for every order, ready to download from your account.")},
]

FEATURED_PRODUCT_COUNT = 8


def get_context(context):
	context.no_breadcrumbs = True
	context.full_width = True
	context.title = frappe.db.get_single_value("Website Settings", "app_name") or "Cactus Co.,Ltd"
	context.hero = HERO
	context.features = FEATURES
	context.products = get_featured_products()
	context.shop_route = "/all-products"


def get_featured_products():
	if not frappe.db.exists("DocType", "Website Item"):
		return []

	items = frappe.get_all(
		"Website Item",
		filters={"published": 1},
		fields=["web_item_name", "item_code", "route", "website_image", "thumbnail", "item_group", "short_description"],
		order_by="ranking desc, modified desc",
		limit=FEATURED_PRODUCT_COUNT,
	)
	price_list = frappe.db.get_single_value("Webshop Settings", "price_list") or "Standard Selling"
	for item in items:
		item.image = item.thumbnail or item.website_image
		price = frappe.db.get_value(
			"Item Price",
			{"item_code": item.item_code, "price_list": price_list, "selling": 1},
			["price_list_rate", "currency"],
			as_dict=True,
		)
		item.price = fmt_money(price.price_list_rate, currency=price.currency) if price else None
	return items
