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

import urllib2
from openerp.osv import fields, osv
from openerp import tools
import os
import base64


class ar_base_installer(osv.osv_memory):
    _name = 'ar.base.installer'
    _inherit = 'res.config.installer'
    _logo_image = None

    def _get_image(self, cr, uid, context=None):
        _url = []
        if self._logo_image:
            return self._logo_image
        try:
            im = urllib2.urlopen(_url.encode("UTF-8"))
            if im.headers.maintype != 'image':
                raise TypeError(im.headers.maintype)
        except Exception:
            path = os.path.join(
                'ar_base', 'config_pixmaps', 'module_banner.png')
            image_file = file_data = tools.file_open(path, 'rb')
            try:
                file_data = image_file.read()
                self._logo_image = base64.encodestring(file_data)
                return self._logo_image
            finally:
                image_file.close()
        else:
            self._logo_image = base64.encodestring(im.read())
            return self._logo_image

    def _get_image_fn(self, cr, uid, ids, name, args, context=None):
        image = self._get_image(cr, uid, context)
        # ok to use .fromkeys() as the image is same for all
        return dict.fromkeys(ids, image)

    _columns = {
        'link': fields.char(
            string='Original developer',
            size=128,
            readonly=True
        ),
        'config_logo': fields.function(
            fnct=_get_image_fn,
            string='Image',
            type='binary',
            method=True
        ),
    }

    _defaults = {
        'config_logo': _get_image,
        'link': 'https://opensynergy-indonesia.com',
    }

ar_base_installer()
