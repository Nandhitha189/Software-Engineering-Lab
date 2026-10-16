# Lab 5: Static Code Analysis — Issue Documentation

## Project
Bike Share Stations

## Tools Used
Pylint, Bandit, Flake8

## Identified Issues and Fixes

| Issue | Type | Original Line | Description | Fix Applied |
|---|---|---|---|---|
| B608 SQL Injection | Security | 9 | SQL query constructed using string concatenation, allowing potential SQL injection. | Replaced string concatenation with parameterized SQL queries using placeholders. |
| B311 Insecure Randomness | Security | 22 | `random.randint()` was used to generate unlock PINs. | Replaced it with the cryptographically secure `secrets.randbelow()`. |
| B110 Silent Exception | Security/Robustness | 34–35 | `except Exception: pass` silently ignored errors. | Used specific `sqlite3.Error` handling and reported database errors. |
| W0102 Mutable Default Argument | Bug | 8 | Default list `log=[]` could retain data between function calls. | Replaced it with `log=None` and initialized an empty list inside the function. |
| R1710 Inconsistent Returns | Code Quality | 14–18 | Rental function returned `True` in one path and implicitly returned `None` in another. | Added an explicit `False` return when rental fails. |
| W0612 Unused Variable | Code Quality | 27 | Variable `summary` was assigned but never used. | Removed the unused variable. |
| E711 None Comparison | Style/Correctness | 40 | Used `== None` rather than `is None`. | Replaced with appropriate `is None` checks. |
| C0103 Naming Convention | Style | Multiple | Function names were written in camelCase. | Renamed functions using snake_case. |
| C0114/C0116 Missing Docstrings | Documentation | Multiple | Module and functions lacked documentation. | Added descriptive docstrings. |
| E501/C0301 Long Lines | Style | Multiple | Several lines exceeded the recommended line length. | Reformatted long statements across multiple lines. |
| W291/C0303 Trailing Whitespace | Style | 27 | Unnecessary trailing spaces were present. | Removed trailing whitespace. |

## Static Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 3.89/10 | 10.00/10 |
| Bandit | 3 issues | 0 issues |
| Flake8 | 10 violations | 0 violations |

## Conclusion

Static code analysis identified security vulnerabilities, potential bugs, and coding-style violations in the original Bike Share Stations application. The identified issues were corrected, and all three tools were executed again to verify the improvements. The final analysis reported a Pylint score of 10.00/10, no Bandit security findings, and no Flake8 violations.