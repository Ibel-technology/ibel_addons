from lxml import etree

from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def get_view(self, view_id=None, view_type='form', **options):
        ret_val = super().get_view(view_id=None, view_type='form', **options)

        doc = etree.XML(ret_val["arch"])

        query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(query):
            item.attrib["class"] = "d-none"
        link = "//a"
        for item in doc.xpath(link):
            item.attrib["href"] = item.attrib["href"].replace("www.odoo.com/documentation","docs.ibel.app")

        ret_val["arch"] = etree.tostring(doc)
        return ret_val
