#!/usr/bin/env bash
echo "Please make sure you have the Hyperfine benchmarking tool installed!"
hyperfine -r 100 "python3 ./Attempt_1.py" "python3 ./Attempt_1.5.py" "python3 ./Attempt_2.py"
