# Introduction
This sample app is meant to serve as a stand-alone user authentication module that can be extended or even plugged into your own project. It uses token based authentication (using **JWT**) and allows token refreshing.

# Installation

The prerequisites of this project are:
- Python 3
- pipenv

`pipenv` is the preferred way to create and manage virtual environment for your Python project. If you choose not to use virtual environment, you may install the dependencies manually. The dependencies are listed in the `Pipfile`.

To create a virtual environment, you may specify your preferred Python version first. For example, if you have Python 3.7 installed and wish to use it:

```
pipenv --python 3.7
```

Then, use `pipenv` to install the dependencies automatically into your virtual environment:

```
pipenv install
```

Now you are good to go.

# Running the app

After you have set up the app environment, you can run the app either from the IDE or via command line.

## Running from IDE

Make sure you used the virtual environment, which was created earlier, in the IDE. Then launch the `app.py` file as you would with any other apps.

## Running from command line

There are two options: 
1. activate the virtualenv then run the app
2. run the app from outside

For the first option:

```
pipenv shell    # create a shell in the virtualenv and use it
python app.py   # run the app
```

When you finish, you may exit the virtual environment like this:

```
exit
```

For the second approach:

```
pipenv run python app.py
```

The second approach is actually doing the same thing as the first one, but it's more convenient.

***troubleshoot*** If you have issue installing `marshmallow`, use the following command to install `marshmallow3`:

```
pipenv run pip install -U marshmallow --pre
``` 

*`marshmallow3` is currently in beta version, but we choose to stick to it since it introduces some major changes. Using `marshmallow2` will result in a lot of refactoring.*

 