#!/bin/bash
args=("$@")

root_dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
compression_dir=$root_dir/sos-compression
service_dir=$root_dir/sos-service
service_src_dir=$service_dir/src
admin_dir=$root_dir/sos-admin
sosservice_py=$service_dir/src/sos_service.py
sosserver_py=$service_dir/src/sos_server.py
sosworker_py=$service_dir/src/sos_worker.py

function check_installation {
    commands=( "java" "mvn" "python3" "virtualenv" "npm" )
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

    cd $admin_dir
    if [ ! -d "node_modules" ]; then
        npm install
    fi    

    cd $service_dir
    if [ ! -d "env" ]; then
        virtualenv env        
    fi
    source "env/bin/activate"

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

    cd $admin_dir
    npm run dev &

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

function docker_admin {
    check_installation

    cd $admin_dir
    npm run dev
}

shopt -s nocasematch
case ${args[0]} in
    install)
        check_installation
        ;;
    start)
        docker_service
        ;;        
    server-only)
        docker_server
        ;;
    worker-only)
        docker_worker
        ;;
    admin-only)
        docker_admin
        ;;
    *)
        echo $"Usage: $0 {install|start|server-only|worker-only|admin-only}"
        exit 1
esac