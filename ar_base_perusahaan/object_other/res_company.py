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


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _columns = {
        'status_perusahaan_id': fields.many2one(
            obj='base.status_perusahaan',
            string='Status Perusahaan',
            ),
        'kepemilikan_perusahaan_id': fields.many2one(
            obj='base.kepemilikan_perusahaan',
            string='Kepemilikan Perusahaan',
            ),
        'jenis_usaha_utama_id': fields.many2one(
            obj='base.jenis_usaha_perusahaan',
            string='Jenis Usaha Utama',
            ),
        'surat_ijin_usaha': fields.char(
            string='SIUP',
            size=30,
            ),
        'npwp': fields.char(
            string='NPWP',
            size=30,
            ),
        'tanggal_pengukuhan_pkp': fields.date(
            string='Tanggal Pengukuhan PKP',
            ),
        }
