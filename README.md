# Codenames

#### To write your own clues: 
Find cell with this line: 
generate_n_examples(1000, bert_embedding, 'cosine', 0.00003788)
This will write board + clues to a txt file that can be run to collect data. 

#### To play around with parameters: 
Comment out line generate_n_examples in same cell as above and uncomment the lines below and change parameters, etc. 

#### To collect data: 
Run the python file data_collector.py (make sure that examples.txt is in the folder). 
Instructions: 
- Either choose a word that you think is a good clue, type in your own and press enter or hit pass. 
- VERY IMPORTANT: To stop collecting, hit the QUIT button. Don’t hit x. Doesn’t work for some tkinter reason. 
- You can pick up where you left off by just running data_collector.py again. 
