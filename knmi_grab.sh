 #!bin/bash
source ~/ftm/bin/activate
cd ~/ftm/ftm/ftm
python datagrab_parse_knmi.py
cd ~/ftm/ftm
python manage.py shell < knmi_database/importer.py
