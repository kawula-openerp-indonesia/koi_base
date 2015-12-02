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
{
    'name': 'Base Identitas',
    'version': '1.1',
    'author': 'Kawula OpenERP Indonesia',
    'category': 'Base',
    'description': """
    -
    """,
    'website': 'https://github.com/kawula-openerp-indonesia',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data_Jenis_Kelamin.xml',
        'data/data_Status_Perkawinan.xml',
        'data/data_Agama.xml',
        'data/data_GolonganDarah.xml',
        'view/view_Agama.xml',
        'view/view_StatusPekerjaan.xml',
        'view/view_JenisKelamin.xml',
        'view/view_StatusPernikahan.xml',
        'view/view_Etnis.xml',
        'view/view_GolonganDarah.xml',
        'window_action/waction_Etnis.xml',
        'window_action/waction_GolonganDarah.xml',
        'window_action/waction_StatusPekerjaan.xml',
        'window_action/waction_Agama.xml',
        'window_action/waction_JenisKelamin.xml',
        'window_action/waction_StatusPernikahan.xml',
        ],
    'installable': True,
    'auto_install': False,
}
