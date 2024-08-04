# Homographic Attack to Generate Adversaries in Python

- basic code to begin my Python journey, includes file handling.
- main working: flip target letter with its corresponding cyrillic alphabet thus generating adversarial words.

## Steps to RUN the code:
- 1. download all files in one folder.
- 2. Do the following in VS-Code terminal
- - pip install NLTK
- - pip install spacy
- - python -m spacy download en_core_web_lg
<br>

- 3. Run the 'main.py' file
- 4. use words from the dictionary at random to test other inputs. (there's a purpose to the dictionary and using words outside the dictionary may give wrong results <refer note below>)

## What are Adversarial Examples?
- Adversarial examples are inputs designed to intentionally fool machine learning models, particularly neural networks.
- Adversarial examples are created by making subtle, often imperceptible changes to legitimate inputs.

## What is Homographic Attak?
- A homographic attack is a type of deception where attackers use visually similar but distinct characters to register a malicious domain that can be easily mistaken for a legitimate one. <br>
<t> EXAMPLE: g00gle.com instead of google.com

## How Homographic Attacks Work 
1.  <b>Identify  Homoglyphs </b>:  Create  a  mapping  of  characters  to  their  homoglyphs.  For 
example, the Latin character 'r' has a visually similar counterpart in Cyrillic 'г' (Unicode 
U+0433). 
2.  Select Critical Characters: Use gradient-based methods to identify which characters in 
the input text are most influential in the model's decision-making process. <b>(not implemented in my code) </b>
3.  Apply Homoglyph Substitution: Replace the critical characters with their homoglyphs 
to create an adversarial example. 
4.  Evaluate  the  Impact:  Check  if  the  adversarial  example  fools  the  text  classification model. 

- <u> Refer file name 'crillic_pairs.txt' for the defined pairs </u>

## NOTE:
- Here, since I am only starting my career in python, I have simply declared if input matches any word in my dictionary, then it's not spam. ALL OTHER WORDS regardless of cyrillic will be declared as spam!

# END THANKS!