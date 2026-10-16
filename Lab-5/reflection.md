# Lab 5: Static Code Analysis — Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were trailing whitespace, long lines, missing docstrings, and incorrect naming conventions. These required straightforward formatting and documentation changes without significantly affecting program logic.

The hardest issue was the potential SQL injection vulnerability because it required understanding how unsafe string-based SQL queries could be exploited and how parameterized queries prevent that problem. Replacing insecure random PIN generation and improving exception handling also required considering security and reliability.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

No clear false positives were identified in the reports. The warnings were relevant to the original code and could be addressed through meaningful changes. For example, Bandit detected the use of `random.randint()` for generating an unlock PIN. Although this function can be acceptable for ordinary random numbers, a security-sensitive PIN should use the `secrets` module. Therefore, the warning was appropriate in this application.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate Pylint, Bandit, and Flake8 into my development workflow by running them regularly while writing Python code. Before committing changes to GitHub, I would use Pylint to check code quality, Bandit to detect security vulnerabilities, and Flake8 to check coding-style violations.

I would also include these checks in a continuous integration pipeline so that issues can be detected automatically whenever code is pushed to the repository.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the Python code became more readable, secure, and maintainable. Parameterized SQL queries reduced SQL injection risks, secure PIN generation improved security, and specific exception handling made errors easier to identify.

Consistent function naming, documentation, and improved formatting made the code easier to understand. The Pylint score increased from 3.89/10 to 10.00/10, Bandit findings decreased from 3 to 0, and Flake8 violations decreased from 10 to 0. These results demonstrate measurable improvements in the quality of the code.