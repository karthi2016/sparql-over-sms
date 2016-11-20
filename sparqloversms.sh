#!/bin/bash
args=("$@")

root_dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
compression_dir=$root_dir/sos-compression
service_dir=$root_dir/sos-service
service_src_dir=$service_dir/src
sosservice_py=$service_dir/src/sos_service.py
sosserver_py=$service_dir/src/sos_server.py
sosworker_py=$service_dir/src/sos_worker.py

function check_installation {
    commands=( "java" "mvn" "python3" "virtualenv" )
    for c in "${commands[@]}"
    do
        command -v $c >/dev/null 2>&1 || { 
            echo >&2 "I require '$c' but it's not installed. Aborting.";
            exit 1; 
        }
    done

    cd $compression_dir
    if [ ! -d "target" ]; then
        mvn package -f "pom.xml" -DskipTests
    fi

    cd $service_dir
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

    export C_FORCE_ROOT='true'

    cd $root_dir
}

function docker_service {
    check_installation
    cd $service_src_dir

    python3 $sosservice_py START --triplestore=sos-triplestore --taskqueue=sos-taskqueue
}

function docker_server {
    check_installation
    cd $service_src_dir

    python3 $sosserver_py START --triplestore=sos-triplestore --taskqueue=sos-taskqueue
}

function docker_worker {
    check_installation
    cd $service_src_dir

    python3 $sosworker_py START --triplestore=sos-triplestore --taskqueue=sos-taskqueue
}

function start_service {
    check_installation
    cd $service_src_dir

    python3 $sosserver_py START --background
    python3 $sosworker_py START --background
}

function stop_service {
    check_installation
    cd $service_src_dir

    python3 $sosserver_py STOP
    python3 $sosworker_py STOP
}

function restart_sevice {
    check_installation
    cd $service_src_dir

    python3 $sosserver_py RESTART
    python3 $sosworker_py RESTART
}

shopt -s nocasematch
case ${args[0]} in
    install)
        check_installation
        ;;
    docker)
        docker_service
        ;;
    docker-server)
        docker_server
        ;;
    docker-worker)
        docker_worker
        ;;
    start)
        start_service
        echo Started SPARQL over SMS service.
        while :; do
            sleep 300
        done        
        ;;
    stop)
        stop_service
        echo Stopped SPARQL over SMS service.
        ;;
    restart)
        restart_sevice
        echo Restarted SPARQL over SMS service.
        ;;
    *)
        echo $"Usage: $0 {install|docker|docker-server|docker-worker|start|stop|restart}"
        exit 1
esac