# Lab 5 Reflection: Static Code Analysis

**Name:** Monisha Sharma
**SRN**: PES2UG23CS906 
**Date:** October 27, 2025





## Question 1: Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest Issues:**
- Removing the unused `logging` import (line 4) - just delete one line
- Removing `eval()` (line 61) - simple replacement with print statement
- Adding blank lines between functions - mechanical find and insert

**Hardest Issues:**
- Renaming all camelCase functions to snake_case was tedious because I had to:
  - Rename all 8 function definitions
  - Update all function calls in main() also
  - Ensure that I didn't miss any references
- Understanding that the mutable default argument bug required research to understand why `logs=[]` is dangerous
- Writing meaningful docstrings for all functions took thought and time

**Why the difference?**
Syntax and formatting fixes are quick because they can be easily done manually. 
Logic bugs and design improvements were required to be understanding Python's behavior and thinking about best practices.

## Question 2: Did the static analysis tools report any false positives? If so, describe one example.

I didn't encounter clear false positives in this lab. All the issues reported were legitimate problems that should be fixed:

- The eval() warning was correct - it's a security risk
- The bare except was catching too much
- The naming violations were real PEP 8 issues

However, the "global statement" warning was subjective. For a small script like this, using a global variable isn't necessarily wrong, though it's not best practice. In a real application, we'd use a class or pass the data as parameters, but for this educational example, the global should be acceptable.

## Question 3: How would you integrate static analysis tools into your actual software development workflow?

**During Local Development:**
1. Configure VS Code with Python extensions to show Pylint warnings in real-time as I code
2. Set up pre-commit hooks using the `pre-commit` framework to automatically run Flake8 before allowing commits
3. Create a `pyproject.toml` or `.pylintrc` file to configure consistent rules across the team
4. Run `pylint` manually before pushing to catch issues early

**In CI/CD Pipeline:**
1. Add GitHub Actions workflow that runs all three tools on every pull request:
```yaml
   - name: Run Pylint
     run: pylint src/ --fail-under=8.0
   - name: Run Bandit
     run: bandit -r src/ -ll
   - name: Run Flake8
     run: flake8 src/
```
2. Set quality gates that block merges if:
   - Pylint score drops below 8.0
   - Bandit finds HIGH or MEDIUM severity issues
   - Flake8 finds any errors
3. Generate reports as artifacts for team review

**Team Practices:**
- Include static analysis results in code review checklist
- Schedule monthly "code quality" sprints to address accumulated warnings
- Use tools like SonarQube for centralized quality tracking

## Question 4: What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

**Security Improvements:**
- Removed the `eval()` vulnerability that could allow arbitrary code execution - this is critical for production code
- Proper exception handling prevents hiding errors and makes debugging easier

**Robustness:**
- Context managers ensure files are closed even if errors occur, preventing resource leaks
- Specific exception handling (KeyError) means we only catch expected errors, not system-level issues like KeyboardInterrupt
- Fixed mutable default argument prevents bugs where log entries accumulate unexpectedly across function calls

**Readability:**
- snake_case function names follow Python conventions, making code immediately familiar to other Python developers
- F-strings are clearer and more modern than % formatting
- Docstrings provide inline documentation so developers understand function purpose without reading implementation
- Proper spacing (blank lines) makes code structure clearer at a glance

**Measurable Quality:**
- Pylint score improved from 4.80/10 to 10/10
- Bandit issues reduced from 2 to 0
- Flake8 errors reduced from 11 to 0

**Overall Impact:**
The code went from messy working code to "production-ready." It now follows industry standards, has no known security vulnerabilities, and would be maintainable by other developers. The improvements make it suitable for a professional codebase rather than just a learning exercise.