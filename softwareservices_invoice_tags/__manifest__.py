# -*- coding: utf-8 -*-
{
    "name": "Invoice Tags",
    "version": "18.0.1.0.0",
    "category": "Accounting/Accounting",
    "summary": "Colour-coded tags to classify customer invoices and vendor bills",
    "description": """
Invoice Tags
============

Add your own colour-coded **tags** to customer invoices and vendor bills, then
filter on them - exactly like the tags you already know from Contacts, CRM or
Projects, but on ``account.move``.

* Maintain a simple list of tags (name + colour) under
  *Accounting / Configuration*.
* Pick one or more tags on any invoice or bill, in the form **and** directly in
  the list view (toggle the optional column).
* Search and filter invoices and bills by tag.

The tag field is namespaced (``softwareservices_tag_ids``) so it never clashes
with Odoo core or other apps, and the tag data is preserved on upgrade.

No configuration required beyond creating your tags. Install and tag.
""",
    "author": "Software Services BV",
    "website": "https://www.softwareservices.be",
    "support": "info@softwareservices.be",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/softwareservices_tag_views.xml",
        "views/account_move_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
}
