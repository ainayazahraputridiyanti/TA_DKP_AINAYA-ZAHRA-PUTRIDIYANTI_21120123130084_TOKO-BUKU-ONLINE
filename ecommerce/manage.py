#skrip untuk menjalankan tugas-tugas administratif dalam proyek Django
#sudah ada dari sananya (dari Django nya langsung)

#!/usr/bin/env python -> skrip harus dijalankan menggunakan interpreter Python yang ditemukan di environment pengguna

"""Django's command-line utility for administrative tasks."""
#skrip ini adalah utilitas baris perintah untuk tugas-tugas administratif Django

import os
import sys
#mengimpor modul os dan sys yang diperlukan untuk pengaturan environment dan penanganan argumen baris perintah

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings') 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
