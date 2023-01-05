# Today I Learned (TIL)
I log things that I learn or code snippets that I keep forgetting in this TIL collection.

This log also doubles as a lazy tech "blog". While I am the primary audience, I hope learning in public can offer utility to others.

### Categories
* [Python](#python)
* [Statistics and Machine Learning](#statistics-and-machine-learning)
* [SAS](#sas)
* [SQL](#sql)
* [C](#c)
* [Linux](#linux)
* [Git](#git)
* [Editors](#editors)
* [Resources](#resources)
* [Healthcare](#healthcare)
* [Other](#other)

---

### Python
- [Pandas rename column inside method chain](python/pandas-rename-columns-in-chain.md)
- [Pandas read_csv() from a file in ZIP URL](python/pandas_read_from_file_in_url_zip.md)
- [Multithreading - running asynchronous steps that wait for other events to complete](python/multithreading-wait-for-event.md)
- [How to share Jupyter Notebooks: gists, nbviewer, binder](python/how-to-share-jupyter-notebooks.md)
- [Connecting and Posting Objects to AWS S3](python/aws-s3-demo.md)
- [Catalog/inventory a file tree](python/file-tree-inventory.md)
- [Get file owner on Windows](python/get-file-owner-on-windows.md)
- [`Faker` for Mock Data](python/faker-for-mock-data.md)
- [TF-IDF and cosine similarity implementation with scikit-learn](python/tfidf-with-scikit-learn.md)
- [Installing a package from Git repository, zip file, or PyPI](python/installing-package-from-git-repo.md)
- [Adding to PYTHONPATH environment variable so Python can find modules](python/adding-to-pythonpath.md)
- [Convert markdown to HTML using `markdown` library](python/convert-markdown-to-html.md)
- [Set Comparison Statistics](python/set_comp_stats.md)
- [Flatten nested list with generator](python/flatten_nested_list.md)
- [Fill PDF Forms with PyPDF2](python/pdf-fill-forms.md)
- [Microsoft SQL Server (MSSQL) Connection String Example](python/mssql-config.md)
- [Decorators Example](python/decorators.md)
- [Python Excel Recipes with openpyxl and xlwings](python/openpyxl-xlwings-recipes.md)
- [Text-wrapping utility - `textwrapper`](python/textwrapper.md)
- [Why use classes?](python/why-use-classes.md)
- [Merge mp4 movie files with moviepy.editor](python/merge-mp4-movie-files.md)
- [Get media file metadata with TinyTag](python/tag-metadata-for-media-files-mp4.md)
- [API Usage Demo - FX Rates with Python Requests](python/api-usage-demo-fx-rates.md)
- [pandas - Pivot from columns to rows](python/pivot-rows-to-columns.md)
- [pandas - Display HTML representation of multiple dataframes](python/display-html-repr-jupyter.md)
- [Fast load to MSSQL / SQL Server from Python client](python/fast-load-to-sql-server.md)
- [Send Outlook emails with Win COM](python/send-outlook-emails-with-win-com.md)
- [Install packages from jupyter](python/install-packages-from-jupyter.md)
- [Process large data sets by chunk in pandas](python/pandas-process-data-by-chunk.md)
- [pandas - Idiomatic Pandas: chaining, piping, inspecting and assigning intermediate dataframes](python/idiomatic-pandas.md)
- [pandas - Summarize Frequency Counts with Percentages by Column](python/pandas-show-frequency-counts-with-percent.md)
- [Create timezones for Python datetime objects](python/handle-timezones-in-python.md)
- [OOP example](python/oop-demo.md)
- [OOP classes vs namedtuple](python/oop-namedtuple.py)
- [pandas - Concatenate strings from rows with GroupBy](python/pandas-concat-strings-from-rows-with-groupby.md)
- [Templating SQL from a pandas dataframe](python/jinja-sql-template-from-dataframe.md)
- [Dictionary un-packing and how to set default and override configurations](python/dictionary-unpacking-for-configs.md)
- [Selecting data with df.query()](python/pandas-df-query.md)
- [Flatten a dictionary](python/flatten-dict.md)
- [Iterative vs. Recursive Processes with Factorial](python/recursion-factorial.md)
- [Method chaining by returning self](python/method-chaining.md)
- [Flatten and remove pandas multi-index](python/flatten-multi-index.md)
- [pivot non-numeric rows to x columns](python/pivot-non-numeric-to-x-fields.md)
- [xlwings - add hyperlinks within a workbook](python/xl-add-hyperlinks-in-workbook.md)
- [pandas - miscellaneous](python/pandas-misc.md)
- [Heron's Method for Square Roots](python/square_root.md)
- [Traverse file tree recursively](python/traverse-files.md)
- [Python Custom Logical Sort with `sorted(iterable, key)`](python/python-custom-sort.md)
- [Troubleshooting package installation SSL error on corporate firewall](python/package-install-ssl-error.md)
- [Neatly print a collection using using f-string padding and alignment or `tabulate`](python/format_strings_alignment_and_padding.md)
- [pandas - value counts with percentages snippet](python/pandas_value_counts_with_percent.md)
- [pandas - read multiple sheets from Excel](python/pandas-read-multiple-sheets-from-excel.md)
- [Logging Format Snippet](python/logging-format-snippet.md)
- [LRU Cache decorator](python/lru_cache_demo.ipynb)
- [Set up IPython kernel for VS Code Jupyter Notebook support with a virtual environment](python/setup_ipython_kernel_for_vs_code.md)
- [pandas - display dataframe without index](python/pandas-display-without-index.md)
- [pandas - debug dataframe inside method chain](python/pandas-debug-df-inside-chain.md)

TODO
- TODO: Use of environment variables to protect credentials
- TODO: xlwings - read & write with Excel; split & merge sheets and workbooks
- TODO: matplotlib - subplots
- TODO: pandas pivoting methods and "named aggregations"
- TODO: mixin inheritance pattern
- TODO: class decorators
- TODO: decorator demo; timer and logger
- TODO: closure demo
- TODO: generator and generator expressions to process large file
- TODO: making a class support Python container and iteration protocols
- TODO: producer-consumer with and without queue
- TODO: threading, thread pool, locks, and parallel loops
- TODO: async demo with timer/simulated SQL (long query)
- TODO: add steps for PyPi prep; modifying setup.py, sdist and bdist_wheel; twine upload to test, etc.
- TODO: using pandas dataframe index for faster lookups and filtering
- TODO: include data files in packages with `pkgutil.get_data(package, resource)`

### Statistics and Machine Learning
* [Simple Linear Regression with Python `statsmodels` vs R `lm()` function](statistics-and-ml/slr-with-python-vs-r.md)
* [Linear Model Gotchas with Python vs R](statistics-and-ml/linear-model-gotchas-python-vs-r.md)
* TODO: scikit-learn pipelines
* TODO: scikit-learn column tranformers; feature unions of categorical and numeric
* TODO: scikit-learn subclassing and custom transformers (e.g., fasttext text classifier; customer transformations)
* TODO: compare linear regression in statsmodels vs scikit-learn
* TODO: compare FastText vs scikit-learn vs SpaCy for text classification
 
### SAS
- [Configuring SASPy for Windows](sas/configuring-saspy.md)
- [SAS Loops](sas/sas-loops.md)
- [Expand date spans to year-month view](sas/expand-dates.md)
- [Comparing terminology for similar concepts in Python and SAS](sas/sas-vs-python-semantics.md)
- [Disambiguating double ampersand and period in SAS macro variables](sas/sas-syntax-double&&-periods.md)
- [RSUBMIT and asynchronous SAS tasks](sas/rsubmit_async.md)
- [Export SAS to Excel example](sas/export-sas-to-excel.md)

### SQL
- [Programmatically generating SQL with Jinja Templates](sql/jinja_sql_demo.ipynb)
- [Connect to MS SQL Server with `pyodbc`](sql/sql-server-pyodbc-connection.md)
- [PostgeSQL connection from Python](sql/postgres-connect-with-python.md)
- [PostgreSQL fast bulk load via `copy from`](sql/fast-bulk-copy-postgres.md)
- TODO: pivot, unpivot

### C
- [Tic Tac Toe CLI](c/ttt.c)

### Linux
- TODO: systemd - deaemon process control config example
- [supervisorctl - daemon process control config example](linux/supervisorctl-config-example.md)
- [nginx sample web server config](linux/nginx-web-server-config.md)
- [Check processes](linux/check-processes.md)
- [Check listening ports](linux/check-listening-ports.md)
- [`nohup` - No Signal Hangup to run processes in background](linux/nohup.md)
- [Inspect and persist memory usage statistics with `vmstat`](linux/inspect_memory_usage.md)
- [Use grep to search for source files with lines containing words that match a pattern](linux/grep-search-for-source-files-with-lines-matching-pattern.md)

### Git
- [Show list of files with diffs since latest commit](git/show-latest-diffs.md)
- [Git snippets](git/git_snippets.md)

### Editors
- [VS Code - configuration for Anaconda prompt](editors/vs-code/settings-json.md)
- [How to Remote SSH with `sudo` privilege in VS Code](vs-code/remote-ssh-with-sudo.md)

### Resources
- [So You Want to Learn Python... (Python resource list)](python/so-you-want-to-learn-python.md)

### Presentations
* [Data Anonymization Fundamentals for Data Science](https://github.com/krasch/presentations/blob/master/pydata_Berlin_2016.pdf)

### Libraries
* Data cleaning
    * [PrettyPandas](https://github.com/HHammond/PrettyPandas)
    * [tabulate](https://github.com/astanin/python-tabulate)
    * [scrubadub](https://github.com/LeapBeyond/scrubadub)
    * [ftfy(fixes text for you)](https://github.com/rspeer/python-ftfy)

### Healthcare
* [CMS Risk Adjustment Files](healthcare/cms-risk-adjustment-files.md)
* [Implementing HEDIS Continuous Enrollment Requirements](healthcare/hedis_continuous_enrollment_reqs.md)

### Other
* [Make diagrams from markdown-like text with Mermaid](other/diagrams_with_mermaid.md)
