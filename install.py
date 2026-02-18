import subprocess
import sys
import os
import shutil
import time

# --- AYARLAR ---
HEDEF_DOSYA = "main.py"
EXE_ADI = "HytaleSunucuYoneticisi"
ICON_DOSYASI = ""

# ----------------


def kutuphane_kontrol_et():
    print("🔍 PyInstaller kontrol ediliyor...")
    try:
        import PyInstaller
        print("✅ PyInstaller zaten yüklü.")
    except ImportError:
        print("⬇️ PyInstaller bulunamadı, yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller başarıyla yüklendi.")


def exe_olustur():
    if not os.path.exists(HEDEF_DOSYA):
        print(f"❌ HATA: '{HEDEF_DOSYA}' bulunamadı!")
        return

    print("🔨 EXE oluşturma işlemi başlıyor...")

    komutlar = [
        HEDEF_DOSYA,
        "--onefile",
        "--console",
        f"--name={EXE_ADI}",
        "--clean",

        # 🔥 Eklenenler:
        "--hidden-import=config",
        "--hidden-import=lang",
    ]



    if ICON_DOSYASI and os.path.exists(ICON_DOSYASI):
        komutlar.append(f"--icon={ICON_DOSYASI}")
    elif ICON_DOSYASI:
        print(f"⚠️ İkon dosyası '{ICON_DOSYASI}' bulunamadı.")

    import PyInstaller.__main__

    try:
        PyInstaller.__main__.run(komutlar)
        print("\n✅ EXE başarıyla oluşturuldu!")
        print(f"📂 dist klasörü içinde: {EXE_ADI}.exe")
    except Exception as e:
        print(f"❌ HATA: {e}")


def temizlik_yap():
    print("🧹 Temizlik yapılıyor...")

    if os.path.exists("build"):
        shutil.rmtree("build")

    spec_file = f"{EXE_ADI}.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)

    print("✨ Temizlik tamamlandı.")


if __name__ == "__main__":
    kutuphane_kontrol_et()
    time.sleep(1)
    exe_olustur()
    temizlik_yap()

    print("\nÇıkmak için bir tuşa basın...")
    input()
