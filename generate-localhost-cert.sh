#!/bin/bash

set -e

CERT_DIR="./certs"
mkdir -p "${CERT_DIR}"

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout "${CERT_DIR}/localhost.key" \
  -out "${CERT_DIR}/localhost.crt" \
  -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=localhost"

echo "Self-signed cert generated at ${CERT_DIR}/localhost.crt"
echo "Private key generated at ${CERT_DIR}/localhost.key"
