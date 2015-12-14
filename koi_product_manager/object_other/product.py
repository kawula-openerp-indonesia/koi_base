# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
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

from openerp.osv import osv
from openerp.tools.translate import _


class product_product(osv.osv):
    _inherit = 'product.product'
    _name = 'product.product'

    def button_generate_code(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for id in ids:
            if not self._create_sequence(cr, uid, id):
                return False

        return True

    def _create_sequence(self, cr, uid, id):
        obj_product_category = self.pool.get('product.category')
        obj_sequence = self.pool.get('ir.sequence')

        product = self.browse(cr, uid, [id])[0]

        if product.categ_id:
            category = obj_product_category.browse(
                cr, uid, product.categ_id.id)

            if not category.sequence_product_id.id:
                raise osv.except_osv(
                    _('Warning'),
                    _('Please defined product sequence in product category.'))
            else:
                sequence_id = category.sequence_product_id.id
                name = obj_sequence.next_by_id(
                    cr, uid, sequence_id)
                self.write(cr, uid, [id], {'default_code': name})
        else:
            raise osv.except_osv(
                _('Warning'),
                _('Please select product category.'))

        return True

product_product()
