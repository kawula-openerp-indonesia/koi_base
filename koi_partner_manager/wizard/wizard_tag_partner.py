# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv


class wizard_tag_partner(osv.osv_memory):
    _name = 'base.wizard_tag_partner'
    _description = 'Wizard Tag Partner'

    def _default_detail_ids(self, cr, uid, context=None):
        obj_category = self.pool.get('res.partner.category')
        obj_partner = self.pool.get('res.partner')

        result = []

        partner = obj_partner.read(
            cr, uid, [context['active_id']], ['category_id']
        )[0]

        partner_categ_ids = partner['category_id']

        categ_ids = obj_category.search(cr, uid, [])

        if categ_ids:
            for categ_id in categ_ids:
                tag = False

                if categ_id in partner_categ_ids:
                    tag = True

                res = {
                    'category_id': categ_id,
                    'tag': tag
                }

                result.append((0, 0, res))
        return result

    _columns = {
        'detail_ids': fields.one2many(
            string='Detail',
            obj='base.detail_wizard_tag_partner',
            fields_id='wizard_id'
        )
    }

    _defaults = {
        'detail_ids': _default_detail_ids,
    }

    def button_tag(self, cr, uid, ids, context=None):
        obj_partner = self.pool.get('res.partner')

        for wizard in self.browse(cr, uid, ids):
            categ_ids = []
            if wizard.detail_ids:
                for detail in wizard.detail_ids:
                    if detail.tag:
                        categ_ids.append(detail.category_id.id)

                res = {
                    'category_id': [(6, 1, categ_ids)]
                }

                obj_partner.write(cr, uid, [context['active_id']], res)

            return True

wizard_tag_partner()


class detail_wizard_tag_partner(osv.osv_memory):
    _name = 'base.detail_wizard_tag_partner'
    _description = 'Detail Wizard Tag Partner'

    _columns = {
        'wizard_id': fields.many2one(
            string='Wizard',
            obj='base.wizard_tag_partner'
        ),
        'category_id': fields.many2one(
            string='Tag',
            obj='res.partner.category',
            required=True
        ),
        'tag': fields.boolean(string='Tag')
    }

detail_wizard_tag_partner()
