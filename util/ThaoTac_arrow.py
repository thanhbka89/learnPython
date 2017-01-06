'''
Lam viec voi ngay gio
'''

import arrow

print(dir(arrow))

utc = arrow.utcnow()
print(utc)
utc = utc.replace(hours=-1)
print(utc)
print(utc.year)

local = utc.to('US/Pacific')
print(local.timestamp)

print(local.format())
print(local.format('YYYY-MM-DD HH:mm:ss ZZ'))
print(local.humanize())
print(local.humanize(locale='ko_kr'))
print(local.humanize(locale='vi_vn'))