# Pacote Time

import time

print( "Comecei agora...")
time.sleep(5) 
print("Terminei")
Comecei agora...
Terminei

Agora = time.localtime()
print( Agora )
print( type(Agora) )
time.struct_time(tm_year=2022, tm_mon=4, tm_mday=26, tm_hour=18, tm_min=41, tm_sec=37, tm_wday=1, tm_yday=116, tm_isdst=0)
<class 'time.struct_time'>

time.strftime( '%m/%d/%y, %H:%M:%S', Agora)
04/26/22, 18:41:37

time_texto = '26 June, 2022'
time.strptime( time_texto, '%d %B, %Y')
time.struct_time(tm_year=2022, tm_mon=6, tm_mday=26, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=177, tm_isdst=-1)
