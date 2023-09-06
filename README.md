## English-2-Hinglish-Translator
This is a simple Hinglish translator that can translate English sentences to Hindi and Hinglish.

## Overview
This code is a simple English to Hinglish translator. It uses the Huggingface Transformers library to translate English sentences into Hindi, and then uses a custom function to transliterate the Hindi text into Hinglish.

## Code Explanation
The code is divided into three functions:

**hindiToHinglish()**: This function converts a Hindi sentence into Hinglish by replacing the Hindi characters with their corresponding English transliterations.
**englishToHindi()**: This function converts an English sentence into Hindi using the Huggingface Transformers library.
**get_user_input()**: This function prompts the user to enter an English sentence, and returns the sentence as a string.
The main function of the code is englishToHinglish(). This function first calls the englishToHindi() function to translate the English sentence into Hindi. It then calls the hindiToHinglish() function to transliterate the Hindi text into Hinglish. Finally, it prints the translated and transliterated sentences to the console.

Here we have 2 methods:
**Method 1**: This method first translates the English sentence into Hindi using the englishToHindi() function. Then, it transliterates the Hindi text into Hinglish using the hindiToHinglish() function.

**Method 2**: This method is similar to Method 1, but it allows the user to enter an English sentence interactively. The user enters the sentence in the console, and the code then translates it into Hinglish and prints the result to the console.

The main difference between the two methods is that Method 1 is a batch process, while Method 2 is an interactive process. Method 1 is better for translating a pre-defined set of English sentences, while Method 2 is better for translating an English sentence that you enter interactively.


## Usage of Transformers
The Huggingface Transformers library is a popular library for natural language processing tasks. It provides a number of pre-trained models for tasks such as machine translation, text summarization, and question answering.

In this code, we use the AutoModelForSeq2SeqLM class from the Transformers library to translate English sentences into Hindi. This class is pre-trained on a large dataset of parallel English-Hindi text.

## Table of Contents
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
To get started with this code, you will need to install the following dependencies:

## Prerequisites
- Python 3.8+
- Pip
- Huggingface Transformers
You can install the dependencies using the following command:


To use this code, you will need to have some basic knowledge of Python and the Huggingface Transformers library.

## Installation
To install this code, you can clone the repository from GitHub:
1. Clone this repository to your local machine. 
2. Navigate to the project directory.
3. Run the file -engtohing.py


## Output Image
![image](https://github.com/VAISHNAVIV27/English-2-Hinglish-Translator/assets/94777812/520ecba8-9c3c-4ed8-ac62-95f6fc5ed600)


## Contributing

If you would like to contribute to the Hinglish Translator, please fork the repository and submit a pull request.

## License

The Hinglish Translator is released under the MIT License.
