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
    'name': 'KOI - Product Directory',
    'version': '1.1',
    'author': 'Kawula OpenERP Indonesia; Andhitia Rama & Michael Viriyananda',
    'category': 'Base',
    'website': 'https://github.com/kawula-openerp-indonesia',
    'summary': 'Centralized product management',
    'description': """
    Partner's directory
    """,
    'depends': ['ar_base'],
    'data': [
        'group/group_MenuAccess.xml',
        'group/group_ProductFlow.xml',
        'view/view_ProductCategory.xml',
        'view/view_PricelistType.xml',
        'view/view_Product.xml',
        'window_action/waction_PricelistType.xml',
        'window_action/waction_ProductCategory.xml',
        'window_action/waction_Product.xml',
        'menu/menu_Product.xml'
    ],
    'installable': True,
    'images': [],
    'license': 'AGPL-3',
}
