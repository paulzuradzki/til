### Term-Frequency Inverted Document Frequency Search Implemented with `scikit-learn`

TF-IDF is implemented using the `scikit-learn` library's TfidfVectorizer and cosine_similarity utilities. 

The basic algorithms can be implemented from scratch with reasonable effort, but `scikit-learn` gives us optimizations (e.g., use of sparse matrices and numpy).


### Program
```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict

query = "news about presidential campaign"
documents = ['news about',
             'news about organic food campaign',
             'news of presidential campaign',
             'news of presidential campaign presidential candidate',
             'news of organic food campaign campaign campaign campaign',
             'news about presidential campaign']

# one list with query as first item
query_and_docs = [query] + documents



# `transformed` is a "CSR" compressed sparse row vector by default
# convert to array to get TFIDF weights for each term
# vectorizer.get_feature_names_out() returns the terms in the vocabulary which align with transformed.indices (integers)
vectorizer = TfidfVectorizer()
transformed = vectorizer.fit_transform(query_and_docs)
tfidf_as_df = pd.DataFrame(data=transformed.toarray(), 
                           columns=vectorizer.get_feature_names_out())
tfidf_as_df.index = tfidf_as_df.index - 1
tfidf_as_df.index.name = 'document_id'

#########################
# display input / output
#########################

print(f"query: {query}")
print("documents:")
for idx, doc in enumerate(documents): 
    print('\t', idx, doc)

# Display enumerated features (terms and their "ID")
# Display TFIDF matrix. Each row is a document vector where the column corresponds to a term. Each value is a weight.
# We can then compare document vectors to each other with similarity metric (e.g., cosine) and rank via sort
print("\n(index, feature_name)", tuple(enumerate(vectorizer.get_feature_names_out())), '', sep="\n")

print("TFIDF MATRIX")
print("document_id=-1 is the query")
print(tfidf_as_df.round(3).replace(0, '').to_markdown())

query_weights = transformed[0]
document_weights_all = transformed[1:]
scores = cosine_similarity(query_weights, document_weights_all)

# sort descending by score/weight
scores = sorted(list(enumerate(scores[0])), key=lambda x: x[1], reverse=True)

# adding document so we have more than just the document index
scores = [(doc_index, documents[doc_index], weight) for doc_index, weight in scores]
scores_df = pd.DataFrame(scores, columns=['document_id', 'document', 'weight'])

print("\nRANKED")
print(scores_df.to_markdown(index=False))
```

### Displayed Output
```
query: news about presidential campaign
documents:
	 0 news about
	 1 news about organic food campaign
	 2 news of presidential campaign
	 3 news of presidential campaign presidential candidate
	 4 news of organic food campaign campaign campaign campaign
	 5 news about presidential campaign

(index, feature_name)
((0, 'about'), (1, 'campaign'), (2, 'candidate'), (3, 'food'), (4, 'news'), (5, 'of'), (6, 'organic'), (7, 'presidential'))

TFIDF MATRIX
document_id=-1 is the query
|   document_id | about   | campaign   | candidate   | food   |   news | of    | organic   | presidential   |
|--------------:|:--------|:-----------|:------------|:-------|-------:|:------|:----------|:---------------|
|            -1 | 0.572   | 0.441      |             |        |  0.389 |       |           | 0.572          |
|             0 | 0.827   |            |             |        |  0.562 |       |           |                |
|             1 | 0.419   | 0.323      |             | 0.565  |  0.285 |       | 0.565     |                |
|             2 |         | 0.419      |             |        |  0.37  | 0.626 |           | 0.544          |
|             3 |         | 0.257      | 0.541       |        |  0.227 | 0.384 |           | 0.666          |
|             4 |         | 0.798      |             | 0.349  |  0.176 | 0.298 | 0.349     |                |
|             5 | 0.572   | 0.441      |             |        |  0.389 |       |           | 0.572          |

RANKED
|   document_id | document                                                 |   weight |
|--------------:|:---------------------------------------------------------|---------:|
|             5 | news about presidential campaign                         | 1        |
|             0 | news about                                               | 0.691693 |
|             2 | news of presidential campaign                            | 0.639622 |
|             3 | news of presidential campaign presidential candidate     | 0.582224 |
|             1 | news about organic food campaign                         | 0.493316 |
|             4 | news of organic food campaign campaign campaign campaign | 0.420465 |
```

### References
* https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
* https://www.freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3/
