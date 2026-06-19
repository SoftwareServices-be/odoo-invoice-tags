from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    # The relation/columns are pinned to the names Odoo derives automatically
    # from the two models, so tag data created by earlier versions of this
    # module (which used a generic ``tag_ids`` field) is preserved on upgrade.
    softwareservices_tag_ids = fields.Many2many(
        comodel_name="softwareservices.tag",
        relation="account_move_softwareservices_tag_rel",
        column1="account_move_id",
        column2="softwareservices_tag_id",
        string="Tags",
    )
