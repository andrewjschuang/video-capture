export FLASK_APP="backend/server.py"
export FLASK_DEBUG=true

if [ ! -d backend/venv ]; then
    echo "venv not found, run init_venv.sh first"
    exit 1
fi

source backend/venv/bin/activate
echo dont forget to use /configure!
flask run
