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
from openerp import netsvc
from datetime import datetime


class wizard_cancel_transaction(osv.osv_memory):
    _name = 'base.wizard_cancel_transaction'
    _description = 'Wizard Cancel Transaction'

    def default_cancel_time(self, cr, uid, context=None):
        return datetime.now().strftime('%Y-%m-%d')

    def default_user_cancel_id(self, cr, uid, context=None):
        return uid

    _columns = {
        'cancel_time': fields.datetime(
            string='Cancel Time',
            readonly=True
        ),
        'user_cancel_id': fields.many2one(
            string='Cancelled By',
            obj='res.users',
            readonly=True
        ),
        'cancel_description': fields.text(
            string='Description',
            required=True
        )
    }

    _defaults = {
        'cancel_time': default_cancel_time,
        'user_cancel_id': default_user_cancel_id
    }

    def run_wizard(self, cr, uid, ids, context=None):
        wkf_service = netsvc.LocalService("workflow")

        obj_wizard = self.pool.get('base.wizard_cancel_transaction')
        record_id = context and context.get('active_id', False) or False
        record_object_id = context and context.get(
            'active_model', False) or False

        obj_object_model = self.pool.get(record_object_id)
        wizard = obj_wizard.browse(cr, uid, ids)[0]

        kriteria = [('id', '=', record_id)]
        object_model_ids = obj_object_model.search(cr, uid, kriteria)

        if object_model_ids:
            object_model = obj_object_model.browse(
                cr, uid, object_model_ids)[0]
            if object_model.state == 'done':
                obj_object_model.button_action_cancel(
                    cr, uid, record_id, context)
            else:
                wkf_service.trg_validate(
                    uid, 'pajak.faktur_pajak', record_id, 'button_cancel', cr)

        obj_object_model.write_cancel_description(
            cr, uid, record_id, wizard.cancel_description)

        return {}

wizard_cancel_transaction()
