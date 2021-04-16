# Python Typing Experiment

## About
This is an experiment for my work term report for the MAGNUM Core Dev Team at Evertz Microsystems. The purpose of this experiment is to see how effective type hints and static code analysis tools are for helping developers edit code, as well as measure the time cost of adding type hints to existing code.

To participate in this experiment, you will need to fork this GitHub repository, complete each task, record your results in the Google Form, and then create a pull request with your modified code.

## Software Requirements
- Python 3.8, with mypy and MonkeyType modules installed
    - Verify that mypy and MonkeyType are installed for Python 3.8 by running the following:
        - `python3.8 -m mypy -V`
        - `python3.8 -m monkeytype`
- A code editor with static code analysis tools that you are familiar with using.
    - e.g. Vim with jedi-vim and syntastic installed and mypy configured, VS Code with Python plugin, PyCharm, etc.

To configure syntastic to use mypy, do the following in your .vimrc:
- add 'mypy' to `g:syntastic_python_checkers`
    - e.g. `let g:syntastic_python_checkers=['flake8', 'mypy']`
- add the following lines:
    - `let g:syntastic_python_mypy_exec='python3.8'`
    - `let g:syntastic_python_mypy_args=['-m', 'mypy']`

# Before you start
This experiment requires you to have a basic understanding of how Python type hints work. For a brief introduction, please read the following:
- https://realpython.com/lessons/type-hinting/
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html (up to Functions)

You will also need to have some understanding of what mypy and MonkeyType are:
- mypy is a static type checker. It checks that your code follows your type hints.
- MonkeyType is a tool for generating type hints by running the program and recording the types passed to and returned from each function call.

You should also be familiar with the auto-completion and code inspection tools in your code editor. These tools become more powerful if the code has type hints.

# Instructions
1. Create a fork of this repository, and clone it to your computer.
2. Complete each task in the sections below. You will need to time how long it takes to complete each task, and record it in the Google Form.
3. Commit and push your changes, and create a pull request.

# Google Form
Please fill out this Google Form as you progress through each task: https://forms.gle/hTPUEpDYWNjf3p75A

# Part 1
For this part, you will be changing the name of variables in a Python program written without type hints.
1. Open the `1_rename_untyped/` directory. Take some time to familiarize yourself with the code in this directory.
2. (Timed) Open `clocks.py`. Rename the `clock` attribute of the `Microwave` class to `timer`. Also, rename the `clock` attribute of the `Referee` class to `stopwatch`. Be sure that all occurences of these attributes are renamed as well.
3. Record the time it took to complete the previous step in the Google Form.

# Part 2
For this part, you will be changing the name of variables in a Python program written with type hints.
1. Open the `2_rename_typed/` directory. Take some time to familiarize yourself with the code in this directory.
2. (Timed) Open `clocks.py`. Rename the `clock` attribute of the `Microwave` class to `timer`. Also, rename the `clock` attribute of the `Referee` class to `stopwatch`. Be sure that all occurences of these attributes are renamed as well.
3. Record the time it took to complete the previous step in the Google Form.
4. Also record what differences (if any) you experienced when completing Part 2 as compared with Part 1.

# Part 3
For this part, you will be making modifications to a method in order to fix a failing test. The code will not have any type hints.
1. Open the `3_electric_grid_untyped/` directory. Take some time to familiarize yourself with the code in this directory, especially the `test_old_nuclear_power_plant_id` function in `test.py`.
2. (Timed) Run `test.py`, and note that an assertion in `test_old_nuclear_power_plant_id` is failing. Find and fix the bug.
3. Record the time it took to complete the previous step in the Google Form.

# Part 4
For this part, you will be making modifications to a method in order to fix a failing test. The code will have type hints.
1. Open the `4_electric_grid_typed/` directory. Take some time to familiarize yourself with the code in this directory, especially the `test_old_nuclear_power_plant_id` function in `test.py`.
2. (Timed) Run `test.py`, and note that an assertion in `test_old_nuclear_power_plant_id` is failing. Find and fix the bug with the help of static code analysis.
3. Record the time it took to complete the previous step in the Google Form.
4. Also record what differences (if any) you experienced when completing Part 4 as compared with Part 3.

# Part 5
For this part, you will be adding type hints to an existing Python file with the help of MonkeyType.
1. Open the `3_electric_grid_untyped/` directory. Take some time to familiarize yourself with the code in this directory, especially `nuclear.py`.
2. (Timed) Add type hints to `nuclear.py` with the help of MonkeyType and mypy.
    1. Run `monkeytype run test.py` in order for MonkeyType to generate the types.
    2. Run `monkeytype stub nuclear` to see what type hints MonkeyType has generated. Note that it has not generated type hints for any private methods.
    3. Run `monkeytype apply nuclear` to apply the suggested type hints.
    4. Run `mypy --strict nuclear.py` to see what type hints are missing.
    5. Manually add the missing type hints to `nuclear.py` until mypy no longer complains about missing annotations in `nuclear.py`. Also check over the type hints applied by MonkeyType and make alterations if necessary.
3. Record the time it took to complete the previous step in the Google Form.
4. Also record a short description of your experience adding type hints to `nuclear.py`.

# Part 6
There is a little survey in the Google Form. Please fill out the survey with some short answers (no need for proper grammar).
