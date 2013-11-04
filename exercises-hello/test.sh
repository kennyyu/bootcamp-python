#!/bin/bash

prog="hello.py"
expected="hello world"
output=$(python $prog)

if [[ $output = $expected ]]
then
    echo "Test passed!"
else
    echo "Test failed! Mismatch in output:"
    echo "Expected: $expected"
    echo "Got     : $output"
fi