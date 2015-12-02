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
##############################################################################
from openerp.osv import fields, osv
from openerp.tools.translate import _


class res_currency(osv.osv):
    _name = 'res.currency'
    _inherit = 'res.currency'

    _columns = {
        'fungsi_terbilang': fields.char(
            string='Amount To Text Function',
            size=100,
            ),
        }

    def terbilang(self, cr, uid, mata_uang_id, nilai):
        obj_currency = self.pool.get('res.currency')
        currency = obj_currency.browse(cr, uid, [mata_uang_id])[0]

        if hasattr(currency, currency.fungsi_terbilang):

            try:
                f = getattr(obj_currency, currency.fungsi_terbilang, None)
            except Exception, e:
                raise osv.except_osv(_('Error !'), _('%s')%e)
            else:
                hasil = f(cr, uid, nilai)

                return hasil

    def terbilang_v2(self, cr, uid, id, localdict, context=None):
        obj_currency = self.pool.get('res.currency')

        currency = obj_currency.browse(cr, uid, [id])[0]
        eval(currency.fungsi_terbilang, localdict, mode='exec', nocopy=True)

        val = {
            'terbilang' : localdict['nw'],
            }

        return val
                
    def terbilang_indo(self, cr, uid, n):
        def terbilang_indo_child(n):
            nw = ''
            if n > 0:
                ones = ["", "Satu ","Dua ","Tiga ","Empat ", "Lima ","Enam ","Tujuh ","Delapan ","Sembilan "]
                tens = ["Sepuluh ","Sebelas ","Dua Belas ","Tiga Belas ", "Empat Belas ","Lima Belas ","Enam Belas ","Tujuh Belas ","Delapan Belas ","Sembilan Belas "]
                twenties = ["","","Dua Puluh ","Tiga Puluh ","Empat Puluh ","Lima Puluh ","Enam Puluh ","Tujuh Puluh ","Delapan Puluh ","Sembilan Puluh "]
                thousands = ["","Ribu ","Juta ", "Milyar "]

                n3 = []

                ns = str(n)

                for k in range(3, 33, 3):
                    r = ns[-k:]
                    q = len(ns) - k
                    if q < -2:
                        break
                    else:
                        if q >= 0:
                            n3.append(int(r[:3]))
                        elif q >= -1:
                            n3.append(int(r[:2]))
                        elif q >= -2:
                            n3.append(int(r[:1]))
                nw = ""

                for i, x in enumerate(n3):
                    b1 = x % 10
                    b2 = (x % 100)//10
                    b3 = (x % 1000)//100
                    if x == 0:
                        continue
                    else:
                        t = thousands[i]
                    if b2 == 0:
                        if b1 == 1:
                            nw = 'se' + t + nw
                        else:
                            nw = ones[b1] + t + nw
                    elif b2 == 1:
                        nw = tens[b1] + t + nw
                    elif b2 > 1:
                        nw = twenties[b2] + ones[b1] + t + nw
                    if b3 > 0:
                        nw = ones[b3] + "Ratus " + nw

                nw = nw.replace("seJuta", "Satu Juta")
                nw = nw.replace("seMilyar", "Satu Milyar")
                nw = nw.replace("Satu ratus", "Seratus")
                nw = nw.replace("ratus", "Ratus")

            return nw

        rupiah, sen = str(n).split(".")
        rupiah = terbilang_indo_child(rupiah)
        sen = terbilang_indo_child(sen)

        if rupiah and sen:
            terbilang = rupiah + ' Rupiah ' + ' Koma ' + sen + 'Sen'
        elif rupiah and not sen:
            terbilang = rupiah + ' Rupiah '
        else:
            terbilang = ''
        return terbilang

    def terbilang_eng(self, cr, uid, n):
        def terbilang_eng_child(n):
            nw = ''
            if n > 0:
                ones = ["", "one ","two ","three ","four ", "five ","six ","seven ","eight ","nine "]
                tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
                twenties = ["","","twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
                thousands = ["","thousand ","million ", "billion ", "trillion ","quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ","nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ","quattuordecillion ", "sexdecillion ", "septendecillion ", "octodecillion ","novemdecillion ", "vigintillion "]

                n3 = []

                ns = str(n)

                for k in range(3, 33, 3):
                    r = ns[-k:]

                    q = len(ns) - k
                    if q < -2:
                        break
                    else:
                        if q >= 0:
                            n3.append(int(r[:3]))
                        elif q >= -1:
                            n3.append(int(r[:2]))
                        elif q >= -2:
                            n3.append(int(r[:1]))
                nw = ""

                for i, x in enumerate(n3):
                    b1 = x % 10
                    b2 = (x % 100)//10
                    b3 = (x % 1000)//100
                    if x == 0:
                        continue
                    else:
                        t = thousands[i]
                    if b2 == 0:
                        if b1 == 1:
                            nw = 'se' + t + nw
                        else:
                            nw = ones[b1] + t + nw
                    elif b2 == 1:
                        nw = tens[b1] + t + nw
                    elif b2 > 1:
                        nw = twenties[b2] + ones[b1] + t + nw
                    if b3 > 0:
                        nw = ones[b3] + "hundred " + nw

            return nw

        dollars, cent = str(n).split(".")
        dollars = terbilang_eng_child(dollars)
        cent = terbilang_eng_child(cent)

        if dollars and cent:
            terbilang = dollars + ' Dollar ' + ' and ' + cent + 'Cent'
        elif dollars and not cent:
            terbilang = dollars + ' Dollar '
        else:
            terbilang = ''
        return terbilang
res_currency()
