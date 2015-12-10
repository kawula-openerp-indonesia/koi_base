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
import time


class ir_sequence(osv.osv):
    _inherit = 'ir.sequence'
    _columns = {
        'base_sequence_configuration_ids': fields.one2many(
            string='Sequences',
            obj='base.sequence_configuration',
            fields_id='sequence_main_id',
        ),
    }

    def get_romawi_months(self, t):

        month = time.strftime('%m', t)

        bulan = {
            '01': 'I',
            '02': 'II',
            '03': 'III',
            '04': 'IV',
            '05': 'V',
            '06': 'VI',
            '07': 'VII',
            '08': 'VIII',
            '09': 'IX',
            '10': 'X',
            '11': 'XI',
            '12': 'XII'
        }

        val = bulan.get(month, False)

        if not val:
            return ''

        return val

    def _interpolation_dict(self):
        # Actually, the server is always in UTC.
        t = time.localtime()

        return {
            'year': time.strftime('%Y', t),
            'month': time.strftime('%m', t),
            'day': time.strftime('%d', t),
            'y': time.strftime('%y', t),
            'doy': time.strftime('%j', t),
            'woy': time.strftime('%W', t),
            'weekday': time.strftime('%w', t),
            'h24': time.strftime('%H', t),
            'h12': time.strftime('%I', t),
            'min': time.strftime('%M', t),
            'sec': time.strftime('%S', t),
            'rom': self.get_romawi_months(t)
        }

    def get_sequence_configuration(
        self, cr, uid, sequence_id_or_code, code_or_id, context=None
    ):

        obj_ir_sequence = self.pool.get('ir.sequence')

        date_now = datetime.strptime(
            datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')

        if context is None:
            context = {}
        context_date = context.get('source_date')

        if code_or_id == 'id':
            kriteria = [('id', '=', sequence_id_or_code)]
        elif code_or_id == 'code':
            kriteria = [('code', '=', sequence_id_or_code)]

        sequence_ids = obj_ir_sequence.search(cr, uid, kriteria)

        if sequence_ids:
            for sequence in obj_ir_sequence.browse(cr, uid, sequence_ids):
                configuration_ids = sequence.base_sequence_configuration_ids
                for sequence_configuration in configuration_ids:

                    start_date = datetime.strptime(
                        sequence_configuration.start_date, "%Y-%m-%d")
                    end_date = datetime.strptime(
                        sequence_configuration.end_date, "%Y-%m-%d")

                    if context_date:
                        date = datetime.strptime(context_date, "%Y-%m-%d")
                        if date >= start_date and date <= end_date:
                            return sequence_configuration.sequence_id.id

                    elif date_now >= start_date and date_now <= end_date:
                        return sequence_configuration.sequence_id.id
        return False

    def next_by_id(self, cr, uid, sequence_id, context=None):
        base_sequence_configuration_id = self.get_sequence_configuration(
            cr, uid, sequence_id, 'id', context=context)

        if base_sequence_configuration_id:
            return super(ir_sequence, self).next_by_id(
                cr, uid, base_sequence_configuration_id, context=context)

        return super(ir_sequence, self).next_by_id(
            cr, uid, sequence_id, context=context)

    def next_by_code(self, cr, uid, sequence_code, context=None):
        base_sequence_configuration_code = self.get_sequence_configuration(
            cr, uid, sequence_code, 'code', context=context)

        if base_sequence_configuration_code:
            return super(ir_sequence, self).next_by_id(
                cr, uid, base_sequence_configuration_code, context=context)

        return super(ir_sequence, self).next_by_code(
            cr, uid, sequence_code, context=context)

ir_sequence()
