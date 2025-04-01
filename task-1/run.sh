#!/bin/bash

build_project() {
    docker build . -t vicky/docker-pascal
    docker run --rm -v "$(pwd):/app" -w /app vicky/docker-pascal fpc RandomGenerator.pas
    docker run -it --rm -v "$(pwd):/app" -w /app vicky/docker-pascal ./RandomGenerator
}

run_tests() {
    docker build . -t vicky/docker-pascal
    docker run --rm -v "$(pwd):/app" -w /app vicky/docker-pascal fpc -Fu./fptest/src -Fu./fptest/3rdparty/epiktimer -Mobjfpc Tests.pas
    docker run -it --rm -v "$(pwd):/app" -w /app vicky/docker-pascal ./Tests
}

show_help() {
    echo "Script to build or test Pascal project"
    echo ""
    echo "Options:"
    echo "  -build     Build and run the project"
    echo "  -test      Compile and run tests"
    echo "  -help      Display this help message"
}

case $1 in
    -build)
        build_project
        ;;
    -tests)
        run_tests
        ;;

    -help)
        show_help
        ;;
    *)
        exit 1
        ;;
esac
