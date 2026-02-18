import subprocess
import time
import os
import sys
import threading
import shutil
import zipfile
import config
import lang

# --- AYARLAR ---
CONFIG_DOSYASI = "config.json"
ayarlar = config.config_yukle(CONFIG_DOSYASI)
JAVA_KOMUTU = ayarlar.get("JAVA_COMMAND", "java") 
JAVA_ARGUMAN = ayarlar.get("JAVA_ARGUMENT", "")
JAR_DOSYASI = ayarlar.get("JAR_FILE", "HytaleServer.jar")
DOWNLOADER_DOSYASI = ayarlar.get("DOWNLOADER_FILE", "")
EKSTRA_ARGUMANLAR = ayarlar.get("EXTRA_ARGUMENTS", [])
GUNCELLEME_KLASORU = ayarlar.get("UPDATE_FOLDER", "")
GUNCELLEME_ZIP_ADI = ayarlar.get("UPDATE_ZIP_NAME", "")
BEKLEME_SURESI = ayarlar.get("WAIT_TIME", 10)
YENIDEN_BASLATMA_SAATI = ayarlar.get("REBOOT_TIME", 4.0)
UYARI_DAKIKALARI = ayarlar.get("WARNING_MINUTES", [])
dil = ayarlar.get("LANG", "TR").upper()
textler = lang.metinleri_yukle(dil)
# ----------------



def versiyonu_getir_mevcut():
    """Mevcut JAR dosyasının versiyonunu çeker ve temizler."""
    if not os.path.exists(JAR_DOSYASI):
        return None
        
    try:
        # Çıktı örneği: "HytaleServer v2026.01.28-87d03be09 (release)"
        cikti = subprocess.check_output(f"java -jar {JAR_DOSYASI} --version", text=True).strip()
        parcalar = cikti.split() 
        parca = parcalar[1]
        cikti = parca[1:]
        print(textler[0])
        print(cikti)
        return cikti 
        
    except Exception as e:
        print(f"{textler[1]} {e}")
        return None

def versiyonu_getir_guncel():
    """Downloader üzerinden en son versiyon bilgisini çeker."""
    if not os.path.exists(DOWNLOADER_DOSYASI):
        print(f"{textler[2]}({DOWNLOADER_DOSYASI})")
        return None

    try:
        # Çıktı örneği: "2026.02.06-aa1b071c2"
        cikti = subprocess.check_output(f'"{DOWNLOADER_DOSYASI}" -print-version', text=True, shell=True).strip()
        print(textler[3])
        print(cikti)
        return cikti
    except Exception as e:
        print(f"{textler[4]} {e}")
        return None

def guncelleme_islemi_yap():
    """Dosyayı indirir, zipten çıkarır ve yerleştirir."""
    print(f"{textler[5]}")
    
    # Klasörü oluştur (yoksa)
    if not os.path.exists(GUNCELLEME_KLASORU):
        os.makedirs(GUNCELLEME_KLASORU)
        
    zip_tam_yol = os.path.join(GUNCELLEME_KLASORU, GUNCELLEME_ZIP_ADI)
    
    # 1. İndirme Komutu
    # Not: Downloader parametre yapınızın doğruluğundan emin olun.
    komut_indir = f'{DOWNLOADER_DOSYASI} -download-path "{zip_tam_yol}"'
    subprocess.run(komut_indir, shell=True)
    
    if not os.path.exists(zip_tam_yol):
        print(f"{textler[6]}")
        return False

    print(f"{textler[7]}")
    
    try:
        # 2. Zip'i aç ve dosyaları taşı
        with zipfile.ZipFile(zip_tam_yol, 'r') as zip_ref:
            # Önce geçici klasöre hepsini çıkaralım
            zip_ref.extractall(GUNCELLEME_KLASORU)
            
        # Hedef dosyalar ve kaynakları
        kaynak_assets = os.path.join(GUNCELLEME_KLASORU, "Assets.zip")
        kaynak_jar = os.path.join(GUNCELLEME_KLASORU, "Server", "HytaleServer.jar")
        kaynak_oat = os.path.join(GUNCELLEME_KLASORU, "Server", "HytaleServer.oat")
        
        # Dosyaları ana dizine (scriptin olduğu yere) taşı
        hedef_klasor = os.getcwd() # Şu anki çalışma dizini
        
        if os.path.exists(kaynak_assets):
            shutil.move(kaynak_assets, os.path.join(hedef_klasor, "Assets.zip"))
            print(f" -> {textler[8]}")
            
        if os.path.exists(kaynak_jar):
            shutil.move(kaynak_jar, os.path.join(hedef_klasor, "HytaleServer.jar"))
            print(f" -> {textler[9]}")

        if os.path.exists(kaynak_oat):
            shutil.move(kaynak_oat, os.path.join(hedef_klasor, "HytaleServer.oat"))
            print(f" -> {textler[10]}")
            
        # Temizlik: İndirilen klasörü temizle
        shutil.rmtree(GUNCELLEME_KLASORU)
        print(f"{textler[11]}")
        return True

    except Exception as e:
        print(f"{textler[12]} {e}")
        return False

