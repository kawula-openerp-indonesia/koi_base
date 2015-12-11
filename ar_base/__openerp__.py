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
    'name': 'KOI - Base Module',
    'version': '1.1',
    'category': 'Base',
    'author': 'Kawula OpenERP Indonesia,Andhitia Rama,Michael Viriyananda',
    'summary': 'Initial important addition',
    'description': """
        This module install basic functionality that each db needed.
        Such as web_shortcut, etc.
        Also there are few fungtional addition
    """,
    'depends': [
        'base',
        'document',
        'audittrail',
        'koi_partner_manager',
        'koi_base_people',
        'base_action_rule',
        'mail',
        'ar_base_perusahaan',
        'ar_base_amount_to_text',
        'web_ckeditor4',
        'web_export_view',
        'web_m2x_options',
        'web_nocreatedb',
        'web_send_message_popup',
        'web_shortcuts',
        'mass_editing',
        'document_amazons3',
    ],
    'data': [
        'wizard/wizard_cancel_transaction.xml',
        'menu/menu_Unused.xml',
        'menu/menu_Base.xml',
        'menu/menu_Setting.xml',
        "view/installer.xml"
    ],
    'installable': True,
    'images': [],
    'license': 'AGPL-3',
}
