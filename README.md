# fact-checker
We are trying to check covid-19 facts against verified websites like WHO, CDC, etc.

Users can enter statements regarding covid-19 on our website. We then run the statement through a Google custom search over some trusted websites to get relevant links. 
This is done in the test_search_engine.py file.

Then we score these results using sentence similarity based on Bert embeddings (this function is available in the utils.py file).

Lastly, we display the verdict (whether or not the fact is true or false) and the citations for the articles we used to get to this conclusion. 

To check a query using test_search_engine.py, use the following format:

```
python test_search_engine.py 'covid-19 is caused by a virus'
```
You will see either True, False or inconclusive in the result.

We can also check the fact-check website from Google to see if their results are relevant. This can be done using the test_fact_check_api.py file as follows:

```
python test_fact_check_api.py 'covid-19 is caused by a virus'
```


