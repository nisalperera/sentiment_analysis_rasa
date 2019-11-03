# sentiment_analysis_rasa

Note: suggested to use python 3.6. python 3.7 version might create some runtime errors.

run "pip install -r requirements.txt" to install required packages.
run "python init.py" to start training
for predictions use method named "chat" in the package "sentiment_analysis" and parse the text to be predicted as the parameter. This will return the predicted emotion.

Note: Please do not change data.json file format. If you need to add training data add them to "DataSetForWorkersEmotions.txt" with tab seperated then run "python csvtojson".