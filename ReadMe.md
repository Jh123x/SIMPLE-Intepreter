# SIMPLE Intepreter

An intepreter for the SIMPLE language based on CS3203 SIMPLE language [here](https://github.com/nus-cs3203/project-wiki/wiki/Basic-SPA-Requirements)
Completed in [python](https://www.python.org/)

# Quick start
1. Clone the repository using `git clone https://github.com/Jh123x/SIMPLE-Intepreter.git`
1. Run `__main__.py` using `python __main__.py [filepath]` to run the Simple Language


# Tech Stack
1. [rply](https://pypi.org/project/rply/)

# Difficulties during the process
1. Lexor detects `printData` as `Print token` and `Name token`.
1. Wrong ordering of different rules in the `lexor`.
1. Making a multiline parser using `statements` rather than just 1 line.


# To do
1. Bug fixes (If there are any bugs please let me know)
1. Code clean up (Spaghetti code currently)
