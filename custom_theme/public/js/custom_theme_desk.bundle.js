// The desk header and the apps screen show each app's own logo. Show the brand logo for
// ERPNext instead, so the company's mark is what users see. Runs before the desk renders:
// desk.html defines frappe.boot ahead of app_include_js.
(() => {
	const LOGO = "/assets/custom_theme/images/logo.svg";
	for (const app of frappe.boot?.app_data || []) {
		if (app.app_name === "erpnext") {
			app.app_logo_url = LOGO;
		}
	}
})();
