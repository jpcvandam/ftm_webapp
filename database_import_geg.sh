 #!bin/bash
source ~/ftm/bin/activate
cd ~/ftm/ftm
python manage.py shell < knmi_database/importer.py
