 #!/bin/bash
date >> ~/ftm/ftm/logs/vul_log.log
source ~/ftm/bin/activate
cd ~/ftm/ftm/ftm
python datagrab_parse_knmi.py
date >> ~/ftm/ftm/logs/vul_log.log
cd ~/ftm/ftm
python manage.py shell < knmi_database/importer.py 2>> ~/ftm/ftm/logs/vul_log.log
date >> ~/ftm/ftm/logs/vul_log.log
