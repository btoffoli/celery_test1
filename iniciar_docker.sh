touch .bash_history && export UID && docker-compose up --build -d && docker ps --format "{{.ID}}" | xargs ^Ccker container inspect | jq '.[] | "\(.NetworkSettings.Networks | keys[] as $k | "\(.[$k].IPAddress)    \($k)") \(.Config.Hostname)"' | while read line;do echo ${line//'"'/}; done | grep -e '^[0-9]' | sort -k3 | grep 'celery_test1'