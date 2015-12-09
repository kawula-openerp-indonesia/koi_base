# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
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
from openerp.osv import fields, osv


class document_page(osv.osv):
    _name = 'document.page'
    _inherit = ['document.page', 'base.approval_object']

    def default_state(self, cr, uid, context=None):
        if context is None:
            context = {}

        return 'draft'

    _columns = {
        'name': fields.char(
            string='Title',
            required=True,
            readonly=True,
            states={
                'draft': [
                    ('readonly', False)
                    ]
                }
            ),
        'content': fields.text(
            string='Content',
            readonly=True,
            states={
                'draft': [
                    ('readonly', False)
                    ]
                }
            ),
        'parent_id': fields.many2one(
            string='Category',
            obj='document.page',
            readonly=True,
            states={
                'draft': [
                    ('readonly', False)
                    ]
                }
            ),
        'state': fields.selection(
            string='State',
            selection=[
                ('draft', 'Draft'),
                ('confirm', 'Approval Process'),
                ('approve', 'Approved'),
                ('obsolete', 'Obsolete'),
                ],
            readonly=True,
            ),
        }

    _defaults = {
        'state': default_state,
        }

    def workflow_action_confirm(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for document in self.browse(cr, uid, ids):
            self.approval_start_approval_process(cr, uid, document.id)

            self.write(cr, uid, [document.id], {'state': 'confirm'})

        return True

    def workflow_action_approve(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for document in self.browse(cr, uid, ids):
            self.approval_approve(cr, uid, document.id)

            document = self.browse(cr, uid, [document.id])[0]

            if document.next_approval_id:
                self.approval_start_approval_process(cr, uid, document.id)
            else:
                self.write(cr, uid, [document.id], {'state': 'approve'})

        return True

    def workflow_action_reject(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for document in self.browse(cr, uid, ids):
            self.approval_reject(cr, uid, document.id)

            self.write(cr, uid, [document.id], {'state': 'draft'})

        return True

    def workflow_action_bypass(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for document in self.browse(cr, uid, ids):
            self.approval_bypass(cr, uid, document.id)

            document = self.browse(cr, uid, [document.id])[0]

            if document.next_approval_id:
                self.approval_start_approval_process(cr, uid, document.id)
            else:
                self.write(cr, uid, [document.id], {'state': 'approve'})

        return True

    def workflow_action_restart(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for document in self.browse(cr, uid, ids):
            self.approval_restart_approval(cr, uid, document.id)

            self.write(cr, uid, [document.id], {'state': 'draft'})

        return True

    def workflow_action_obsolete(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        for id in ids:
            self.write(cr, uid, [id], {'state': 'obsolete'})

        return True
document_page()