def guncelleme_kontrol():
    """Versiyonları karşılaştırır ve gerekirse güncellemeyi başlatır."""
    print(f"{textler[13]}")
    
    v_mevcut = versiyonu_getir_mevcut()
    v_guncel = versiyonu_getir_guncel()
    print(f"{textler[14]}")
    print(v_guncel)
    print(v_mevcut)
    if v_mevcut is None:
        print(f"{textler[15]}")
        return
        
    if v_guncel is None:
        print(f"{textler[16]}")
        return

    print(f"{textler[17]}{v_mevcut}")
    print(f"{textler[18]}{v_guncel}")
    print(textler[19])
    if v_mevcut != v_guncel:
        print(f"{textler[20]}")
        guncelleme_islemi_yap()
    else:
        print(f"{textler[21]}")

# --- SUNUCU YÖNETİM FONKSİYONLARI ---

def sunucuya_komut_gonder(process, komut):
    """Çalışan sunucuya komut gönderir."""
    try:
        if process.poll() is None:
            process.stdin.write(f"{komut}\n")
            process.stdin.flush()
            print(f"{textler[22]} {komut}")
    except Exception as e:
        print(f"{textler[23]} {e}")

def zamanlayici_thread(process):
    """Sunucu çalışırken arka planda süreyi sayar."""
    toplam_saniye = int(YENIDEN_BASLATMA_SAATI * 3600)
    gecen_saniye = 0
    
    print(f"{textler[24]} {YENIDEN_BASLATMA_SAATI} {textler[25]}")

    while gecen_saniye < toplam_saniye:
        if process.poll() is not None:
            return

        kalan_saniye = toplam_saniye - gecen_saniye
        kalan_dakika = kalan_saniye / 60

        for dk in UYARI_DAKIKALARI:
            if abs(kalan_dakika - dk) < 0.02:
                msg = f"say {textler[26]} {dk} {textler[27]}"
                sunucuya_komut_gonder(process, msg)
                time.sleep(2)

        time.sleep(1)
        gecen_saniye += 1

    sunucuya_komut_gonder(process, f"say {textler[28]}")
    time.sleep(3)
    sunucuya_komut_gonder(process, "stop")
    print(f"{textler[29]}")
    guncelleme_kontrol()

def sunucuyu_baslat():
    """Sunucuyu başlatır."""
    ekstra_args_str = " ".join(EKSTRA_ARGUMANLAR)
    komut = f"{JAVA_KOMUTU} {JAVA_ARGUMAN} -jar {JAR_DOSYASI} {ekstra_args_str}"
    print("-" * 40)
    print(f"{textler[30]} {komut}")
    print("-" * 40)
    
    try:
        process = subprocess.Popen(komut, shell=True, stdin=subprocess.PIPE, text=True)
        t = threading.Thread(target=zamanlayici_thread, args=(process,))
        t.daemon = True
        t.start()
        process.wait()
        return process.returncode
    except FileNotFoundError:
        print(f"{textler[31]}")
        return -1
    except KeyboardInterrupt:
        return "STOP"

def dongu():
    print(f"{textler[32]}")
    
    while True:
        try:
            
            print(f"{textler[33]} {JAVA_KOMUTU} {JAVA_ARGUMAN} -jar {JAR_DOSYASI}")
            print(f"{textler[34]} {type(UYARI_DAKIKALARI)} -> Değerler: {UYARI_DAKIKALARI}")
            print(f"{textler[35]} {GUNCELLEME_KLASORU}")
            # 1. Önce güncellemeyi kontrol et
            guncelleme_kontrol()
            
            # 2. Sonra sunucuyu başlat
            durum = sunucuyu_baslat()
            
            if durum == "STOP":
                print(f"\n{textler[36]}")
                break
            
            print(f"\n{textler[37]} {durum}).")
            print(f"⏳ {textler[38]} {BEKLEME_SURESI} {textler[39]}")
            time.sleep(BEKLEME_SURESI)
            
        except KeyboardInterrupt:
            print(f"\n{textler[40]}")
            sys.exit()

if __name__ == "__main__":
    
    dongu()