#!/bin/bash

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly BLUE='\033[0;34m'
readonly NO_COLOR='\033[0m'
readonly BASE_URL="http://localhost:8000/api"

print_separator() {
    printf "${BLUE}=%.0s" {1..100}
    printf "${NO_COLOR}\n"
}

print_header() {
    print_separator
    printf "| ${BLUE}%-40s${NO_COLOR} | ${BLUE}%-10s${NO_COLOR} | ${BLUE}%-27s${NO_COLOR} | ${BLUE}%-10s${NO_COLOR} |\n" "URL" "METHOD" "DATA" "STATUS"
    print_separator
}

print_status_line() {
    local url=$1
    local method=$2
    local data=$3
    local status=$4
    
    if [[ $status -ge 200 && $status -lt 400 ]]; then
        status_color=$GREEN
    else
        status_color=$RED
    fi

    if [[ "$data" != "null" && "$data" == {* ]]; then
        local display_data=$(echo "$data" | jq -r '[.[]] | join(", ")')
    else
        local display_data=$data
    fi

    printf "| %-40s | %-10s | %-27s | ${status_color}%-10s${NO_COLOR} |\n" "$url" "$method" "$display_data" "$status"
}

test_index() {
    local resource=$1
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$BASE_URL/$resource")

    print_status_line "/$resource" "GET" "null" "$status_code"
}

test_show() {
    local resource=$1
    local id=$2
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$BASE_URL/$resource/$2")

    print_status_line "/$resource/$2" "GET" "null" "$status_code"
}

test_create() {
    local resource=$1
    local data='{"title":"Product Test","price":123.4,"amount":123}'
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE_URL/$resource" \
                        --header 'Accept: application/json' \
                        --header 'Content-Type: application/json' \
                        --data "$data")

    print_status_line "/$resource" "POST" "$data" "$status_code"
}

test_update() {
    local resource=$1
    local id=$2
    local data='{"title":"Product Updated","price":123.4,"amount":123}'
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" -X PUT "$BASE_URL/$resource/$2" \
                        --header 'Accept: application/json' \
                        --header 'Content-Type: application/json' \
                        --data "$data")

    print_status_line "/$resource/$2" "PUT" "$data" "$status_code"
}

test_delete() {
    local resource=$1
    local id=$2
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE "$BASE_URL/$resource/$2")

    print_status_line "/$resource/$2" "DELETE" "null" "$status_code"
}

get_first_resource() {
    local resource=$1

    local response=$(curl -s -X GET "$BASE_URL/$resource")
    local first_product_id=$(echo "$response" | jq -r '.[0].id')

    echo "$first_product_id"
}

test_crud() {
    print_header

    test_index "product"
    local resource_id=$(get_first_resource "product")
    test_show "product" "$resource_id"
    test_create "product"
    test_update "product" "$resource_id"
    test_delete "product" "$resource_id"
}


test_crud