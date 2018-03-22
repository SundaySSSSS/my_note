# [转]emacs代码缩进解决方案

```
原文地址：http://www.emacswiki.org/emacs/IndentingC

设置空格代替tab缩进，并且tab宽度为四个空格，同时设置c代码中语句首字母与括号对齐，下面四句话可以解决

(setq default-tab-width 4)
(setq-default indent-tabs-mode nil)
(setq c-default-style "linux")
(setq c-basic-offset 4)

全选后，用C-M-\整理一下缩进就好了

下面是原文：
IndentingC
讨论

curly braces lead to anger, anger leads to fear, and fear leads to suffering
– kensanata on #emacs
See also: TurnAllIndentingOff

Contents
CC mode for C, C++, Java
Different Styles
C-like Automatic Style Input (casi)
Tabs Instead of Spaces
Automatic Indentation
Another form of Automatic Indentation
No Indentation
Long names
Automatic Offset Detection
Handling Uncommon File Extensions
Conditional Styles
Indenting Preprocessor Statements
More Complex Issues
CC mode for C, C++, Java
The CC modes (C, C++, Java, etc.) have their own manual, the CC mode manual. Read it. It’s good for you.

If you just want to change the indentation level, set ‘c-basic-offset’:

    (setq-default c-basic-offset 4)
Add it to your ~/.emacs.

You can also set it within Emacs: Options → Customize Emacs → Top-level Customization Group → Programming → Languages → C. Here, change ‘C
 Basic Offset’ and save for future sessions. This will only affect buffers opened after setting, not the ones already open.

Different Styles
Instead of just changing the basic offset, consider switching to a particular style. A style defines much more than just the basic offset. There are a number of predefined styles. Take a look at the variable ‘c-style-alist’ to see a list of them.

You probably don’t want the default style. This is how Emacs indents out of the box:

    if(foo)
      {
        bar++;
      }
That’s the “gnu” style. If you don’t want to indent the braces, add something like the following to your ~/.emacs:

    (setq c-default-style "linux"
          c-basic-offset 4)
When this is in effect, Emacs will indent like below instead:

    if(foo)
    {
        bar++;
    }
A lower-level way to achieve this is (c-set-offset
 'substatement-open 0), where substatement-open is the braces’ syntactic context. Press ‘C-c
 C-o’to see the syntax at point (and customize its indentation).

A partial list of the better known C styles:

“gnu”: The default style for GNU projects
“k&r”: What Kernighan and Ritchie, the authors of C used in their book
“bsd”: What BSD developers use, aka “Allman style” after Eric Allman.
“whitesmith”: Popularized by the examples that came with Whitesmiths C, an early commercial C compiler.
“stroustrup”: What Stroustrup, the author of C++ used in his book
“ellemtel”: Popular C++ coding standards as defined by “Programming in C++, Rules and Recommendations,” Erik Nyquist and Mats Henricson, Ellemtel
“linux”: What the Linux developers use for kernel development
“python”: What Python developers use for extension modules
“java”: The default style for java-mode (see below)
“user”: When you want to define your own style
See Indent style article on Wikipedia with examples how different predefined C styles looks like.

C-like Automatic Style Input (casi)
Casi allows you to tune the behavior of many keystrokes for every specified style in CC mode. For example, you can tell Emacs to insert a space (” “) when you type ‘(’, and delete this space when you type DEL while point is after a ‘(’, in a CC mode buffer and the style of the buffer is “gnu”, but keep the default behavior when the style is not “gnu”. This is useful for some cases, e.g. when you are used to “bsd” style, but have to write programs in “gnu” style, and you don’t want to change your key-pressing habit. Plus “c-auto-newline”, casi makes Emacs a more convenient tool of writing C/C++ programs, since it allows one to keep a single key-pressing habit to write programs in many different styles. For more information about casi, see http://sourceforge.net/projects/casi-mode.

Tabs Instead of Spaces
If you want to have it look like an “ordinary” editor in Emacs, use 8 instead of 4:

    (setq-default c-basic-offset 8
                  tab-width 8
                  indent-tabs-mode t)
But Emacs can do better! Emacs can save it with TabsInsteadOfSpaces, and on an ordinary editor the file will look as above, and still have Emacs show every tab as four spaces:

    (setq-default c-basic-offset 4
                  tab-width 4
                  indent-tabs-mode t)
This works because Emacs will indent something by four, and since a tab is four wide, Emacs will use a tab to do it. To convert existing code that uses spaces to using tabs, use M-x
 tabify or reindent the entire file (C-x
 h C-M-\). (However, see SmartTabs for a better way to do this.)

For the opposite, see NoTabs. For a discussion of this, see TabsAreEvil or http://my.erinet.com/~tschaef/cc-mode/description.html. To use tabs for indentation and spaces for alignment, see SmartTabs.

Automatic Indentation
Add the following to your ~/.emacs file. Whenever you type certain characters, a newline will be inserted automatically. Some like it, some hate it.

    (add-hook 'c-mode-common-hook '(lambda () (c-toggle-auto-state 1)))
If you like this you might also be interested in ‘c-toggle-hungry-state’, which will delete all characters until next non-whitespace when you delete whitespace.

Another form of Automatic Indentation
For people who don’t like automatic indentation, but don’t want to hit tab on every line, here’s another method:

    (define-key c-mode-base-map (kbd "RET") 'newline-and-indent)
This maps newline-and-indent (normally C-j) to the return key. It’s exactly equivalent to hitting tab after every time you hit return.

Note: In order to add this to your .emacs you must add `(require ‘cc-mode)’ if you don’t have it already.

