web: bash -c 'gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000 --workers 4 & nginx -p . -c nginx.conf'
