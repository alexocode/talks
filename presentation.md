theme: Next, 1

# GIT GUD

---
[.build-lists: true]

# Agenda

1. Background
2. Basics
3. Advanced
4. Tips & Tricks
5. Best Practices

^
1. & 2. => Lecture
3. & 4. => Interactive
5. => Lecture

---

# Background
### What is `Git`?

^
Ask this question?

---

# VCS
### Version Control System

^
What does a VCS do?

---

> [...] a system that records changes to a file or set of files over time
-- Scott Chacon & Ben Straub [^ProGit]

---

## Version Control Systems

- `CVS`
- `Perforce`
- `SVN`
- `Mercurial`
- `Git`

^
Later: How they differ

---

# Open Source
### GNU GPL2

^
published under GNU General Public License version 2
^
Next Slide: What makes Git different from, for example, SVN

---

# Distributed

^
What does that mean? For this we have understand:

---

# Centralised
### VS
# Distributed

---

# Centralised

![100%](images/centralized.png)

^
- Central repository = Single source of truth
- Server/Client communication

^
Examples: SVN, CVS, Perforce

---

# Distributed

![80%](images/distributed.png)

^
- Each repository a full backup (with exceptions)
- Communication between repositories
- Possibel to do centralised approach

^
Examples: Git, Mercurial

---

# Basics

^
Who has more SVN than Git experience?
=> You'll be trouble

^
I could bore with commands, but you probably know those already.
Let's talk about how Git works internally => Helps a lot for advanced stuff
- Terminology
- Object model

---

# Expected Knowledge

- `add`
- `reset`
- `commit`
- `merge`

---

![150%](images/areas.png)

^
How to add changes? (Probably familiar with this)
Follow up: How does Git track changes?

---

## How does `Git` track changes?

---

# `Git` is different

^
Not only "Distributed"
=> The way `Git` thinks about it's files

---

> The major difference [...] is the way Git thinks about its data.
-- Scott Chacon & Ben Straub [^ProGit]

---

# Snapshots
## not
# Deltas

![150%](images/snapshots.png)

^
Deltas: What changed?
Snapshots: Current state

^
How does Git build this to a commit?

---

### *What is a*
# Commit

---

![150%](images/commit-and-tree.png)

^
Commit -> Tree -> Tree | BLOB
Commit: Tree + Parents + Metadata

^
Git is closer to a filesystem then to a classic VCS
Next slide: How does Git identify objects?

---

# SHA1

^
Hash built over all properties of the object (Commit => Author, Committer etc.)
You might have heard to never change commits after pushing: Hash changes when properties change

---

# Try it out!

---

```
$ git init git-playground
Initialized empty Git repository in ...

$ cd git-playground

$ echo 'Some random text' > my_file

$ git hash-object -w my_file
1a76b8a41993e2c667f5b191fb57abdab2102a8b

$ git cat-file -t 1a76b8a41993e2c667f5b191fb57abdab2102a8b
blob

$ git cat-file -p 1a76b8a41993e2c667f5b191fb57abdab2102a8b
Some random text
```

^
You can actually find the blob in .git/objects/1a/76b8a41993e2c667f5b191fb57abdab2102a8b
Git only uses the content; create an identical file and the hash will be the same

---

# How history is made
### `Git` history at least

![fit](images/log-graph.png)

---

![150%](images/commits-and-parents.png)

^
Each commit has a reference on it's parent => Single linked list
Not really single though ...

---

# Honour thy parent
### Navigate through history

^
Q: You want to remove the last commit, how?

---

# `^` and `~<N>`

```
$ git log --oneline -1 HEAD
810e72b Presentation - Basics: Add the ancestry operations slide

$ git log --oneline -1 HEAD^
85b332f Presentation - Basics: Git History

$ git log --oneline -1 HEAD^^
1a60452 Presentation: Reformat headlines

$ git log --oneline -1 HEAD~2
1a60452 Presentation: Reformat headlines
```

---

### *What is a*
# Branch

^
Q: Ask this!

---

# Let's take a look

<br/>

```
$ ls -l .git/refs/heads/
total 16
drwxr-xr-x  3 swolf  staff  96 Dec  1 14:58 catch-up
-rw-r--r--  1 swolf  staff  41 Sep  7 09:44 espec
-rw-r--r--  1 swolf  staff  41 Nov  6 16:30 master
drwxr-xr-x  3 swolf  staff  96 Jan 16 08:24 mentoring
drwxr-xr-x  3 swolf  staff  96 Jan 14 19:50 review
```

---

# Huh, `master` is a file ...

---

# I wonder what's in there ...

```
$ cat .git/refs/master
f3cb43e2601c54819928ee289f948234896e9cb8
```

---

# It's just a hash!

---

# Let's inspect the object

```
$ cat .git/refs/master | git cat-file --batch
f3cb43e2601c54819928ee289f948234896e9cb8 commit 523
tree 4e6897e11baef8fbf0382093dc160442e9c99f2b
parent c79a7bb4ef8a587c9264207f6f6715cb9fda8425
author Sascha Wolf <sascha.wolf@grandcentrix.net> 1509982143 +0100
committer Sascha Wolf <sascha.wolf@grandcentrix.net> 1509982216 +0100
gpgsig -----BEGIN PGP SIGNATURE-----

 iHUEABEIAB0WIQTQyMji07ff76Vkk26j80vFo8w6AAUCWgCACAAKCRCj80vFo8w6
 AFXDAQDrDWUgym7AuNIDL5Lb4dfgMGtA2DWWj4VqghOA2Vq/aAEAhJmh3vGbvLbu
 WeTc1BfojvsWPqdLp+1kEV7ZqcJMH1U=
 =F4z8
 -----END PGP SIGNATURE-----

Presentation: Add a template for the presentation
```

---

# What about `HEAD`?

^
Q: What do you think is HEAD?

---

<br/><br/><br/><br/>

```
$ cat .git/HEAD
ref: refs/heads/master

$ git checkout --detach master
...

$ cat .git/HEAD
f3cb43e2601c54819928ee289f948234896e9cb8
```

^
1. Reference onto a branch
2. Reference onto a commit (detached HEAD)

---

# Advanced
### From porcelain to plumbing

^
Porcelain: Clean CLI commands (like add, commit, reset)
Plumbing: Programmatically used low-level commands

---

## Clone workshop repository
### `git clone`
### `git@github.gcxi.de:swolf/git-workshop.git`

---

- (add|reset) patch
- rebase
- bisect

---

# `git bisect`
### The bug has to be here

---

# Best Practices

---

- Commit message
- Merging and rebasing
- Branching?

---

# Tables

With `:---:`, `---:` and `:---` you can center, right or right align the cell content.

  Header 1 |    Header 2   |   Header 3   |
-----------| :-----------: | -----------: |
Cell       |     _Cell_    |     *Cell*
Cell       |   **Cell**    |     __Cell__

[^ProGit]: https://git-scm.com/book/en/v2