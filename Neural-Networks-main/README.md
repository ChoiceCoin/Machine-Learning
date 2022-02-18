# Neural-Networks
This is a repository for Algomy. Algomy is an autonomous data processor and machine learning algorithm using neural networks to predict the future prices of digital assets. Algomy uses layered recurrent neural networks to predict shifts in the price of Algo based on historical price and other statistical factors. Algomy automatically aggregates data about digital assets from Yahoo Finance, generating an updated set every time it is trained. This eliminates the manual collection of data, thus making Algomy more computationally efficient. 

In its initial iteration, Algomy predicts the price of the Algorand native asset, ALGO. However, the Algomy model was built for interoperability across Algorand, Bitcoin, Ethereum, and Cardano. This iteration also provides additional financial asset information with osciilators and calculations pertinent to predicting price. Thus, Algomy informs investors in making decisions on a logical basis in addition to statistical analysis. This Repository includes various folders with software code, which are defined below as Files.

# Files

- The *Final_Deliverables* folder has the script used in our final submission and the software demo, along with the final results. 

- The *AlgoNet* folder has the code for the majority of our workflow, and includes intermediary results, code, and comments. 

- The *Dataset* folder contains all the data for which we applied the Algomy model to.

- The *results* folder includes several graphs of ALGO volatility predictions made by Algomy throughout the training process.

- The *data_collection* folder includes introductory scripts that parsed data from Yahoo Finance.

- The *pseudocode* folder has some scripts that detail an essential plan for data-analyis and statistical predictions.

- The *Paper* folder contains the research paper for this work.

- The *Patent_Application* folder contains the patent application for this work.

- The *Phase_III_Report* folder contains the report for Phase III of the Grant.

# Dependencies
- To run the code in the *Final_Deliverables* Folder, you first must have Python installed. Please download the latest version of Python, and create a virutal environment specifcally for this directory. Python Download: https://www.python.org/downloads/.
- Second, your Python virtual envrionment must have all of the packages listed in the *requirements.txt* file, which is also found in the *Final_Deliverables* folder. Note: All of the packages in the *requirements.txt* file may not be required. However, we strongly recommend downloading them as they depict our workflow and also open up alternative solutions. For example, parsing data from CoinMarketCap instead of Yahoo Finance may generate new or improved results.

# Run Steps
- To run the code in the *Final_Deliverables* folder, make sure you have all the dependcies installed as described above. 
- Access the directory where the *Final_Deliverables* folder is stored on your local machine.
- With your virutal environment activated, run the *script.py* executuable script. This can be done with "python run.py" on a Linux Terminal.
- Alternatively, access your Python Terminal, and then import the *algo_prediction* function from the *ALGO_Prediction.py* file by running "from ALGO_Prediction import algo_prediction". Then, simply run *algo_prediction* on the Python Terminal. 
- Note: You may need to configure your machine for TensorFlow. Read more on TensorFlow's website: https://www.tensorflow.org/install
- To get results for Algorand, Bitcoin, and Ethereum, run the *run.py* function.
- Edit the number of Epochs and drop-out rate as neccescary. Look at the *ALGO_Prediction.py* file under *Final_Deliverables* for more details.
- You should recieve several outputs through PyPlot: a graph of ALGO's past volatility, a prediction of future ALGO Volatility, and a graph detailing predictions of Algorand's future price.

# Demo
YouTube: https://www.youtube.com/watch?v=uc9HyV-7dzE

# Software License
Copyright Fortior Blockchain, LLLP 2021 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
