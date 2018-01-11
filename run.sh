export FLASK_APP=portal.py
if [[ "$1" == "--prod" ]]; then
	export FLASK_DEBUG=0
	HOST='0.0.0.0'
	PORT=4244
	nohup='nohup '
else
	export FLASK_DEBUG=1
	HOST='127.0.0.1'
	PORT=5000
	nohup=''
fi

${nohup}python3 -m flask run --port $PORT --host $HOST
