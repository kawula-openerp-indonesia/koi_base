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
    'name': 'KOI - Base Access Right Module',
    'version': '1.1',
    'author': 'Kawula OpenERP Indonesia,Andhitia Rama,Michael Viriyananda',
    'category': 'Base',
    'summary': 'Initial important addition',
    'description': """
This module represent another function of Access Right from OpenERP
Basic Module.
The customize is create a wizard to copy access right from another user.
    """,
    'website': 'http://github.com/kawula-openerp-indonesia',
    'images': [],
    'depends': ['ar_base'],
    'data': ['wizard/wizard_base_copyAccessRight.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