No Indentation
    (require 'cc-mode)
    (add-to-list 'c-mode-common-hook
      (lambda () (setq c-syntactic-indentation nil)))
It only works in version 5.27 or later. The effect: Every line is just indented to the same level as the previous one, and TAB adjusts the indentation in steps specified by ‘c-basic-offset’.

Long names
When you have a long method name with long arguments, you would like to lay it out as follows:

  public void veryLongMethodNameHereWithArgs(
          String arg1,
          String arg2,
          int arg3)
Here’s how to do it, thanks to KnutForkalsrud and KaiGrossjohann:

    (defun my-indent-setup ()
      (c-set-offset 'arglist-intro '+))
    (add-hook 'java-mode-hook 'my-indent-setup)
Side node: Look at GlassesMode if you hate functionNamesLikeThis. --ErikBourget

A very cool thing to do is automatically switching to that behavior for long lines only.

  (defconst my-c-lineup-maximum-indent 30)
  (defun my-c-lineup-arglist (langelem)
    (let ((ret (c-lineup-arglist langelem)))
      (if (< (elt ret 0) my-c-lineup-maximum-indent)
          ret
        (save-excursion
          (goto-char (cdr langelem))
          (vector (+ (current-column) 8))))))
  (defun my-indent-setup ()
    (setcdr (assoc 'arglist-cont-nonempty c-offsets-alist)
     '(c-lineup-gcc-asm-reg my-c-lineup-arglist)))
– nschum

Automatic Offset Detection
To have Emacs transparently and non-intrusively choose the proper ‘c-basic-offset’ for every visited C source file, use `guess-offset.el’ from the ElispArea(Lisp:guess-offset.el). Works for C++ and Java code as well.

This is especially useful if you occasionally edit source files written by other people.

More information in the source commentary and the GuessOffset topic.

Handling Uncommon File Extensions
Add the following to your ~/.emacs file:

    (add-to-list 'auto-mode-alist '("\\.ext\\'" . c-mode))
Conditional Styles
The following sets Linux style only if the filename (or the directory) contains the string “linux” somewhere.

    (defun maybe-linux-style ()
      (when (and buffer-file-name
                 (string-match "linux" buffer-file-name))
        (c-set-style "Linux")))
    (add-hook 'c-mode-hook 'maybe-linux-style)
Metacity uses a ‘c-basic-offset’ of 2, instead of the 8 that the linux style uses. The following sets c-basic-offset to 2 if the filename has “metacity” in it somewhere:

   (defun maybe-metacity-offset ()
     (if (string-match "metacity" buffer-file-name)
       (setq c-basic-offset 2)))
   (add-hook 'c-mode-hook 'maybe-metacity-offset)
Or, if you prefer local file variables, then use a LocalVariables section in your source files.

Example:

    /* -*- c-file-style: "linux" -*- */
See also trick on CcMode (currently) to set the style according to the directory location.

Indenting Preprocessor Statements
You can try PpIndent if you want to indent your C Preprocessor (#ifdef, #else, etc…) statements.

More Complex Issues
Read the node Interactive Customization in the CC mode manual that came with Emacs. Here is a summary:

To change the indentation of a line, we need to see which syntactic components affect the offset calculations for that line. Hit ‘C-c
 C-s’ on the offending line. This yields something like this:

    ((substatement-open . 44))
so we know that to change the offset, we need to change the indentation for the ‘substatement-open’ syntactic symbol. To do this interactively, just hit ‘C-c
 C-o’ (‘c-set-offset’). This prompts you for the syntactic symbol to change, providing a reasonable default. In this case, the default is ‘substatement-open’, which is just the syntactic symbol we want to change!

After you hit return, CC Mode will then prompt you for the new offset value, with the old value as the default. Use the following symbols:

 +   `c-basic-offset' times 1
 -   `c-basic-offset' times -1
 ++  `c-basic-offset' times 2
 --  `c-basic-offset' times -2
 *   `c-basic-offset' times 0.5
 /   `c-basic-offset' times -0.5
To check your changes quickly, just hit ‘C-c
 C-q’ (‘c-indent-defun’) to reindent the entire function.

For more complicated examples, this may not always work. The general approach to take is to always start adjusting offsets for lines higher up in the file, then re-indent and see if any following lines need further adjustments.

The node Permanent Customization in the CC mode manual tells you how to make these changes permanent.

Here is a trivial example:

    (defun my-c-setup ()
      (c-set-offset 'substatement-open 0))
    (add-hook 'c-mode-hook 'my-c-setup)
Here is AaronL’s C-style, as an example. It has been commented for your convenience.

  (setq-default c-indent-tabs-mode t     ; Pressing TAB should cause indentation
                c-indent-level 4         ; A TAB is equivilent to four spaces
                c-argdecl-indent 0       ; Do not indent argument decl's extra
                c-tab-always-indent t
                backward-delete-function nil) ; DO NOT expand tabs when deleting
  (c-add-style "my-c-style" '((c-continued-statement-offset 4))) ; If a statement continues on the next line, indent the continuation by 4
  (defun my-c-mode-hook ()
    (c-set-style "my-c-style")
    (c-set-offset 'substatement-open '0) ; brackets should be at same indentation level as the statements they open
    (c-set-offset 'inline-open '+)
    (c-set-offset 'block-open '+)
    (c-set-offset 'brace-list-open '+)   ; all "opens" should be indented by the c-indent-level
    (c-set-offset 'case-label '+))       ; indent case labels by c-indent-level, too
  (add-hook 'c-mode-hook 'my-c-mode-hook)
  (add-hook 'c++-mode-hook 'my-c-mode-hook)
Here is a style that pretty much matches the observed style of Microsoft (R)’s C and C++ code:

 (c-add-style "microsoft"
              '("stroustrup"
                (c-offsets-alist
                 (innamespace . -)
                 (inline-open . 0)
                 (inher-cont . c-lineup-multi-inher)
                 (arglist-cont-nonempty . +)
                 (template-args-cont . +))))
 (setq c-default-style "microsoft")
Style for OpenBSD source code, also valid for OpenSSH and other BSD based OSs source.

 (c-add-style "openbsd"
              '("bsd"
                (indent-tabs-mode . t)
                (defun-block-intro . 8)
                (statement-block-intro . 8)
                (statement-case-intro . 8)
                (substatement-open . 4)
                (substatement . 8)
                (arglist-cont-nonempty . 4)
                (inclass . 8)
                (knr-argdecl-intro . 8)))
I’ve had a very hard time trying to customize indentation. I like the Java style overall, but there are a few things I really don’t like about it. One is that it wants to hang ‘if’ braces, another is that when I tell it not to, it wants to indent them, instead of keeping them in line with the ‘if’ statement.

I knew that c-add-style had a means of creating one style based on another one, but it was so poorly documented, I had no idea how to use it. Through trial and error (lots of error), I finally found the trick:

  (defun my-c-common-hook ()
    (progn
      (c-add-style "mine" '("java"
                            (c-basic-offset . 4)
                            (c-hanging-braces-alist
                             ((substatement-open)
                              (block-close . c-snug-do-while)
                              (extern-lang-open after)
                              (inexpr-class-open after)
                              (inexpr-class-close before)))
                            (c-offsets-alist
                             (substatement-open . 0))
                             ))
      (setq c-default-style "mine")
      (c-set-style "mine")
      ))
The errors I encountered getting to this point:

(set-variable c-default-style “mine”) doesn’t work. You have to use ‘setq’. Why? I don’t know.
(set-variable ‘c-default-style “mine”). Anyway, why not setq?
If using ‘customize’, you can’t set the default style to yours if you define yours in a hook, since yours isn’t known at the time the default style is used. The hook is called later.
Despite how things look, the variables you set when defining your style only override existing styles. This means you don’t have to define every offset if you just want to change one.
I hope this helps save someone some hair-out-pullage. It would have been handy for me if it had been documented somewhere.

Is there any way to have indent-region change this:

    if (x == 0) {
        // ...
    } else {
        // ...
    }
to this:

    if (x == 0) {
        // ...
    }
    else {
        // ...
    }
???

No. As the name says, it only changes the indention.
I wanted Tab to call indent-region if anything is selected, and c-indent-command if not. So, after a late irc.freenode.net#emacs session. Here’s what fledermaus, cgray and _sprintf came up with:

    ;;Setting Tab to indent region if anything is selected
    (defun tab-indents-region () (local-set-key [(tab)] 'fledermaus-maybe-tab))
    (add-hook 'c-mode-common-hook   'tab-indents-region)
    ;;fledermaus came up with this
    (defun fledermaus-maybe-tab ()
    (interactive)
    (if (and transient-mark-mode mark-active)
    (indent-region (region-beginning) (region-end) nil)
    (c-indent-command)))
transient-mark-mode is needed, as you see. Works very well :)

  - lurwas
You can also do indentation (and much more) with the indent program that almost everyone with Linux has. It can also fix things like moving the opening brace from “if (x == 0) {” to the next line and similar transformations. This is how I did it (with lots of help from the nice people in #emacs):

  (defun c-reformat-buffer()
    (interactive)
    (save-buffer)
    (setq sh-indent-command (concat
                             "indent -st -bad --blank-lines-after-procedures "
                             "-bli0 -i4 -l79 -ncs -npcs -nut -npsl -fca "
                             "-lc79 -fc1 -cli4 -bap -sob -ci4 -nlp "
                             buffer-file-name
                             )
          )
    (mark-whole-buffer)
    (universal-argument)
    (shell-command-on-region
     (point-min)
     (point-max)
     sh-indent-command
     (buffer-name)
     )
    (save-buffer)
    )
  (define-key c-mode-base-map [f7] 'c-reformat-buffer)
Unfortunately, when I use the function above I’ve got and stdin: is not a tty on the saved buffer :( – LeslieHarlleyWatter
I’d like Emacs(21) to do automagic reformatting/indenting of source code (C, C++, Perl). And it does, using ‘align-mode-rules-list” etc.), which contains:

  (c-assignment
         (regexp   . ,(concat "[^-=!^&*+<>/| \t\n]\\(\\s-*[-=!^&*+<>/|]*\\)"
                        "=\\(\\s-*\\)\\([^= \t\n]\\|$\\)"))
         (group    . (1 2))
         (justify  . t)
         (tab-stop . nil))
However, if I write some C++ like this:

 for (std::vector<int>::const_iterator iter = foo.begin(); iter != foo.end(); ++iter)
         int j = 3;
this will be reformatted as:

  for (std::vector<int>::const_iterator iter = foo.begin(); iter != foo.end(); ++iter)
                        int     j                                = 3;
Not what I want! Does any have the magic code to do the right thing with C++ as well? Thanks!
```
