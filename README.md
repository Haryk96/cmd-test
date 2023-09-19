# `mkdir` Test Suite

## Overview

This test suite partially evaluates the behavior of the `mkdir` command in a Unix environment. It includes various test cases to check the creation of directories with and without the `-p` option, both in non-nested and nested scenarios.

## Test Cases

### Non-Nested Directory Creation

- Create a single directory without any options.
- Create multiple directories without any options.

### Nested Directory Creation

- Create a nested directory without any options.
- Create multiple nested directories without any options.

### Non-Nested Directory Creation with `-p` Option

- Create a single directory with the `-p` option.
- Create multiple directories with the `-p` option.

### Nested Directory Creation with `-p` Option

- Create a nested directory with the `-p` option.
- Create multiple nested directories with the `-p` option.

## Limitations

This test suite focuses on evaluating the `-p` option of the `mkdir` command and does not cover testing other command options, as doing so would be time-consuming.

## Requirements
- Developed and tested for `Python 3.11`
- None, the standard library should be sufficient to run the test

## How to Run

Execute the test suite by running the following command:

```bash
python3 tests/main.py
```