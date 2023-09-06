## English-2-Hinglish-Translator
This is a simple Hinglish translator that can translate English sentences to Hindi and Hinglish.

## Overview
This code is a simple English to Hinglish translator. It uses the Huggingface Transformers library to translate English sentences into Hindi, and then uses a custom function to transliterate the Hindi text into Hinglish.

## Code Explanation
The code is divided into three functions:

hindiToHinglish(): This function converts a Hindi sentence into Hinglish by replacing the Hindi characters with their corresponding English transliterations.
englishToHindi(): This function converts an English sentence into Hindi using the Huggingface Transformers library.
get_user_input(): This function prompts the user to enter an English sentence, and returns the sentence as a string.
The main function of the code is englishToHinglish(). This function first calls the englishToHindi() function to translate the English sentence into Hindi. It then calls the hindiToHinglish() function to transliterate the Hindi text into Hinglish. Finally, it prints the translated and transliterated sentences to the console.

## Usage of Transformers
The Huggingface Transformers library is a popular library for natural language processing tasks. It provides a number of pre-trained models for tasks such as machine translation, text summarization, and question answering.

In this code, we use the AutoModelForSeq2SeqLM class from the Transformers library to translate English sentences into Hindi. This class is pre-trained on a large dataset of parallel English-Hindi text.

## Table of Contents
Getting Started
License
Contribution

## Getting Started
To get started with this code, you will need to install the following dependencies:

Python 3.8+
Pip
Huggingface Transformers
You can install the dependencies using the following command:

pip install -r requirements.txt
Prerequisites
To use this code, you will need to have some basic knowledge of Python and the Huggingface Transformers library.

## Installation
To install this code, you can clone the repository from GitHub:

git clone https://github.com/VAISHNAVIV27/English-2-Hinglish-Translator.git
Then, change directory to the project folder and install the dependencies:

cd English-2-Hinglish-Translatorr
pip install -r requirements.txt


## Contributing

If you would like to contribute to the Hinglish Translator, please fork the repository and submit a pull request.

## License

The Hinglish Translator is released under the MIT License.
