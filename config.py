import os
import sys
import json
import time

# --- VARSAYILAN AYARLAR ---
VARSAYILAN_AYARLAR = {
    "LANG": "TR",
    "JAVA_COMMAND": "java",
    "JAVA_ARGUMENT": "-Xms10G -Xmx20G -XX:+UseG1GC -XX:MaxGCPauseMillis=150 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 -XX:AOTCache=HytaleServer.aot",
    "JAR_FILE": "HytaleServer.jar",
    "DOWNLOADER_FILE": "hytale-downloader-windows-amd64.exe",
    "EXTRA_ARGUMENTS": [
        "--assets Assets.zip"
    ],
    "UPDATE_FOLDER": "C:\\HaytaleServerUpdate",
    "UPDATE_ZIP_NAME": "Lastest.zip",
    "WAIT_TIME": 10,
    "REBOOT_TIME": 4.0,
    "WARNING_MINUTES": [
        30, 10, 5, 1
    ]
}
# ----------------
def config_yukle(dosya_yolu):
    """
    Config dosyasını okur. Eğer dosya yoksa varsayılan ayarlarla yenisini oluşturur.
    """
    # Dosya yoksa oluştur
    if not os.path.exists(dosya_yolu):
        print(f"⚠️BİLGİ: '{dosya_yolu}' bulunamadı. Varsayılan ayarlarla oluşturuluyor...⚠️")
        print(f"INFO: ‘{dosya_yolu}’ not found. Creating with default settings...")
        print("⚠️Default settings are in Turkish⚠️\n⚠️Update to ‘EN’ for English.⚠️")
        
        try:
            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                # indent=4 parametresi JSON dosyasının alt alta ve okunaklı olmasını sağlar
                json.dump(VARSAYILAN_AYARLAR, f, indent=4, ensure_ascii=False)
                time.sleep(3)
            return VARSAYILAN_AYARLAR
        
        except Exception as e:
            print(f"HATA: Config dosyası oluşturulamadı! Detay: {e}")
            sys.exit(1)
    
    # Dosya varsa oku
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        # Kullanıcı dosyayı eliyle düzenlerken virgül vb. unutursa uyarır
        print(f"HATA: '{dosya_yolu}' dosyasının JSON formatı bozuk! Lütfen düzeltin veya silip yeniden oluşmasını sağlayın.")
        print(f"Hata Detayı: {e}")
        sys.exit(1)
    
        