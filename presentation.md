theme: Next, 1

> git gud

---
[.build-lists: true]

# Agenda

1. Background
2. Basics
3. Advanced commands
4. Best Practices
5. Gems

---

# Background
## What is `Git`?

---

# VCS
## Version Control System

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
## GNU GPL2

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
# VS
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
## Day to day stuff

^
Who has more SVN than Git experience?
=> You'll be trouble

---

# `Git` is different

^
Not only "Distributed"
=> The way `Git` thinks about it's files

---

> The major difference [...] is the way Git thinks about its data.
-- Scott Chacon & Ben Straub [^ProGit]

^
A lot VCS: Deltas (what changed?)
Git: Snapshots

---

![100%](images/snapshots.png)

<!--         Version 1
        File A    -> A1 -> *A1* -> A2 -> *A2*
        File B    -> *B* -> *B* -> B1 -> B2
        File C    -> C1 ->  -> 
 -->

---

## Inline Images

When using the **[inline]** modifier, images automatically centre and fit to the available space.

![inline](http://deckset-assets.s3-website-us-east-1.amazonaws.com/colnago2.jpg)

---

![inline, left](http://deckset-assets.s3-website-us-east-1.amazonaws.com/colnago2.jpg)

Use **[inline, left]** or **[inline, right]** to move images around. With the text underneath like this, it is the simplest ways to add captions to images.

---

# Tables

With `:---:`, `---:` and `:---` you can center, right or right align the cell content.

  Header 1 |    Header 2   |   Header 3   |
-----------| :-----------: | -----------: |
Cell       |     _Cell_    |     *Cell*
Cell       |   **Cell**    |     __Cell__

[^ProGit]: https://git-scm.com/book/en/v2