# Todoist Vocabulary to Anki Importer
> Retrieve a list of words from Todoist, translate them and then easily import them into Anki.

I use this simple script to streamline my Todoist to Anki workflow. Anytime I come across a foreign word, I add it as a
task in Todoist. Previously, I would then search for the translations of these words and then manually add them to Anki.
Instead I automated the whole process to save tons of time.


![](header.png)

## Installation

You need to install the following Python packages:

```sh
pip install dict.cc.py
pip install TodoistAPI
```

## Usage example

You need to create a new project in Todoist that will include all the words you want to translate. Now, when you across
any new word, just add it to this project. Once you have accumulated enough words you can start importing them into Anki.

For this you first need your Todoist REST API token. In the desktop app you can find the token if you go to
Settings -> Integrations -> API token.

Next, you need the internal ID of your Todoist vocabulary project. Open the *find_project.py*,
add your token at the top and change *my_project_name* to the name of your vocabulary project.
Hit run and you will get the project ID.

Then add the token and project ID to the *main.py*, change the source and destinations languages if necessary and execute
the script.

Now, you have a CSV file called *new_entries.csv*. Open Anki and press the Import File button at the bottom of the
start screen.


## Meta

Yanic Möller – [LinkedIn](https://linkedin.com/in/ymoeller) - [Github](https://github.com/yanicm/)

Distributed under the MIT license. See ``LICENSE`` for more information.

## Contributing

1. Fork it (<https://github.com/yanicm/todoist_vocabulary_to_anki/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
