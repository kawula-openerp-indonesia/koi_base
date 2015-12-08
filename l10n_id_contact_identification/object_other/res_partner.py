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


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _columns = {
        'ktp': fields.char('KTP', size=30),
        'expired_ktp': fields.date('Sampai Dengan'),
        'sim': fields.char('SIM A', size=30),
        'expired_sim': fields.date('Sampai Dengan'),
        'npwp': fields.char('NPWP', size=30),
        'expired_npwp': fields.date('Sampai Dengan'),
        'simb': fields.char('SIM B', size=30),
        'expired_simb': fields.date('Sampai Dengan'),
        'simb1': fields.char('SIM B1', size=30),
        'expired_simb1': fields.date('Sampai Dengan'),
        'simb2': fields.char('SIM B2', size=30),
        'expired_simb2': fields.date('Sampai Dengan'),
        'simc': fields.char('SIM C', size=30),
        'expired_simc': fields.date('Sampai Dengan'),
        'passport': fields.char('Passport', size=30),
        'expired_passport': fields.date('Sampai Dengan'),
        'kitas': fields.char('Kitas', size=30),
        'expired_kitas': fields.date('Sampai Dengan')
    }

res_partner()
