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


class approval_object(osv.AbstractModel):
    _name = 'base.approval_object'
    _description = 'Approval Object'

    def function_approval(self, cr, uid, ids, fields_name, arg, context=None):
        res = {}
        obj_approval = self.pool.get('base.approval')

        for approval_object in self.browse(cr, uid, ids):
            approval_id = approval_object.id
            app_template_id = approval_object.approval_template_id

            res[approval_id] = {
                'next_approval_id': False,
                'active_approval_id': False
            }

            if not app_template_id:
                pass
            else:
                dict_approval = res[approval_id]

                kriteria_open = [
                    ('model', '=', self._name),
                    ('res_id', '=', approval_id),
                    ('state', '=', 'open')
                ]
                approval_ids = obj_approval.search(cr, uid, kriteria_open)

                if approval_ids:
                    dict_approval['active_approval_id'] = approval_ids[0]

                kriteria_draft = [
                    ('model', '=', self._name),
                    ('res_id', '=', approval_id),
                    ('state', '=', 'draft')
                ]

                approval_ids = obj_approval.search(cr, uid, kriteria_draft)

                if approval_ids:
                    dict_approval['next_approval_id'] = approval_ids[0]
        return res

    _columns = {
        'approval_template_id': fields.many2one(
            string='Approval Template',
            obj='base.approval_template',
            domain=lambda self: [
                ('model_id.model', '=', self._name)
            ]
        ),
        'approval_ids': fields.one2many(
            string='Approval',
            obj='base.approval',
            fields_id='res_id',
            domain=lambda self: [
                ('model', '=', self._name)
            ],
            auto_join=True
        ),
        'active_approval_id': fields.function(
            string='Active Approval',
            fnct=function_approval,
            type='many2one',
            relation='base.approval',
            method=True,
            store=False,
            multi='approval'
        ),
        'next_approval_id': fields.function(
            string='Next Approval',
            fnct=function_approval,
            type='many2one',
            relation='base.approval',
            method=True,
            store=False,
            multi='approval'
        ),
    }

    def copy(self, cr, uid, id, default=None, context=None):
        default = default or {}

        default['approval_ids'] = []

        return super(approval_object, self).copy(
            cr, uid, id, default, context)

    def unlink(self, cr, uid, ids, context=None):
        obj_approval = self.pool.get('base.approval')

        kriteria = [
            ('res_id', 'in', ids),
            ('model', '=', self._name)
        ]

        approval_ids = obj_approval.search(cr, uid, kriteria)

        res = super(approval_object, self).unlink(cr, uid, ids, context)

        obj_approval.unlink(cr, uid, approval_ids)

        return res

    def approval_start_approval_process(self, cr, uid, id):
        obj_approval = self.pool.get('base.approval')

        approval_object = self.browse(cr, uid, [id])[0]
        next_app_id = approval_object.next_approval_id.id

        if approval_object.next_approval_id:
            obj_approval.write(
                cr, uid, [next_app_id], {'state': 'open'}
            )

        return True

    def approval_approve(self, cr, uid, id):
        # TODO:
        obj_approval = self.pool.get('base.approval')

        approval_object = self.browse(cr, uid, [id])[0]
        active_app_id = approval_object.active_approval_id.id

        if approval_object.active_approval_id:
            obj_approval.approve_document(cr, uid, active_app_id)

        return True

    def approval_reject(self, cr, uid, id):
        # TODO:
        obj_approval = self.pool.get('base.approval')

        approval_object = self.browse(cr, uid, [id])[0]
        active_app_id = approval_object.active_approval_id.id

        if approval_object.active_approval_id:
            obj_approval.reject_document(cr, uid, active_app_id)

        return True

    def approval_bypass(self, cr, uid, id):
        # TODO:
        obj_approval = self.pool.get('base.approval')

        approval_object = self.browse(cr, uid, [id])[0]
        active_app_id = approval_object.active_approval_id.id

        if approval_object.active_approval_id:
            obj_approval.bypass_document(cr, uid, active_app_id)

        return True

    def approval_onchange_approval_template_id(
        self, cr, uid, ids, approval_template_id
    ):
        value = {'approval_ids': []}
        domain = {}
        warning = {}

        approval_list = []

        obj_approval_template = self.pool.get('base.approval_template')

        if approval_template_id:
            approval_template = obj_approval_template.browse(
                cr, uid, [approval_template_id]
            )[0]

            if approval_template.detail_ids:
                for detail in approval_template.detail_ids:
                    res_detail = {
                        'name': detail.name,
                        'model': self._name,
                        'approval_template_detail_id': detail.id
                    }
                    approval_list.append((0, 0, res_detail))

            value['approval_ids'] = approval_list

        return {'value': value, 'domain': domain, 'warning': warning}

    def approval_restart_approval(self, cr, uid, id):
        obj_approval = self.pool.get('base.approval')

        criteria = [
            ('model', '=', self._name),
            ('res_id', '=', id)
        ]

        approval_ids = obj_approval.search(cr, uid, criteria)

        if approval_ids:
            res = {
                'approve_user_id': False,
                'approve_time': False,
                'bypass': False,
                'bypass_user_id': False,
                'bypass_time': False,
                'state': 'draft'
            }

            obj_approval.write(cr, uid, approval_ids, res)

        return True

approval_object()
