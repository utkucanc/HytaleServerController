# Hytale Sunucu Yöneticisi

Hytale oyun sunucusunu otomatik olarak yönetmek, güncellemek ve yeniden başlatmak için tasarlanmış bir Python uygulamasıdır.

## 🎯 Özellikler

- ✅ **Otomatik Versiyon Kontrol**: Mevcut ve güncel versiyonları karşılaştırarak güncellemeleri otomatik olarak yönetir
- ✅ **Otomatik Güncelleme**: Yeni sürümler otomatik olarak indirilir ve uygulanır
- ✅ **Zamanlı Sunucu Yönetimi**: Belirli zamanlarda sunucu yeniden başlatma işlemleri
- ✅ **Uyarı Sistemi**: Yeniden başlatmadan öncesini kullanıcılara bildirir (30, 10, 5, 1 dakika)
- ✅ **Yapılandırılabilir Ayarlar**: JSON tabanlı konfigürasyon dosyası ile kolayca özelleştirilebilir
- ✅ **Çok Dil Desteği**: Türkçe ve diğer dilleri destekler
- ✅ **EXE Dönüşümü**: PyInstaller ile Windows EXE dosyasına dönüştürülebilir

## 📋 Gereksinimler

- Python 3.7+
- Java (Hytale Sunucusu çalıştırmak için)
- PyInstaller (EXE oluşturmak için isteğe bağlı)

## 🚀 Kurulum

### 1. Kaynak Kodlarını İndir
```bash
git clone <repository-url>
cd Test/src
```

### 2. Yapılandırma Dosyasını Oluştur
İlk çalışmada otomatik olarak `config.json` dosyası varsayılan ayarlarla oluşturulur.

Veya dosyayı manuel olarak yapılandırmak için:
```bash
python main.py
```

## ⚙️ Yapılandırma

`config.json` dosyasını düzenleyerek ayarları özelleştir:

```json
{
  "LANG": "TR",
  "JAVA_COMMAND": "java",
  "JAVA_ARGUMENT": "-Xms10G -Xmx20G -XX:+UseG1GC -XX:MaxGCPauseMillis=150 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 -XX:AOTCache=HytaleServer.aot",
  "JAR_FILE": "HytaleServer.jar",
  "DOWNLOADER_FILE": "hytale-downloader-windows-amd64.exe",
  "EXTRA_ARGUMENTS": ["--assets Assets.zip"],
  "UPDATE_FOLDER": "C:\\HaytaleServerUpdate",
  "UPDATE_ZIP_NAME": "Lastest.zip",
  "WAIT_TIME": 10,
  "REBOOT_TIME": 4.0,
  "WARNING_MINUTES": [30, 10, 5, 1]
}
```

### Yapılandırma Parametreleri

| Parametre | Açıklama | Varsayılan |
|-----------|----------|-----------|
| `LANG` | Arayüz dili (TR, EN vb.) | `TR` |
| `JAVA_COMMAND` | Java komutu yolu | `java` |
| `JAVA_ARGUMENT` | Java JVM argümanları | `-Xms10G -Xmx20G ...` |
| `JAR_FILE` | Sunucu JAR dosyasının adı | `HytaleServer.jar` |
| `DOWNLOADER_FILE` | Hytale downloader dosyasının adı | `hytale-downloader-windows-amd64.exe` |
| `EXTRA_ARGUMENTS` | Ek argümanlar | `["--assets Assets.zip"]` |
| `UPDATE_FOLDER` | Güncelleme dosyalarının klasörü | `C:\\HaytaleServerUpdate` |
| `UPDATE_ZIP_NAME` | Güncelleme ZIP dosyasının adı | `Lastest.zip` |
| `WAIT_TIME` | Komut gönderme bekleme süresi (saniye) | `10` |
| `REBOOT_TIME` | Yeniden başlatma süresi (saat) | `4.0` |
| `WARNING_MINUTES` | Uyarı verilecek dakikalar | `[30, 10, 5, 1]` |

## 📁 Dosya Yapısı

```
Test/src/
├── main.py              # Ana uygulama dosyası
├── config.py            # Yapılandırma yönetimi
├── lang.py              # Çok dil desteği
├── install.py           # PyInstaller için EXE oluşturma
├── config.json          # Yapılandırma dosyası (otomatik oluşturulur)
└── readme.md            # Bu dosya
```

## 🎮 Kullanım

### Python ile Çalıştır
```bash
python main.py
```

### EXE Dosyası Oluştur
```bash
python install.py
```

Bu komut `HytaleSunucuYoneticisi.exe` dosyasını oluşturur.

## 📝 Dosya Açıklamaları

### main.py
Sunucunun ana yönetim işlevlerini gerçekleştirir:
- Versiyon kontrolü
- Otomatik güncelleme
- Zamanlı yeniden başlatma
- Uyarı sistemi

### config.py
Yapılandırma dosyası yönetimini sağlar:
- Varsayılan ayarları tanımlar
- Yapılandırma dosyasını okur/yazar

### lang.py
Çok dil desteği sağlar:
- Türkçe metinler
- Diğer dillerin eklenmesini destekler

### install.py
PyInstaller ile EXE dönüşümü sağlar:
- PyInstaller kontrolü ve kurulumu
- EXE dosyası oluşturma

## 🔧 Sorun Giderme

### Downloader dosyası bulunamadı
- `DOWNLOADER_FILE` yolunun `config.json` dosyasında doğru olduğundan emin olun
- Hytale Downloader'ın bilgisayara kurulu olduğundan emin olun

### Versiyon bilgisi alınamadı
- Java yüklü ve PATH'e ekli olduğundan emin olun
- `JAR_FILE` yolunun doğru olduğundan emin olun

