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
from datetime import datetime
from openerp.tools.translate import _


class approval(osv.osv):
    _name = 'base.approval'
    _description = 'Approval'
    _order = 'sequence, id'

    STATE = [
        ('draft', 'Draft'),
        ('open', 'Waiting For Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('bypass', 'Bypass')
    ]

    def default_sequence(self, cr, uid, context={}):
        return 5

    def default_state(self, cr, uid, context={}):
        return 'draft'

    def function_allowed_user(
        self, cr, uid, ids, fields_name, args, context=None
    ):
        res = {}
        for approval in self.browse(cr, uid, ids):
            app_template_id = approval.approval_template_detail_id

            res[approval.id] = {
                'allowed_approve_user_ids': []
            }

            if app_template_id:
                user_ids = []
                user_bypass_ids = []

                user_ids = app_template_id.user_ids
                group_ids = app_template_id.group_ids
                u_bypass = app_template_id.user_bypass_ids
                g_bypass = app_template_id.group_bypass_ids

                # Find users that allowed to approve/reject
                if group_ids:
                    for user in user_ids:
                        user_ids.append(user.id)
                if group_ids:
                    for group in group_ids:
                        if group.users:
                            for user in group.users:
                                user_ids.append(user.id)
                res[approval.id]['allowed_approve_user_ids'] = user_ids

                # Find users that allowed to bypass
                if u_bypass:
                    for user in u_bypass:
                        user_bypass_ids.append(user.id)
                if g_bypass:
                    for group in g_bypass:
                        if group.users:
                            for user in group.users:
                                user_bypass_ids.append(user.id)
                res[approval.id]['allowed_bypass_user_ids'] = user_bypass_ids

        return res

    _columns = {
        'name': fields.char(
            string='Name',
            size=100,
            required=True
        ),
        'model': fields.char(
            string='Related Document Model',
            size=128,
            select=1
        ),
        'res_id': fields.integer(
            string='Related Document ID',
            select=1
        ),
        'approval_template_detail_id': fields.many2one(
            string='Approval Template Detail',
            obj='base.approval_template_detail'
        ),
        'sequence': fields.integer(
            string='Sequence',
            select=1,
            required=True,
            readonly=True
        ),
        'allowed_approve_user_ids': fields.function(
            string='Allowed Approve User',
            type='many2many',
            fnct=function_allowed_user,
            relation='res.users',
            method=True,
            store=False,
            multi='allowed_user'
        ),
        'allowed_bypass_user_ids': fields.function(
            string='Allowed Bypass User',
            type='many2many',
            fnct=function_allowed_user,
            relation='res.users',
            method=True,
            store=False,
            multi='allowed_user'
        ),
        'approve_user_id': fields.many2one(
            string='Approved By',
            obj='res.users',
            readonly=True
        ),
        'approve_time': fields.datetime(
            string='Approve Time',
            readonly=True
        ),
        'bypass': fields.boolean(
            string='Bypass',
            readonly=True
        ),
        'bypass_reason': fields.text(
            string='Bypass Reason'
        ),
        'bypass_user_id': fields.many2one(
            string='Bypass By',
            obj='res.users',
            readonly=True
        ),
        'bypass_time': fields.datetime(
            string='Bypass Time',
            readonly=True
        ),
        'state': fields.selection(
            string='State',
            selection=STATE,
            readonly=True
        )
    }

    _defaults = {
        'sequence': default_sequence,
        'state': default_state
    }

    def approve_document(self, cr, uid, id, context=None):
        if not self._allowed_to_approve(cr, uid, id):
            return False

        values = self._update_approve_field(uid)
        values['state'] = 'approved'

        self.write(cr, uid, [id], values)

        return True

    def reject_document(self, cr, uid, id, context=None):
        if not self._allowed_to_approve(cr, uid, id):
            return False

        values = self._update_approve_field(uid)
        values['state'] = 'rejected'

        self.write(cr, uid, [id], values)

        return True

    def bypass_document(self, cr, uid, id, context=None):
        if not self._allowed_to_bypass(cr, uid, id):
            return False

        values = self._update_bypass_field(uid)
        values['state'] = 'bypass'

        self.write(cr, uid, [id], values)

        return True

    def _update_approve_field(self, uid):
        now = datetime.now().strftime('%Y-%m-%d')
        res = {
            'approve_user_id': uid,
            'approve_time': now
        }

        return res

    def _update_bypass_field(self, uid):
        now = datetime.now().strftime('%Y-%m-%d')
        res = {
            'bypass': True,
            'bypass_user_id': uid,
            'bypass_time': now,
        }

        return res

    def _allowed_to_approve(self, cr, uid, id):
        allowed_user_ids = []

        approval = self.browse(cr, uid, [id])[0]

        if not approval.allowed_approve_user_ids:
            err = 'No one allowed to approve this document.'\
                'Please reconfigure approval template'
            raise osv.except_osv(_('Warning'), _(err))
            return False
        else:
            for user in approval.allowed_approve_user_ids:
                allowed_user_ids.append(user.id)

            if uid in allowed_user_ids:
                return True
            else:
                err = 'You are not allowed to approve/reject this document.'\
                    'Please contact system admin'
                raise osv.except_osv(_('Warning!'), _(err))
                return False

    def _allowed_to_bypass(self, cr, uid, id):
        allowed_user_ids = []

        approval = self.browse(cr, uid, [id])[0]

        if not approval.allowed_bypass_user_ids:
            err = 'No one allowed to bypass approval this document.'\
                'Please reconfigure approval template'
            raise osv.except_osv(_('Warning'), _(err))
            return False
        else:
            for user in approval.allowed_bypass_user_ids:
                allowed_user_ids.append(user.id)

            if uid in allowed_user_ids:
                return True
            else:
                err = 'You are not allowed to bypass approval this document.'\
                    'Please contact system admin'
                raise osv.except_osv(_('Warning!'), _(err))
                return False

approval()
