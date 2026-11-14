class MissionFSM:
    def __init__(self):
        # Tekne göreve her zaman IDLE (Bekleme) modunda başlar
        self.state = "IDLE"

    def process_event(self, event):
        eski_durum = self.state
        yeni_durum = self.state

        # 1. Acil Durum Kuralı: DOCKING hariç herhangi bir anda KILL_SWITCH veya CRITICAL_FAIL gelirse
        if self.state != "DOCKING" and event in ("KILL_SWITCH", "CRITICAL_FAIL"):
            yeni_durum = "EMERGENCY_STOP"

        # 2. Normal Durum Geçiş Kuralları
        elif self.state == "IDLE" and event == "CMD_START":
            yeni_durum = "NAVIGATING"

        elif self.state == "NAVIGATING" and event == "OBSTACLE_NEAR":
            yeni_durum = "OBSTACLE_AVOIDANCE"

        elif self.state == "OBSTACLE_AVOIDANCE" and event == "PATH_CLEAR":
            yeni_durum = "NAVIGATING"

        elif self.state == "NAVIGATING" and event == "DESTINATION_REACHED":
            yeni_durum = "DOCKING"

        # Eğer durum değiştiyse güncelle ve log yazdır
        if yeni_durum != eski_durum:
            self.state = yeni_durum
            print(f"[STATE CHANGE] {eski_durum} -> {yeni_durum} (Sebep: {event})")


if __name__ == "__main__":
    # PDF'teki örnek olay dizisi
    olaylar = [
        "CMD_START",
        "OBSTACLE_NEAR",
        "PATH_CLEAR",
        "DESTINATION_REACHED"
    ]

    fsm = MissionFSM()
    for olay in olaylar:
        fsm.process_event(olay)