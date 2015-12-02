# -*- encoding: utf-8 -*-
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
##############################################################################
from openerp.osv import fields, osv


class bulan(osv.osv):
    _name = 'base.bulan'
    _description = 'Bulan'
    _columns = {
        'name': fields.char(
            string='Bulan',
            size=100,
            required=True,
            ),
        'kode': fields.char(
            string='Kode',
            size=2,
            required=True),
        'urutan': fields.integer(
            string='Urutan',
            required=True,
            ),
        }

    def jumlah_hari(self, cr, uid, bulan_id, tahun):
        obj_bulan = self.pool.get('base.bulan')
        bulan = obj_bulan.browse(cr, uid, [bulan_id])[0]

        if bulan.urutan in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif bulan.urutan in [4, 6, 9, 11]:
            return 30
        else:
            if float(tahun) / 4.0 == float(tahun/4):
                return 29
            else:
                return 28

    def bulan_selanjutnya(self, cr, uid, bulan_id, tahun, skip):
        obj_bulan = self.pool.get('base.bulan')
        bulan = obj_bulan.browse(cr, uid, [bulan_id])[0]

        if bulan.urutan + skip > 12:
            return [12 - bulan.urutan + skip, tahun+1]
        else:
            return [bulan.urutan + skip, tahun]
            
    def cek_tanggal_valid(self, cr, uid, bulan_id, tahun, tanggal):
        obj_bulan = self.pool.get('base.bulan')

        jumlah_hari = obj_bulan.jumlah_hari(bulan_id, tahun)

        if tanggal > jumlah_hari:
            return jumlah_hari
        else:
            return tanggal
