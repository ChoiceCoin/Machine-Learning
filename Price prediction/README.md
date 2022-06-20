# Cryptocurrency Prediction Program

This is a cryptocurrency price prediction program using Python's keras module and

Tensorflow.

## Use

To execute, do:

```bash

$ python main.py [-s, --seed]

```

--s or --seed is an int of the seed desired to use, if ignored, it defaults to 123

After some time, this _should_ display:

```text

Using [Tensorflow/Theano] backend.

prediction coins by Lachi Balabanski

``` 

The backend used by the program is whichever you have installed or keras prefers, namely Tensorflow and Theano.

Next, the program will prompt you for the cryptocurrency abbreviation and the length of time to train from. __It is important to note:__ The larger dataset the program has, the better predictions it will be able to make.

The program will then show a matplotlib graph of the history of the coin that it is training from. This is a sample of the bitcoin graph for a month:

![BTC_graph](https://github.com/Temitopeishola/Hackathon/blob/main/btc_sample.png)

Following that, the program will display another matplotlib generated graph of its

predictions, similar to the one above, but with "Predictions" instead of "History"

in its title.

## Useful Information

It is important to note that upon the first use, a new folder called 

"\_\_pycache\_\_" will be created. This folder contains a compressed version

of the _genData.py_ file.

Secondly, if the program displays something along the lines of:

```text

	Your CPU supports instructions that this TensorFlow binary was not compiled to use:

```

This means that your CPU has special operators that tensorflow could, but did not, use. 
