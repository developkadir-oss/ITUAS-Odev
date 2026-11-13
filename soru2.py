def compute_rudder_angle(current_yaw, target_heading,Kp=1.5) :
    hata = target_heading - current_yaw 
    if hata < -180 :
        gercek  = hata + 360 
    elif hata > 180 :
        gercek  = hata - 360
    else :
        gercek = hata
    dümen = gercek * Kp
    if dümen < -45 :
        dümen = -45
    elif dümen > 45 :
        dümen = 45
    return dümen 
print(compute_rudder_angle(350,10))
print(compute_rudder_angle(20,340))
print(compute_rudder_angle(5,5))
    




    