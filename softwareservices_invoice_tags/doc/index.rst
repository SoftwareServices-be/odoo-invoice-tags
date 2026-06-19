============
Invoice Tags
============

Add your own colour-coded **tags** to customer invoices and vendor bills, and
filter on them - the familiar tagging experience from Contacts, CRM and Projects,
brought to ``account.move``.

Features
========

* Maintain a simple list of tags (name + colour) under
  *Accounting / Configuration / Invoice Tags*.
* Assign one or more tags to any invoice or bill, both in the form header and
  directly in the list view (an optional, toggleable column).
* Search and filter customer invoices and vendor bills by tag.
* Namespaced field (``softwareservices_tag_ids``) and model
  (``softwareservices.tag``) - no clash with Odoo core or other apps.

Configuration
=============

None beyond creating tags. Open *Accounting / Configuration / Invoice Tags*,
add the tags you need and give each a colour. The tags are then available on
every customer invoice and vendor bill.

Usage
=====

* On an invoice or bill, use the **Tags** field in the header to add tags. You
  can create a tag on the fly by typing a new name.
* In the customer-invoice and vendor-bill lists, switch on the optional **Tags**
  column to see and edit tags inline.
* Use the **Tag** field in the search bar to filter the list.

Security
========

* Every internal user can read tags (so they render on invoices they may see).
* Accountants (*Billing* users) can create and edit tags.
* Accounting managers can additionally delete tags.

Data & privacy
==============

The module stores only the tags you create and their links to your invoices,
inside your own Odoo database. No data is sent to any third party and no external
service is contacted.

Upgrade notes
=============

Earlier internal builds exposed the tag field as a generic ``tag_ids``. The
relation table is unchanged, so existing tag assignments are preserved when you
upgrade to this version; only the technical field name became
``softwareservices_tag_ids``.

Credits
=======

Author: Software Services BV (Belgium) - Odoo partner.
Support: info@softwareservices.be
