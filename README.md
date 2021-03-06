# Eddie

A take on @vzhz's wonderful [Friendly Terminal](https://github.com/vzhz/friendly_terminal) but with a [Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) & Douglas Adams twist:

* Why, you might/may ask? as a reply one might say: Well then i guess this is not for you!

* Eddie is the shipboard computer on the starship Heart of Gold. Like every other system on the spaceship, it has a Sirius Cybernetics Corporation Genuine People Personality. Thus, Eddie is over-excitable, quite talkative, over-enthused and extremely ingratiating, or alternatively a coddling, school matron-type as a back-up personality. _([Wikipedia](https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Eddie))_

* Forty-two, said Deep Thought, with infinite majesty and calm

## To sum things up a bit

## Here's a preview

![eddie terminal preview](./eddie-terminal-preview.png "why yes that is tea")

## Installation

## 1. Clone this repo into your directory of choice

You may choose to place these files in your home folder, or any other. Navigate to the desired parent location and run

```git
git clone git@github.com:2lach/eddie-terminal.git eddie
```

_Make note of the file paths for `randline.py` (this is the main script) and `greetings.txt`. (this is were quotes are stored)_

## 2. Add the paths to your .*profile, or .*rc file

This will run the python file when you open a new terminal. Add the following code using your preferred text editor:

```bash
# run friendly terminal greeting
python3 /[PATH]/[TO]/[FILE]/eddie/randline.py /[PATH]/[TO]/[FILE]/eddie/greetings.txt [NAME]
```

```bash
newLine="\n"
description="# Friendly terminal greeting with messages from The Hitchhiker's Guide"
command="source ${PWD}/greeting-from-eddie.sh"

echo $newLine $description $newLine $command >> ~/.bashrc
```

### 3. Or while in this repo

```bash
echo "${PWD}/randline.py ${PWD}/greetings.txt $USER" >> ./greeting-from-eddie.sh
echo "\nsource ${PWD}/greeting-from-eddie.sh" >> ~/.your_rc
```

## 4. Source .bashrc or open a new terminal

Eddie is now installed and to be polite and stuff

## Optionally, edit Eddie's greetings

Add your favorite _Guide_ quotes, or other changes in Eddie's personality in `greetings.txt`.

---

## Changes

for the latest features you can look in the [changelog](./changelog.md)

## Contributing

We welcome your contributions in pretty much any form.

**Want to make your own modifications and share what you've done?** Fork & get started on a pull request. ([This repo](https://github.com/firstcontributions/first-contributions) has a step-by-step guide to for using Github as a first-time contributor).

## License

Eddie Terminal maintains [the MIT license](https://github.com/2lach/eddie-terminal/blob/master/LICENSE.txt).


<!--
https://github.com/damofthemoon/zsh-quotify/blob/master/quotify.coding.zsh
https://github.com/oldratlee/hacker-quotes/blob/master/hacker-quotes.plugin.zsh

-->
