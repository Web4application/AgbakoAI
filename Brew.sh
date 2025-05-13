./config.sh --url https://github.com/QUBUHUB-incs/AgbakoAI --token BH6MBWC5MQDJJEF7AG474WTIEKNEM
curl -o actions-runner-linux-arm64-2.323.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.323.0/actions-runner-linux-arm64-2.323.0.tar.gz

echo "9cb778fffd4c6d8bd74bc4110df7cb8c0122eb62fda30b389318b265d3ade538  actions-runner-linux-arm64-2.323.0.tar.gz" | shasum -a 256 -c

tar xzf ./actions-runner-linux-arm64-2.323.0.tar.gz
