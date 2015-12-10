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
from datetime import datetime, date, timedelta
from openerp.tools.translate import _

moths_option = [
    (1, 'January'),
    (2, 'February'),
    (3, 'Maret'),
    (4, 'April'),
    (5, 'Mei'),
    (6, 'Juny'),
    (7, 'July'),
    (8, 'Agustus'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'Desember')
]


class wizard_create_base_sequence_configuration_period(osv.osv_memory):
    _name = 'base.sequence_configuration_period'
    _description = 'Wizard Create Base Sequence Configuration Per Period'

    _columns = {
        'name': fields.char('Name', size=64),
        'prefix': fields.char(
            string='Prefix',
            size=64,
            help="Prefix value of the record for the sequence"
        ),
        'suffix': fields.char(
            string='Suffix',
            size=64,
            help="Suffix value of the record for the sequence"
        ),
        'number_increment': fields.integer(
            string='Increment Number',
            required=True,
            help="The next number of the sequence "
            "will be incremented by this number"
        ),
        'padding': fields.integer(
            string='Number Padding',
            required=True,
            help="OpenERP will automatically adds some '0' "
            "on the left of the 'Next Number' "
            "to get the required padding size."
        ),
        'implementation': fields.selection(
            # TODO update the view
            string='Implementation',
            selection=[
                ('standard', 'Standard'),
                ('no_gap', 'No gap')
            ],
            required=True,
            help="Two sequence object implementations are offered: Standard "
            "and 'No gap'. The later is slower than the former "
            "but forbids any gap in the sequence "
            "(while they are possible in the former)."
        ),
        'year': fields.integer(string='Year', size=64),
        'start_month': fields.selection(
            selection=moths_option,
            string='Start Month'
        ),
        'end_month': fields.selection(
            selection=moths_option,
            string='End Month'
        ),
    }

    def get_default_name(self, cr, uid, context=None):
        sequence_name = '/'
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            sequence_name = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).name

        return 'Child ' + '- ' + sequence_name

    def get_default_number_increment(self, cr, uid, context=None):
        number_increment = 0
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            number_increment = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).number_increment

        return number_increment

    def get_default_padding(self, cr, uid, context=None):
        padding = 0
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            padding = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).padding

        return padding

    def get_default_implementation(self, cr, uid, context=None):
        implementation = []
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            implementation = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).implementation

        return implementation

    def get_default_prefix(self, cr, uid, context=None):
        prefix = ''
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            prefix = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).prefix

        return prefix

    def get_default_suffix(self, cr, uid, context=None):
        suffix = ''
        obj_ir_sequence = self.pool.get('ir.sequence')

        if context.get('active_id'):
            suffix = obj_ir_sequence.browse(
                cr, uid, context.get('active_id')).suffix

        return suffix

    def get_default_year(self, cr, uid, context=None):

        date_now = datetime.strptime(
            datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        year_now = int(str(date_now)[0:4])

        return year_now

    _defaults = {
        'name': get_default_name,
        'number_increment': get_default_number_increment,
        'prefix': get_default_prefix,
        'suffix': get_default_suffix,
        'implementation': get_default_implementation,
        'number_increment': get_default_number_increment,
        'padding': get_default_padding,
        'year': get_default_year,
        'start_month': 1,
        'end_month': 12,
    }

    def get_list_months(self, cr, uid, start_month, end_month):
        # Variable Definition
        list_months_avalaible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        val = []
        count = 0

        # Main Algorithm for searching range of months
        # depend on start_month and end_month from wizard
        for list_months in list_months_avalaible:
            if count > 0:
                val.append(list_months)
            if list_months == start_month:
                count = 1
                val.append(list_months)
            if list_months == end_month:
                count = 0

        return val

    def get_2d_months(self, month):

        bulan = {
            1: '01',
            2: '02',
            3: '03',
            4: '04',
            5: '05',
            6: '06',
            7: '07',
            8: '08',
            9: '09',
            10: '10',
            11: '11',
            12: '12'
        }

        val = bulan.get(month, False)

        if not val:
            return ''

        return val

    def get_romawi_months(self, month):

        bulan = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            11: 'XI',
            12: 'XII'
        }

        val = bulan.get(month, False)

        if not val:
            return ''

        return val

    def get_string_months(self, month):

        bulan = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        val = bulan.get(month, False)

        if not val:
            return ''

        return val

    def get_short_months(self, month):

        bulan = {
            1: 'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sept',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec'
        }

        val = bulan.get(month, False)

        if not val:
            return ''

        return val

    def interpolation(self, month):
        return {
            'auto-m': month,
            'auto-m-2d': self.get_2d_months(month),
            'auto-m-r': self.get_romawi_months(month),
            'auto-m-M': self.get_string_months(month),
            'auto-m-SM': self.get_short_months(month),
            'year': '%(year)s',
            'month': '%(month)s',
            'day': '%(day)s',
            'y': '%(y)s',
            'doy': '%(doy)s',
            'woy': '%(woy)s',
            'weekday': '%(weekday)s',
            'h24': '%(h24)s',
            'h12': '%(h12)s',
            'min': '%(min)s',
            'sec': '%(sec)s',
        }

    def _interpolate(self, s, d):
        if s:
            return s % d
        return ''

    def create_base_sequence_period(self, cr, uid, ids, data, context=None):
        # Object Declaration
        obj_base_sequence_configuration = self.pool.get(
            'base.sequence_configuration')
        obj_ir_sequence = self.pool.get('ir.sequence')

        # Variable Wizard Definition
        wizard = self.read(cr, uid, ids[0], context=context)
        record_id = data['active_id']
        name = wizard['name']
        year = wizard['year']
        prefix = wizard['prefix']
        suffix = wizard['suffix']
        number_increment = wizard['number_increment']
        padding = wizard['padding']
        # implementation = wizard['implementation']
        start_month = wizard['start_month']
        end_month = wizard['end_month']

        # Variable Definition
        line_months = self.get_list_months(
            cr, uid, start_month, end_month)

        # Validation State
        if start_month > end_month:
            raise osv.except_osv(
                _('Warning'),
                _('Start Month cannot be greater than End Month !'))

        # Main Algorithm for searching range of date
        # depend on start_month and end_month from wizard

        for months in line_months:
            new_prefix = ''
            new_suffix = ''

            if months == 11:
                start_date = date(year, months, 1)
                end_date = date(year, months, 30)
            if months == 12:
                start_date = date(year, months, 1)
                end_date = date(year, months, 31)
            if months not in [11, 12]:
                start_date = date(year, (months) % 12, 1)
                end_date = date(year, (months + 1) % 12, 1)\
                    - timedelta(1, 0, 0)

            d = self.interpolation(months)

            try:
                new_prefix = self._interpolate(prefix, d)
                new_suffix = self._interpolate(suffix, d)
            except ValueError:
                raise osv.except_osv(
                    _('Warning'),
                    _('Invalid prefix or suffix.'))

            sequence_id = obj_ir_sequence.create(cr, uid, {
                'name': "%s %s %s" % (name, months, year),
                'prefix': new_prefix,
                'suffix': new_suffix,
                'padding': padding,
                'number_increment': number_increment,
            })

            obj_base_sequence_configuration.create(cr, uid, {
                'start_date': start_date,
                'end_date': end_date,
                'sequence_id': sequence_id,
                'sequence_main_id': record_id
            })

        return {'type': 'ir.actions.act_window_close'}

wizard_create_base_sequence_configuration_period()
