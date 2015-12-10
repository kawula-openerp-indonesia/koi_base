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

from openerp.osv import fields, osv

IMPLEMENTATION_SELECTION = [
    ('standard', 'Standard'),
    ('no_gap', 'No gap')
]


class base_sequence_configuration(osv.osv):
    _name = 'base.sequence_configuration'
    _columns = {
        'sequence_id': fields.many2one(
            obj='ir.sequence',
            string='Sequence',
            required=True,
            ondelete='cascade'
        ),
        'sequence_main_id': fields.many2one(
            obj='ir.sequence',
            string='Main Sequence',
            required=True,
            ondelete='cascade'
        ),
        'start_date': fields.date(
            string='Start Date',
            required=True
        ),
        'end_date': fields.date(
            string='End Date',
            required=True
        ),
        'related_prefix': fields.related(
            'sequence_id',
            'prefix',
            string='Prefix',
            type='char',
            size=240,
            related='ir.sequence',
            store=True,
            readonly=False
        ),
        'related_suffix': fields.related(
            'sequence_id',
            'suffix',
            string='Suffix',
            type='char',
            size=240,
            related='ir.sequence',
            store=True,
            readonly=False
        ),
        'related_number_increment': fields.related(
            'sequence_id',
            'number_increment',
            string='Number Increment',
            type='integer',
            related='ir.sequence',
            store=True,
            readonly=False
        ),
        'related_padding': fields.related(
            'sequence_id',
            'padding',
            string='Padding',
            type='integer',
            related='ir.sequence',
            store=True,
            readonly=False
        ),
        'related_implementation': fields.related(
            'sequence_id',
            'implementation',
            string='Impelemntation',
            type='selection',
            selection=IMPLEMENTATION_SELECTION,
            size=240,
            related='ir.sequence',
            store=True,
            readonly=False
        ),
        'related_number_next': fields.related(
            'sequence_id',
            'number_next',
            string='Number Next',
            type='integer',
            related='ir.sequence',
            store=True,
            readonly=False
        ),
    }

    _sql_constraints = [
        ('main_id', 'CHECK (sequence_main_id != sequence_id)',
            'Main Sequence must be different from current !'),
    ]

base_sequence_configuration()
