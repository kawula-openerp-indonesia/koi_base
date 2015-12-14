##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp import SUPERUSER_ID
from openerp.tools.translate import _


class product_category(osv.osv):
    _inherit = 'product.category'
    _name = 'product.category'
    _columns = {
        'group_ids': fields.many2many(
            string='Groups Allowed',
            obj='res.groups',
            rel='rel_product_categ_2_group',
            id1='pricelist_type_id',
            id2='group_id'),
        'parent_menu_id': fields.many2one(
            string='Parent Menu',
            obj='ir.ui.menu',
            ondelete='set null'),
        'window_action_id': fields.many2one(
            string='Window Action',
            obj='ir.actions.act_window',
            ondelete='set null'),
        'menu_id': fields.many2one(
            string='Menu',
            obj='ir.ui.menu',
            ondelete='set null'),
        'sequence_product_id': fields.many2one(
            string='Product Sequence',
            obj='ir.sequence')
    }

    def button_create_menu(self, cr, uid, ids, context=None):
        for id in ids:
            if not self._check_type(cr, uid, id):
                return False

            window_action_id = self._create_window_action(cr, uid, id)

            if not window_action_id:
                return False

            if not self._create_menu(cr, uid, id, window_action_id):
                return False

            pass

        return True

    def button_delete_menu(self, cr, uid, ids, context=None):
        for id in ids:
            if not self._delete_menu(cr, uid, id):
                return False

        return True

    def _create_window_action(self, cr, uid, id):
        obj_act_window = self.pool.get('ir.actions.act_window')
        obj_data = self.pool.get('ir.model.data')
        product_category = self.browse(cr, uid, [id])[0]

        waction_id = obj_data.get_object_reference(
            cr, uid, 'koi_product_manager', 'waction_base_product')[1]

        res = {
            'name': product_category.name,
            'domain': [('categ_id', '=', product_category.id)],
            'context': {'default_categ_id': product_category.id}
        }
        window_action_id = obj_act_window.copy(
            cr, SUPERUSER_ID, waction_id, res)

        self.write(cr, uid, [id], {'window_action_id': window_action_id})

        return window_action_id

    def _create_menu(self, cr, uid, id, window_action_id):
        product_category = self.browse(cr, uid, [id])[0]
        group_ids = self.read(cr, uid, [id], ['group_ids'])[0]
        obj_menu = self.pool.get('ir.ui.menu')
        obj_data = self.pool.get('ir.model.data')

        parent_id = obj_data.get_object_reference(
            cr, uid, 'koi_product_manager', 'menu_base_productRoot')[1]

        res = {
            'name': product_category.name,
            'parent_id': parent_id,
            'action': 'ir.actions.act_window,%s' % window_action_id
        }

        if group_ids:
            res.update({'groups_id': [(6, 0, group_ids['group_ids'])]})

        menu_id = obj_menu.create(cr, SUPERUSER_ID, res)

        self.write(cr, uid, [id], {'menu_id': menu_id})

        return True

    def _delete_menu(self, cr, uid, id):
        obj_act_window = self.pool.get('ir.actions.act_window')
        obj_menu = self.pool.get('ir.ui.menu')

        product_category = self.browse(cr, uid, [id])[0]

        obj_menu.unlink(
            cr, SUPERUSER_ID, [product_category.menu_id.id])
        obj_act_window.unlink(
            cr, SUPERUSER_ID, [product_category.window_action_id.id])

        return True

    def _check_type(self, cr, uid, id):
        product_category = self.browse(cr, uid, [id])[0]

        if product_category.type == 'view':
            raise osv.except_osv(
                _('Warning'),
                _('Please change type into normal.'))
        return True
product_category()
