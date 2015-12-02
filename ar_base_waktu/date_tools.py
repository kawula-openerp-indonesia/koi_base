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
from datetime import date


def string2date(string_tanggal):
    tanggal = int(string_tanggal[8:10])
    bulan = int(string_tanggal[5:7])
    tahun = int(string_tanggal[0:4])
    return date(tahun, bulan, tanggal)


def cari_tanggal(tanggal, skip):
    a = string2date(tanggal)
    b = a.toordinal() + skip
    c = date.fromordinal(b)
    return c.strftime('%Y-%m-%d')


def jumlah_hari(bulan, tahun):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        if float(tahun) / 4.0 == float(tahun/4):
            return 29
        else:
            return 28


def bulan_selanjutnya(bulan, tahun, skip):
    if bulan + skip > 12:
        return [12 - bulan + skip, tahun+1]
    else:
        return [bulan + skip, tahun]


def cek_tanggal_valid(bulan, tahun, tanggal):
    hari = jumlah_hari(bulan, tahun)

    if tanggal > hari:
        return hari
    else:
        return tanggal


def cari_tanggal_selanjutnya(string_tanggal, skip_tanggal, skip_bulan):
    bulan = int(string_tanggal[5:7])
    tahun = int(string_tanggal[0:4])

    bulan1, tahun1 = bulan_selanjutnya(bulan, tahun, skip_bulan)
    tanggal1 = cek_tanggal_valid(bulan1, tahun1, skip_tanggal)
    a = date(tahun1, bulan1, tanggal1)
    return a.strftime('%Y-%m-%d')
