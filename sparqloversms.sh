#!/bin/bash
args=("$@")

script_dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
service_dir=$script_dir/sos-service
sosserver_py=$service_dir/src/sos_server.py
sosworker_py=$service_dir/src/sos_worker.py

function activate_venv {
    cd $service_dir
    
    command -v virtualenv >/dev/null 2>&1 || { 
        echo >&2 "I require virtualenv but it's not installed. Aborting.";
        exit 1; 
    }

    if [ ! -d "venv-linux" ]; then
        virtualenv venv-linux        
    fi

    source "venv-linux/bin/activate"

    requirements=$(cat requirements.txt)
    installed="$(pip3 freeze)"

    if [ ! "$requirements" = "$installed" ]; then
        pip3 install -r requirements.txt
        pip3 freeze > requirements.txt
    fi
}

function start_service {
    activate_venv

    export C_FORCE_ROOT='true'

    python3 $sosserver_py START --background
    python3 $sosworker_py START --background

    echo Started SPARQL over SMS service.
}

function stop_service {
    activate_venv

    python3 $sosserver_py STOP
    python3 $sosworker_py STOP

    echo Stopped SPARQL over SMS service.
}

function restart_sevice {
    activate_venv

    python3 $sosserver_py RESTART
    python3 $sosworker_py RESTART

    echo Restarted SPARQL over SMS service.
}

shopt -s nocasematch
case ${args[0]} in
    install)
        activate_venv
        ;;
    docker-start)
        start_service
        while :; do
            sleep 300
        done
        ;;
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        restart_sevice
        ;;
    *)
        echo $"Usage: $0 {install|docker-start|start|stop|restart}"
        exit 1
esac