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
from openerp.tools.translate import _
from openerp import SUPERUSER_ID


class res_partner_category(osv.osv):
    _name = 'res.partner.category'
    _inherit = 'res.partner.category'

    def _default_restriction_method(self, cr, uid, context=None):
        return 'all'

    def _default_type(self, cr, uid, context=None):
        return 'normal'

    _columns = {
        'restriction_method': fields.selection(
            string='Restriction Method',
            selection=[
                ('all', 'Allow All'),
                ('allow', 'Allow List'),
                ('restrict', 'Restrict')
            ],
            required=True
        ),
        'group_ids': fields.many2many(
            string='Groups',
            obj='res.groups',
            rel='rel_partner_cat_group',
            id1='partner_category_id',
            id2='group_id'
        ),
        'type': fields.selection(
            string='Type',
            selection=[
                ('view', 'View'),
                ('normal', 'Normal')
            ],
            required=True
        ),
        'search_view_id': fields.many2one(
            string='Search View',
            obj='ir.ui.view',
            readonly=True
        )
    }

    _defaults = {
        'restriction_method': _default_restriction_method,
        'type': _default_type
    }

    def button_create_filter(self, cr, uid, ids, context=None):
        for category in self.browse(cr, uid, ids):
            if category.search_view_id:
                return True

            search_view_id = self._create_search_view(cr, uid, category.id)

            if not search_view_id:
                raise osv.except_osv(_('Warning'), _('Error'))

            res = {
                'search_view_id': search_view_id
            }

            self.write(cr, uid, [category.id], res)

        return True

    def button_delete_filter(self, cr, uid, ids, context=None):
        obj_view = self.pool.get('ir.ui.view')

        for category in self.browse(cr, uid, ids):
            if not category.search_view_id:
                return True

            if category.type == 'view':
                criteria = [
                    ('parent_id', '=', category.id),
                    ('search_view_id', '!=', False)
                ]

                child_ids = self.search(cr, uid, criteria)

                if child_ids:
                    raise osv.except_osv(
                        _('Warning'),
                        _('Delete child search view first')
                    )

            obj_view.unlink(cr, SUPERUSER_ID, [category.search_view_id.id])

        return True

    def _create_search_view(self, cr, uid, id):
        obj_view = self.pool.get('ir.ui.view')
        obj_data = self.pool.get('ir.model.data')

        category = self.browse(cr, uid, [id])[0]

        if category.type == 'view':
            arch = """
                <data>
                    <xpath expr="//group[@name='group_1']"
                        position="after">
                        <group name="group_custom_%s" string="%s">

                        </group>
                    </xpath>
                </data>
            """ % (str(category.id), category.name)

            view_id = obj_data.get_object_reference(
                cr, uid, 'koi_partner_manager', 'search_base_partnerDirectory'
            )[1]

        elif category.type == 'normal':
            if not category.parent_id.search_view_id:
                raise osv.except_osv(
                    _('Warning'),
                    _('Create search view for parent first')
                )

            arch = """
                <data>
                    <xpath expr="//group[@name='group_custom_%s']"
                        position="inside">
                        <filter string="%s"
                            domain="[('category_id','in', [%s])]"/>
                    </xpath>
                </data>
            """ % (str(category.parent_id.id), category.name, str(category.id))

            view_id = category.parent_id.search_view_id.id

        res = {
            'name': 'Search Partner - %s' % (category.name),
            'model': 'res.partner',
            'inherit_id': view_id,
            'arch': arch
        }

        view_id = obj_view.create(cr, SUPERUSER_ID, res)

        return view_id

    def onchange_type(self, cr, uid, ids, type):
        value = {}
        domain = {}
        warning = {}

        if type == 'view':
            value.update({'parent_id': False})

        res = {
            'value': value,
            'domain': domain,
            'warning': warning
        }

        return res

res_partner_category()
