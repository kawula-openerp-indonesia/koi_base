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


class kepemilikan_perusahaan(osv.osv):
    _name = "base.kepemilikan_perusahaan"
    _description = "Kepemilikian Perusahaan"

    _columns = {
        'name': fields.char(
            string='Kepemilikian Perusahaan',
            size=100,
            required=True,
            ),
        'kode': fields.char(
            string='Kode',
            size=30,
            ),
        'keterangan': fields.text(
            string='Keterangan',
            ),
        'active': fields.boolean(
            string='Aktif',
            ),
        }