### EXE oluşturulamıyor
- PyInstaller kurulumuna devam etmek için:
```bash
pip install pyinstaller
```

## 🌐 Dil Desteği

Uygulamayı farklı dillerde kullanmak için `config.json` dosyasında `LANG` değerini değiştirebilirsiniz.

## 📄 Lisans

Bu proje açık kaynaklıdır. Kendi ihtiyaçlarınıza göre kullanabilir ve değiştirebilirsiniz.

## 🤝 Katkı

Hata bildirimi veya iyileştirme önerileri için lütfen bir issue açın.

## 💡 Öneriler

- Sunucu dosyalarını yedeklemek için otomatik yedekleme sistemi eklemeyi düşünün
- Hata günlüğü(log) sistemi ekleyin
- Web tabanlı kontrol paneli oluşturmayı değerlendirin
- Windows Hizmeti olarak çalıştırma desteği ekleyin

---

**Geliştirme Tarihi:** Şubat 2026

---

# Hytale Server Manager

A Python application designed to automatically manage, update, and restart the Hytale game server.

## 🎯 Features

- ✅ **Automatic Version Control**: Compares current and latest versions to manage updates automatically
- ✅ **Automatic Updates**: New versions are automatically downloaded and applied
- ✅ **Scheduled Server Management**: Restart server operations at specific times
- ✅ **Warning System**: Notifies users before restart (30, 10, 5, 1 minutes)
- ✅ **Configurable Settings**: Easily customizable with JSON-based configuration file
- ✅ **Multi-Language Support**: Supports Turkish and other languages
- ✅ **EXE Conversion**: Can be converted to Windows EXE file with PyInstaller

## 📋 Requirements

- Python 3.7+
- Java (to run Hytale Server)
- PyInstaller (optional, for EXE creation)

## 🚀 Installation

### 1. Download Source Code
```bash
git clone <repository-url>
cd Test/src
```

### 2. Create Configuration File
The `config.json` file is automatically created with default settings on first run.

Or to configure manually:
```bash
python main.py
```

## ⚙️ Configuration

Customize settings by editing the `config.json` file:

```json
{
  "LANG": "TR",
  "JAVA_COMMAND": "java",
  "JAVA_ARGUMENT": "-Xms10G -Xmx20G -XX:+UseG1GC -XX:MaxGCPauseMillis=150 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 -XX:AOTCache=HytaleServer.aot",
  "JAR_FILE": "HytaleServer.jar",
  "DOWNLOADER_FILE": "hytale-downloader-windows-amd64.exe",
  "EXTRA_ARGUMENTS": ["--assets Assets.zip"],
  "UPDATE_FOLDER": "C:\\HaytaleServerUpdate",
  "UPDATE_ZIP_NAME": "Lastest.zip",
  "WAIT_TIME": 10,
  "REBOOT_TIME": 4.0,
  "WARNING_MINUTES": [30, 10, 5, 1]
}
```

### Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `LANG` | Interface language (TR, EN, etc.) | `TR` |
| `JAVA_COMMAND` | Java command path | `java` |
| `JAVA_ARGUMENT` | Java JVM arguments | `-Xms10G -Xmx20G ...` |
| `JAR_FILE` | Server JAR file name | `HytaleServer.jar` |
| `DOWNLOADER_FILE` | Hytale downloader file name | `hytale-downloader-windows-amd64.exe` |
| `EXTRA_ARGUMENTS` | Additional arguments | `["--assets Assets.zip"]` |
| `UPDATE_FOLDER` | Update files folder | `C:\\HaytaleServerUpdate` |
| `UPDATE_ZIP_NAME` | Update ZIP file name | `Lastest.zip` |
| `WAIT_TIME` | Command send wait time (seconds) | `10` |
| `REBOOT_TIME` | Restart time (hours) | `4.0` |
| `WARNING_MINUTES` | Warning minutes | `[30, 10, 5, 1]` |

## 📁 File Structure

```
Test/src/
├── main.py              # Main application file
├── config.py            # Configuration management
├── lang.py              # Multi-language support
├── install.py           # EXE creation with PyInstaller
├── config.json          # Configuration file (auto-generated)
└── readme.md            # This file
```

## 🎮 Usage

### Run with Python
```bash
python main.py
```

### Create EXE File
```bash
python install.py
```

This command creates the `HytaleSunucuYoneticisi.exe` file.

## 📝 File Descriptions

### main.py
Performs main server management functions:
- Version control
- Automatic updates
- Scheduled restarts
- Warning system

### config.py
Provides configuration file management:
- Defines default settings
- Reads/writes configuration file

### lang.py
Provides multi-language support:
- Turkish texts
- Supports adding other languages

### install.py
Provides EXE conversion with PyInstaller:
- PyInstaller verification and installation
- EXE file creation

## 🔧 Troubleshooting

### Downloader file not found
- Ensure the `DOWNLOADER_FILE` path is correct in `config.json`
- Ensure Hytale Downloader is installed on your computer

### Version information not retrieved
- Ensure Java is installed and added to PATH
- Ensure the `JAR_FILE` path is correct

### Cannot create EXE
- Continue with PyInstaller installation:
```bash
pip install pyinstaller
```

## 🌐 Language Support

To use the application in different languages, change the `LANG` value in the `config.json` file.

## 📄 License

This project is open source. You can use and modify it according to your needs.

## 🤝 Contributing

Please open an issue for bug reports or improvement suggestions.

## 💡 Recommendations

- Consider adding an automatic backup system for server files
- Add error logging system
- Consider creating a web-based control panel
- Add support for running as a Windows Service

---

**Development Date:** February 2026
