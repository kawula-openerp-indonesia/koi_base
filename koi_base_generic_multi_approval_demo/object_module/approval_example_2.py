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


class approval_example_2(osv.osv):
    _name = 'base.approval_example_2'
    _description = 'Approval Example 2'
    _inherit = ['base.approval_object']

    def default_state(self, cr, uid, context=None):
        return 'draft'

    _columns = {
        'name': fields.char(
            string='Name',
            size=100,
            required=True),
        'state': fields.selection(
            string='State',
            selection=[
                ('draft', 'Draft'),
                ('confirm', 'Approval Process'),
                ('approve', 'Ready To Process'),
                ('done', 'Done'),
                ('cancel', 'Cancel')
            ],
            readonly=True),
    }

    _defaults = {
        'state': default_state,
    }

    def workflow_action_confirm(self, cr, uid, ids, context=None):
        for example in self.browse(cr, uid, ids):
            self.approval_start_approval_process(
                cr, uid, example.id)

            self.write(cr, uid, [example.id], {'state': 'confirm'})
        return True

    def workflow_action_approve(self, cr, uid, ids, context=None):
        for example in self.browse(cr, uid, ids):
            self.approval_approve(cr, uid, example.id)

            example = self.browse(cr, uid, [example.id])[0]

            if example.next_approval_id:
                self.approval_start_approval_process(
                    cr, uid, example.id)
            else:
                self.write(cr, uid, [example.id], {'state': 'approve'})

        return True

    def workflow_action_reject(self, cr, uid, ids, context=None):
        for example in self.browse(cr, uid, ids):
            self.approval_reject(cr, uid, example.id)

            self.write(cr, uid, [example.id], {'state': 'cancel'})

        return True

    def workflow_action_bypass(self, cr, uid, ids, context=None):
        for example in self.browse(cr, uid, ids):
            self.approval_bypass(cr, uid, example.id)

            example = self.browse(cr, uid, [example.id])[0]

            if example.next_approval_id:
                self.approval_start_approval_process(
                    cr, uid, example.id)
            else:
                self.write(cr, uid, [example.id], {'state': 'approve'})

        return True

    def workflow_action_done(self, cr, uid, ids, context=None):
        for example in self.browse(cr, uid, ids):
            self.write(cr, uid, [example.id], {'state': 'done'})
        return True

approval_example_2()
