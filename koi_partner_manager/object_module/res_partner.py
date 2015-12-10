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


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _columns = {
        'contact_address_ids': fields.one2many(
            string='Contact',
            obj='res.partner',
            fields_id='parent_id',
            domain=[
                ('active', '=', True),
                ('type', '=', 'contact')
            ]
        ),
        'employee_address_ids': fields.one2many(
            string='Employee',
            obj='res.partner',
            fields_id='work_at_id',
            domain=[('active', '=', True)]
        ),
        'invoice_address_ids': fields.one2many(
            string='Invoice Address',
            obj='res.partner',
            fields_id='parent_id',
            domain=[
                ('active', '=', True),
                ('type', '=', 'invoice')
            ]
        ),
        'shipping_address_ids': fields.one2many(
            string='Shipping Address',
            obj='res.partner',
            fields_id='parent_id',
            domain=[
                ('active', '=', True),
                ('type', '=', 'shipping')
            ]
        ),
    }

    def button_set_customer(self, cr, uid, ids, context=None):
        for id in ids:
            self._flag_partner(cr, uid, id, True, True, False, False)

        return True

    def button_set_supplier(self, cr, uid, ids, context=None):
        for id in ids:
            self._flag_partner(cr, uid, id, False, False, True, True)

        return True

    def button_unset_customer(self, cr, uid, ids, context=None):
        for id in ids:
            self._flag_partner(cr, uid, id, True, False, False, False)

        return True

    def button_unset_supplier(self, cr, uid, ids, context=None):
        for id in ids:
            self._flag_partner(cr, uid, id, False, True, True, False)
        return True

    def _flag_partner(
        self, cr, uid, id, change_customer=False,
        customer=True, change_supplier=False, supplier=False
    ):
        partner_ids = [id]

        kriteria = [('parent_id', 'child_of', id)]

        partner_ids += self.search(cr, uid, kriteria)

        partner_dict = {}
        if change_customer:
            partner_dict['customer'] = customer
        if change_supplier:
            partner_dict['supplier'] = supplier
        self.write(cr, uid, partner_ids, partner_dict)

        return True

res_partner()
