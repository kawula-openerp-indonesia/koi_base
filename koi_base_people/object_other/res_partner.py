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
from openerp.osv import fields, osv
from datetime import datetime


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def _function_age(self, cr, uid, ids, field_name, args, context=None):
        if context is None:
            context = {}

        res = {}

        for partner in self.browse(cr, uid, ids):
            res[partner.id] = {
                'age_year': 0,
                'age_month': 0,
                'age_day': 0,
                }

            if not partner.is_company and partner.birthday:
                date_birthday = datetime.strptime(partner.birthday, '%Y-%m-%d')
                date_today = datetime.today()

                if date_today.month < date_birthday.month:
                    res[partner.id]['age_year'] = date_today.year \
                        - date_birthday.year - 1
                else:
                    res[partner.id]['age_year'] = date_today.year \
                        - date_birthday.year

        return res

    _columns = {
        'birthday': fields.date(
            string='Birthday',
            ),
        'born_in': fields.char(
            string='Born In',
            size=100,
            ),
        'age_year': fields.function(
            string='Age Year',
            type='integer',
            fnct=_function_age,
            method=True,
            store=False,
            multi='age',
            ),
        'age_month': fields.function(
            string='Age Month',
            type='integer',
            fnct=_function_age,
            method=True,
            store=False,
            multi='age',
            ),
        'age_day': fields.function(
            string='Age Day',
            type='integer',
            fnct=_function_age,
            method=True,
            store=False,
            multi='age',
            ),
        'religion_id': fields.many2one(
            string='Religion',
            obj='base.agama',
            ),
        'ethnic_id': fields.many2one(
            string='Ethnic',
            obj='base.etnis',
            ),
        'marital_status_id': fields.many2one(
            string='Marital Status',
            obj='base.status_pernikahan',
            ),
        'blood_type_id': fields.many2one(
            string='Blood Type',
            obj='base.golongan_darah',
            ),
        'gender_id': fields.many2one(
            string='Gender',
            obj='base.jenis_kelamin',
            ),
        'father_id': fields.many2one(
            string='Father',
            obj='res.partner',
            domain=[
                ('is_company', '=', False),
                ('parent_id', '=', False),
                ],
            ),
        'mother_id': fields.many2one(
            string='Mother',
            obj='res.partner',
            domain=[
                ('is_company', '=', False),
                ('parent_id', '=', False),
                ],
            ),
        'spouse_id': fields.many2one(
            string='Spouse',
            obj='res.partner',
            domain=[
                ('is_company', '=', False),
                ('parent_id', '=', False),
                ],
            ),
        'children_ids': fields.one2many(
            string='Childrens',
            obj='base.partner_children',
            fields_id='partner_id',
            ),
        'other_family_ids': fields.one2many(
            string='Other Family',
            obj='base.partner_other_family',
            fields_id='partner_id',
            ),
        'work_at_id': fields.many2one(
            string='Work At',
            obj='res.partner',
            domain=[
                ('is_company', '=', True),
                ('parent_id', '=', False),
                ],
            ),
        }
res_partner()


class partner_children(osv.osv):
    _name = 'base.partner_children'
    _description = 'Children'

    def _default_sequence(self, cr, uid, context={}):
        return 5

    _columns = {
        'partner_id': fields.many2one(
            string='Partner',
            obj='res.partner',
            ),
        'children_id': fields.many2one(
            string='Children',
            obj='res.partner',
            domain=[
                ('is_company', '=', False),
                ('parent_id', '=', False),
                ],
            required=True,
            ),
        'sequence': fields.integer(
            string='Child No.',
            required=True,
            ),
        }

    _defaults = {
        'sequence': _default_sequence,
        }

partner_children()


class partner_other_family(osv.osv):
    _name = 'base.partner_other_family'
    _description = 'Other Family'

    _columns = {
        'partner_id': fields.many2one(
            string='Partner',
            obj='res.partner',
            ),
        'family_relationship_type_id': fields.many2one(
            string='Relationship Type',
            obj='base.family_relationship_type',
            required=True,
            ),
        'family_id': fields.many2one(
            string='Relative Name',
            obj='res.partner',
            required=True,
            domain=[
                ('is_company', '=', False),
                ('parent_id', '=', False),
                ],
            ),
        }

partner_other_family()
