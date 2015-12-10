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
    'name': 'KOI Base - Partner Manager',
    'version': '1.1',
    'category': 'Base',
    'author': 'Kawula OpenERP Indonesia,Andhitia Rama,Michael Viriyananda',
    'website': 'https://github.com/kawula-openerp-indonesia',
    'summary': 'Centralized partner management',
    'description': """
    Partner's directory
    """,
    'depends': [
        'ar_base_identitas',
        'koi_base_admin_tools',
        'contacts'
    ],
    'data': [
        'security/data_Groups.xml',
        'security/data_GroupsMenuAccess.xml',
        'security/data_AccessRight.xml',
        'wizard/wizard_tag_partner.xml',
        'view/view_ResPartner.xml',
        'view/view_ResPartnerCategory.xml',
        'window_action/waction_CorporatePartner.xml',
        'window_action/waction_IndividualPartner.xml',
        'window_action/waction_AllContacts.xml',
        'menu/menu_PartnersDirectory.xml',
        'menu/menu_Messaging.xml'
    ],
    'installable': True,
    'images': [],
    'license': 'AGPL-3',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
