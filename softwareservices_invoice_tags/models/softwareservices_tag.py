from odoo import fields, models


class SoftwareservicesTag(models.Model):
    """A simple, colour-coded tag that can be attached to invoices and bills."""

    _name = "softwareservices.tag"
    _description = "Invoice Tag"
    _order = "name"

    name = fields.Char(string="Tag", required=True, translate=True)
    # Integer colour index, rendered with the standard Odoo colour picker and
    # reused by the ``many2many_tags`` widget through ``color_field``.
    color = fields.Integer(string="Colour Index")
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        (
            "name_uniq",
            "unique(name)",
            "A tag with this name already exists.",
        ),
    ]
