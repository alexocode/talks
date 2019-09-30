theme: Poster, 1
build-lists: true
footer: _`BetterDoc | 🐦 wolf4earth | saschawolf.me`_

[.background-color: #1F233D]
[.header-strong: #1F223D]

## **l**A**i**_Sip_**lll.**
## of _Elixir_

---
![](images/a-sip.gif)

---
## What is *Elixir*?

---
> Elixir is a dynamic, functional language designed for building scalable and maintainable applications.
-- elixir-lang.org

^
Great sales pitch, right?

---
### To understand
## _Elixir_[^*]
### we need to understand its
## _History_

[^*]: and the problems it tries to solve

---
## The year is
# _2012_

---
# José _Valim_

^
- Well-known Rubyist
- Frustrated with the concurrency in Ruby

---
# José _Valim_
![](images/jose-valim.jpg)

` `

---
# José _Valim_
![](images/jose-valim.jpg)

__A well-known Rubyist__

- _Rails_ 44.2k ⭐ (Contributor)
- _Devise_ 20.2k ⭐
- _Simple Form_ 7.5k ⭐
- And more ...

^
He became frustrated with ...

---
# _Concurrency_

---
![](images/lookout.gif)

^
Compared different concurreny models

---
# _Erlang_

^
Running in ...

---
# _BEAM_
#### _Erlang_ VM

^
Concurrency: Using the ...

---
# _Actor_ Model

^
Q: Familiarity

---
[.background-color: #ffffff]
[.footer-style: #000000]
[.footer: `source: https://www.brianstorti.com/the-actor-model/`]

![inline](images/actor-model.png)

^
- Isolation (shared nothing)
- Message passing
- Sequential processing

---
## _Erlang_ was created
## at _Ericsson_ for
## _telephony switches_

---
- Distributed
- Fault-tolerant
- Soft real-time
- High-availability

^
- Light processes
- Hot-code reloading
- self-recovering

---
## Work on
## _Erlang_ started
## in _1987_

---
## It went
## _open-source_
## in _1998_

---
## _Battle-tested_
## in over _30 years_
## of _usage_

^
Sounds pretty good, right?

^
BUT ...

---
```erlang
-module(greetings).
-export([hello/1]).


hello(Name) ->
    io:format("Hello ~s~n", [Name]).
```

---
### _Ruby_
#### +
### _Erlang_
#### =
### _?_

---
![](images/cant-we-have-both.gif)

^
Remember, Erlang runs in a VM

---
# _BEAM_

---
### _Ruby_
#### +
### _Erlang_
#### =
## **_Elixir_**

---
```elixir
defmodule Greetings do
  def hello(name) do
    IO.puts("Hello #{name}")
  end
end
```

---
[.autoscale: true]

# Hero's Journey

1. The journey begins with the introduction of the Heroes in the Ordinary World, where
2. they are presented with the Call to Adventure.
3. Their initial reluctance may lead to Refusal of the Call, but they
4. receive encouragement from a Mentor to
5. cross over the Threshold and gain entry into the Special World.
6. There, they encounter Tests, Allies, and Enemies.
7. They Approach the Inmost Cave where
8. they must endure an Ordeal.
9. The Reward is seized and
10. they are pursued as they follow The Road Back to the Ordinary World.
11. They are transformed by the experience of a Resurrection and
12. return triumphant with the Elixir—an item of great value that will benefit the Ordinary World.

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