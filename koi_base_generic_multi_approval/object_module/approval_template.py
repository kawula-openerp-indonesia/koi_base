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


class approval_template(osv.osv):
    _name = 'base.approval_template'
    _description = 'Approval Template'
    _inherit = ['mail.thread']

    def default_active(self, cr, uid, context={}):
        return True

    _columns = {
        'name': fields.char(
            string='Approval Template',
            size=100,
            required=True
        ),
        'model_id': fields.many2one(
            string='Model',
            obj='ir.model',
            required=True
        ),
        'active': fields.boolean(string='Active'),
        'description': fields.text(string='Description'),
        'detail_ids': fields.one2many(
            string='Approval Detail',
            obj='base.approval_template_detail',
            fields_id='approval_id'
        ),
    }

    _defaults = {
        'active': default_active
    }

approval_template()


class approval_template_detail(osv.osv):
    _name = 'base.approval_template_detail'
    _description = 'Approval Template Detail'
    _columns = {
        'name': fields.char(
            string='Name',
            size=100,
            required=True
        ),
        'approval_id': fields.many2one(
            string='Approval Template',
            obj='base.approval_template',
            required=True,
            ondelete='restrict'
        ),
        'sequence': fields.integer(string='Sequence'),
        'user_ids': fields.many2many(
            string='Allowed User',
            obj='res.users',
            rel='rel_approval_user',
            id1='detail_approval_id',
            id2='user_id'
        ),
        'group_ids': fields.many2many(
            string='Allowed Group',
            obj='res.groups',
            rel='rel_approval_group',
            id1='detail_approval_id',
            id2='group_id'
        ),
        'allowed_bypass': fields.boolean(string='Allowed Bypass'),
        'user_bypass_ids': fields.many2many(
            string='Allowed Bypass User',
            obj='res.users',
            rel='rel_approval_user_bypass',
            id1='detail_approval_id',
            id2='user_id'
        ),
        'group_bypass_ids': fields.many2many(
            string='Allowed Bypass Group',
            obj='res.groups',
            rel='rel_approval_group_bypass',
            id1='detail_approval_id',
            id2='group_id'
        ),
    }

approval_template_detail()
