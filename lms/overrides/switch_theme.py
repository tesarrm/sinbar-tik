import frappe

@frappe.whitelist()
def switch_theme(theme):
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    print(theme)
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    if theme in ["Dark", "Light", "Automatic", "Modern_ui_theme"]:
        frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)