## In Short: It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module

For most practical purposes, you can think of the conditional block that you open with `if __name__ == "__main__"` as a way to store code that should only run when your file is executed as a script.

You'll see what that means in a moment. For now, say you have the following file:

```python linenums="1"
# echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
```

In this example, you define a function, `echo()`, that mimics a real-world echo by gradually printing fewer and fewer of the final letters of the input text.

Below that, in lines 10 to 12, you use the `if __name__ == "__main__"` idiom. This code starts with the conditional statement `if __name__ == "__main__"` in line 10. In the indented lines, 11 and 12, you then collect user input and call `echo()` with that input. These two lines will execute when you run `echo.py` as a script from your command line:

```console
$ python echo.py
Yell something at a mountain: HELLOOOO ECHOOOOOOOOOO
ooo
oo
o
.
```

When you run the file as a script by passing the file object to your Python interpreter, the expression `__name__ == "__main__"` returns `True`. The code block under `if` then runs, so Python collects user input and calls `echo()`.

Try it out yourself! You can download all the code files that you'll use in this tutorial from the link below:

{% optin "if-name-main-python-code" %}

At the same time, if you import `echo()` in another module or a console session, then the nested code won't run:

```pycon
>>> from echo import echo
>>> print(echo("Please help me I'm stuck on a mountain"))
ain
in
n
.
```

In this case, you want to use `echo()` in the context of another script or interpreter session, so you won't need to collect user input. Running `input()` would mess with your code by producing a side effect when importing `echo`.

When you nest the code that's specific to the script usage of your file under the `if __name__ == "__main__"` idiom, then you avoid running code that's irrelevant for imported modules.

Nesting code under `if __name__ == "__main__"` allows you to cater to different use cases:

- **Script:** When run as a script, your code prompts the user for input, calls `echo()`, and prints the result.
- **Module:** When you import `echo` as a module, then `echo()` gets defined, but no code executes. You provide `echo()` to the main code session without any side effects.

By implementing the `if __name__ == "__main__"` idiom in your code, you set up an additional entry point that allows you to use `echo()` right from the command line.

There you go! You've now covered the most important information about this topic. Still, there's more to find out, and there are some subtleties that can help you build a deeper understanding of this code specifically and Python more generally.

Read on to learn more about [the name-main idiom](#is-the-idiom-boilerplate-code-that-should-be-simplified), as this tutorial will refer to it for short.
