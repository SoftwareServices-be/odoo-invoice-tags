# Invoice Tags (`softwareservices_invoice_tags`)

Add colour-coded **tags** to customer invoices and vendor bills in Odoo, and
filter on them — the familiar tagging experience from Contacts, CRM and Projects,
brought to `account.move`.

## Features

- **Tag invoices & bills** — assign one or more tags in the form header and
  directly in the list view (an optional, toggleable column).
- **Colour-coded** — each tag carries an Odoo colour, rendered with the standard
  `many2many_tags` widget.
- **Filter by tag** — search customer invoices and vendor bills by tag from the
  search bar.
- **Simple configuration** — maintain the tag list under
  *Accounting → Configuration → Invoice Tags*.
- **Conflict-free & upgrade-safe** — the field is namespaced
  (`softwareservices_tag_ids`) and the relation table is pinned, so tag data is
  preserved on upgrade.

## How it works

| Layer | File | Role |
|-------|------|------|
| Model `softwareservices.tag` | `models/softwareservices_tag.py` | The tag master (name, colour, active). |
| `account.move` inherit | `models/account_move.py` | Adds `softwareservices_tag_ids` (many2many). |
| Account views | `views/account_move_views.xml` | Tags on the invoice/bill form, lists and search. |
| Tag views & menu | `views/softwareservices_tag_views.xml` | Tag list/form + *Accounting / Configuration* menu. |

## Compatibility

Works on Odoo **18.0** and **19.0** (Community & Enterprise). Each Odoo series
lives on its own branch (`18.0`, `19.0`); the code is identical apart from the
manifest version. The technical name `softwareservices_invoice_tags` is kept
stable across versions.

## Installation

1. Copy `softwareservices_invoice_tags/` into your Odoo addons path
   (or install the matching branch for your Odoo version).
2. Update the apps list and install **Invoice Tags**.
3. Create tags under *Accounting → Configuration → Invoice Tags*.

## Security

| Role | Read | Create / Edit | Delete |
|------|:----:|:-------------:|:------:|
| Internal user (`base.group_user`) | ✓ | | |
| Accountant (`account.group_account_user`) | ✓ | ✓ | |
| Accounting manager (`account.group_account_manager`) | ✓ | ✓ | ✓ |

## Naming convention

Software Services modules use the `softwareservices_` prefix for module and model
technical names, keeping a unique, recognisable namespace on the Odoo Apps Store.

## License

LGPL-3. © Software Services BV — https://www.softwareservices.be
