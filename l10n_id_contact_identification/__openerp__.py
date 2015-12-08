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
{
    'name': 'Indonesia - Contact Personal Identification Information',
    'version': '1.1',
    'author': 'Kawula OpenERP Indonesia,Andhitia Rama,Michael Viriyananda',
    'website': 'https://github.com/kawula-openerp-indonesia',
    'category': 'Localization',
    'description': """
    """,
    'depends': ['koi_base_people'],
    'demo': [],
    'data': [
        'view/view_ResPartner.xml',
        'view/view_TipeIdentitas.xml',
        'window_action/waction_TipeIdentitas.xml'
    ],
    'installable': True,
    'images': [],
    'license': 'AGPL-3',
}
