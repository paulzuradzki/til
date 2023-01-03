# Problem
I want to idenfity recent source code files that use a particular word or pattern.

# Solution
Use grep to search for source files containing lines that match a pattern.

```bash
$ ls -tr | grep -r "QUERY_WORD" ./some_subdirectory | head -n 5
```

# Discussion
* First sort files in descending order by modified time (`-tr`)
* Use recursive (`-r`) grep pattern match in some_subdirectory
* Limit to most top 5 results (most recent 5 if you pipe sorted list of files earlier)
