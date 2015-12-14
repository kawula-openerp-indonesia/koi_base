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


class pricelist_type(osv.osv):
    _inherit = 'product.pricelist.type'
    _name = 'product.pricelist.type'
    _columns = {
        'group_ids': fields.many2many(
            string='Groups Allowed',
            obj='res.groups',
            rel='rel_pricelist_type_2_group',
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
    }

    def button_create_menu(self, cr, uid, ids, context=None):
        for id in ids:
            window_action_id = self._create_window_action(
                cr, uid, id)

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
        pricelist_type = self.browse(cr, uid, [id])[0]

        search_view_id = obj_data.get_object_reference(
            cr, uid, 'koi_product_manager', 'search_base_pricelistType')[1]

        res = {
            'name': pricelist_type.name,
            'type': 'ir.actions.act_window',
            'domain': [('key', '=', pricelist_type.key)],
            'context': {'default_key': pricelist_type.key},
            'search_view_id': search_view_id,
            'res_model': 'product.pricelist.type',
            'view_type': 'form',
            'view_mode': 'tree,form'
        }

        window_action_id = obj_act_window.create(cr, SUPERUSER_ID, res)

        self.write(cr, uid, [id], {'window_action_id': window_action_id})

        return window_action_id

    def _create_menu(self, cr, uid, id, window_action_id):
        pricelist_type = self.browse(cr, uid, [id])[0]
        group_ids = self.read(cr, uid, [id], ['group_ids'])[0]
        obj_menu = self.pool.get('ir.ui.menu')
        obj_data = self.pool.get('ir.model.data')

        parent_id = obj_data.get_object_reference(
            cr, uid, 'koi_product_manager', 'menu_base_pricelistRoot')[1]

        res = {
            'name': pricelist_type.name,
            'parent_id': parent_id,
            'action': 'ir.actions.act_window, %s' % window_action_id
        }

        if group_ids:
            res.update({'groups_id': [(6, 0, group_ids['group_ids'])]})

        menu_id = obj_menu.create(cr, SUPERUSER_ID, res)

        self.write(cr, uid, [id], {'menu_id': menu_id})

        return True

    def _delete_menu(self, cr, uid, id):
        obj_act_window = self.pool.get('ir.actions.act_window')
        obj_menu = self.pool.get('ir.ui.menu')

        project_family = self.browse(cr, uid, [id])[0]

        obj_menu.unlink(
            cr, SUPERUSER_ID, [project_family.menu_id.id])
        obj_act_window.unlink(
            cr, SUPERUSER_ID, [project_family.window_action_id.id])

        return True
pricelist_type()
