 #!bin/bash
source ~/ftm/bin/activate
cd ~/ftm/ftm
date >> logs/sql.log
python manage.py shell < knmi_database/importer.py
date >> logs/sql.log
