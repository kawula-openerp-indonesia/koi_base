# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


class wizard_base_copyAccessRight(osv.osv_memory):
    _name = 'base.copy_access_right'
    _description = 'Wizard Copy Access Right From User'

    def get_default_selected_user_id(self, cr, uid, context=None):
        if context.get('active_ids'):
            return context.get('active_ids')

        return False

    _columns = {
        'selected_user_id': fields.char(
            string='User',
            ),
        'user_id': fields.many2one(
            string='User',
            obj='res.users',
            ),
        }

    _defaults = {
        'selected_user_id': get_default_selected_user_id,
        }

    def copy_access_right(self, cr, uid, ids, context=None):
        res = []
        obj_user = self.pool.get('res.users')

        record_id = context.get('active_ids')

        wizard = self.read(cr, uid, ids[0], context=context)

        user = obj_user.browse(cr, uid, wizard['user_id'][0])

        for group in user.groups_id:
            res.append(group.id)

        for data in record_id:
            user_id = obj_user.browse(cr, uid, data)
            vals = {
                'groups_id': [(6, 0, res)],
                }

            obj_user.write(cr, uid, [user_id.id], vals, context=context)

        return {'type': 'ir.actions.act_window_close'}

wizard_base_copyAccessRight()
