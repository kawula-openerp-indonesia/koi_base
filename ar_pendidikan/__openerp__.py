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
    'name': 'Pendidikan',
    'version': '1.1',
    'author': 'Kawula OpenERP Indonesia, Andhitia Rama, Michael Viriyananda',
    'category': 'Base',
    'website': 'https://github.com/kawula-openerp-indonesia',
    'description': """
    -
    """,
    'images': [],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data_JenisJenjangPendidikan.xml',
        'data/data_JenjangPendidikan.xml',
        'view/view_JenisJenjangPendidikan.xml',
        'view/view_JenjangPendidikan.xml',
        'view/view_KategoriInstitusi.xml',
        'view/view_KepemilikanInstitusi.xml',
        'window_action/waction_Pendidikan_JenisJenjangPendidikan.xml',
        'window_action/waction_Pendidikan_JenjangPendidikan.xml',
        'window_action/waction_KategoriInstitusi.xml',
        'window_action/waction_KepemilikanInstitusi.xml',
        ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
