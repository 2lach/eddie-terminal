# Eddie

A take on @vzhz's wonderful [Friendly Terminal](https://github.com/vzhz/friendly_terminal) with a [Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) spin:

> Eddie is the name of the shipboard computer on the starship Heart of Gold. Like every other system on the spaceship, it has a Sirius Cybernetics Corporation Genuine People Personality. Thus, Eddie is over-excitable, quite talkative, over-enthused and extremely ingratiating, or alternatively a coddling, school matron-type as a back-up personality. _([Wikipedia](https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Eddie))_

### And since I may not have gone where I intended to go, but I think I have ended up where I needed to be.

I found this repo and forked it from the lovely @victoriadrake.

# Preview

![Eddie's always ready to help.](https://github.com/2lach/eddie-terminal/blob/master/eddie-terminal-preview.png)

# Installation

Concise instructions below. View [original instructions at the parent repo.](https://github.com/vzhz/friendly_terminal)

## 1. Clone this repo into your directory of choice

You may choose to place these files in your home folder, or any other. Navigate to the desired parent location and run:

```
git clone https://github.com/2lach/eddie-terminal.git eddie
```

Make note of the file paths for `randline.py` and `greetings.txt`.

## 2. Add the paths to your .bash_profile, .bashrc

This will run the python file when you open a new terminal. Add the following code using your preferred text editor:

```
# run friendly terminal greeting
python3 /[PATH]/[TO]/[FILE]/eddie/randline.py /[PATH]/[TO]/[FILE]/eddie/greetings.txt [NAME]
```

### 3. Or

```
$ echo "\n${PWD}/randline.py ${PWD}/greetings.txt $USER >> greeting-from-eddie.sh"
```

```
$ echo "\n# Eddie-terminal greeting messages with a Hitchhiker's Guide \n source ${PWD}/greeting-from-eddie.sh" >> ~/.bashrc
```

## 4. Source .bashrc or open a new terminal

Eddie is now installed and ready to help!

## Optionally, edit Eddie's greetings

Add your favorite _Guide_ quotes, or change up Eddie's personality in `greetings.txt`.

---

## Contributing

We welcome your contributions in pretty much any form.

**Want to make your own modifications and share what you've done?** Fork & get started on a pull request. ([This repo](https://github.com/firstcontributions/first-contributions) has a step-by-step guide to for using Github as a first-time contributor).

## License

Eddie Terminal maintains [the MIT license](https://github.com/victoriadrake/eddie-terminal/blob/master/LICENSE.txt).

```

```
