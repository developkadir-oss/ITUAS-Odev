import math
def calculate_navigation(lat1,lon1,lat2,lon2) :
        R = 6371000
        a = math.sin(math.radians((lat1 - lat2)/2))**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(math.radians((lon1 - lon2)/2))**2
        c = 2 * math.asin(math.sqrt(a))
        mesafe = R * c #haversine mesafe 
        y = math.sin(math.radians(lon2 - lon1)) * math.cos(math.radians(lat2))
        x = (math.cos(math.radians(lat1)) * math.sin(math.radians(lat2))) - (math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon2 - lon1)))
        m = math.atan2(y,x)
        aci = (math.degrees(m) + 360) % 360 #tam kuzeyden açı
        return mesafe , aci
if __name__ == "__main__" :
    lat1 , lat2 = 41.1054 ,41.1082
    lon1 , lon2 = 29.0238 ,29.0295
mesafe , aci =  calculate_navigation(lat1, lon1, lat2, lon2)
print("--- NAVİGASYON HESABI SONUÇLARI ---")
print(f"Başlangıç (Tekne A) : {lat1}° N, {lon1}° E")
print(f"Hedef (Waypoint B)  : {lat2}° N, {lon2}° E")
print(f"Hesaplanan Mesafe   : {mesafe:.2f} metre")
print(f"Baş Açısı (Kerteriz): {aci:.2f}°")