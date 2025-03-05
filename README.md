[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18523592)
# 5.01-Intro-To-Dictionaries

## Internet Slang

Write a program that uses a dictionary to offer users the meanings of common (appropriate for school) internet abbreviations.

The program should include a dictionary, `internet_slang` which stores items in a key: value pair format: the abbreviation will be the key and the definition the value. Then it will prompt the user to enter an internet abbreviation they would like explained. If the requested abbreviation is in the program's dictionary (use the **in** keyword with an `if` statement to test this), then it prints out the definition. If the abbreviation is not in the dictionary, the program prints an apologetic message saying that it could not find a definition.

### Example Ouput

```
What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What word would you like to look up?
```

### Bonus

Extend the program with any of these features:
* the user can update the definitions (values) for existing abbreviations in the dictionary
* the user can add new abbreviations (keys) and provide the definitions (values)
* the user can delete entries (key: value pairs) from the dictionary
* the user can get the entire dictionary printed (in a nice looking format) to the screen

Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) about dictionaries and the [advanced Python documentation about dictionaries](https://docs.python.org/3/library/stdtypes.html#typesmapping).

