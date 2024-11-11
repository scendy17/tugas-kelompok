def inputan(komentar):
    masukan = int(input(komentar +'='))
    return masukan

def get_watt_lampu(watt_lampu,waktu_lampu):
    konsumsi_lampu = watt_lampu*waktu_lampu
    print('konsumsi lampu=',konsumsi_lampu)
    return konsumsi_lampu

def get_watt_kipas(watt_kipas,waktu_kipas):
    konsumsi_kipas = watt_kipas*waktu_kipas
    print('konsumsi kipas=',konsumsi_kipas)
    return konsumsi_kipas

def get_watt_tv(watt_tv,waktu_tv):
    konsumsi_tv = watt_tv*waktu_tv
    print('konsumsi tv=',konsumsi_tv)
    return konsumsi_tv

def get_total_watt(konsumsi_lampu,konsumsi_kipas,konsumsi_tv):
    total_watt = konsumsi_lampu+konsumsi_kipas+konsumsi_tv
    print('total watt=',total_watt)
    return total_watt

def get_kwh(total_watt):
    kWh=total_watt/1000
    print('total kwh=',kWh)
    return kWh

def get_harga(kWh,harga_perkwh):
    total_harga=kWh*harga_perkwh
    print('total harga=',total_harga)
    return total_harga

def get_perhari(harga):
    print('harga perhari=',harga)
    
def get_sebulan(harga,hari):
    total_bulan = harga*hari
    print(' total bulan=',total_bulan)
    return total_bulan

watt_lampu=inputan('watt lampu')
watt_kipas=inputan('watt kipas')
watt_tv=inputan('watt tv')

waktu_lampu=inputan('waktu lampu perjam')
waktu_kipas=inputan('waktu kipas perjam')
waktu_tv=inputan('waktu tv perjam')

harga_perkwh=inputan('harga perkwh')

konsumsi_lampu=get_watt_lampu(watt_lampu,waktu_lampu)
konsumsi_kipas=get_watt_kipas(watt_kipas,waktu_kipas)
konsumsi_tv=get_watt_tv(watt_tv,waktu_tv)
#watt perjam
total_watt=get_total_watt(konsumsi_lampu,konsumsi_kipas,konsumsi_tv)
#konversi wh ke kwh
kWh=get_kwh(total_watt)
harga=get_harga(kWh,harga_perkwh)
get_perhari(harga)
bulan=30
get_sebulan(harga,bulan)
