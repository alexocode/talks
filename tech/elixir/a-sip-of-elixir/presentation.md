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
## _Elixir_[^1]
### we need to understand its
## _History_

[^1]: and the problems it tries to solve

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

^
Why? CPUs don't get much faster, instead multiple CPUs

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
# _Actor_ Model[^2]

[^2]: `Technically almost-actor (https://www.youtube.com/watch?v=_0m0_qtfzLs)`

^
Q: Familiarity

^
Why almost? Not quite as defined in papers etc.
Why? Because Erlang was designed without it's knowledge

---
[.background-color: #ffffff]
[.footer-style: #000000]
[.footer: `source: https://www.brianstorti.com/the-actor-model/`]

![inline](images/actor-model.png)

^
- Isolation (shared nothing)
- Message passing
- Sequential processing

^
When message arrives (one of):
- Create more actors
- Send messages to other actors
- Designate what to do with the next message = Mutate State

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

^
Syntax: Prolog-inspired
Not a bad language, but takes some getting used to
Old language which you notice

---
## ` `Ruby `       ` _Erlang_
![original](images/ruby-and-erlang.png)

^
Ruby = Developer productivity and happiness

^
Erlang = Powerful and battle-hardened concurrency

---
![](images/cant-we-have-both.gif)

^
Remember, Erlang runs in a VM

---
# _BEAM_

^
A VM; just like the JVM

---
```erlang
-module(greetings).
-export([hello/1]).

hello(Name) ->
    io:format("Hello ~s~n", [Name]).
```


---
```elixir
defmodule Greetings do
  def hello(name) do
    IO.puts("Hello #{name}")
  end
end
```

---
### _Ruby_
#### +
### _Erlang_
#### =
## **_Elixir_**

^
With the history out of the way, let's talk specifics

---
# **_Elixir_**

- Erlang compatibility
- developer happiness
- pattern-matching
- syntactic macro system

---
# _Erlang_ compatibily

^
What does that mean?

---
```erlang
-module(greetings).
-export([hello/1]).

hello(Name) ->
    io:format("Hello ~s~n", [Name]).
```

---
```elixir
defmodule Greetings do
  def hello(name) do
    :greetings.hello(name)
  end
end
```

^
A lot of Elixirs std just delegates to Erlang
Example: Enum.reverse

^
Not unlike the state of languages on the JVM

---
# _Developer_ Happiness

---
## _Great_ Tooling

- build tool `mix`
- code formatter
- unit testing framework
- first-class documentation
- and more ...

^
All maintained by the core team

^
Not gonna talk about `mix` and formatter

---
## Unit Testing Framework - _ExUnit_

[.code-highlight: all]
[.code-highlight: 6]
```elixir
defmodule GreetingsTest do
  use ExUnit.Case, async: true

  test "it greets friendly" do
    assert Greetings.hello("Lambda Cologne") ==
             "Hello Lambda Cologne!"
  end
end
```

^
`async: true` because code is pure

^
*Highlight change with laser: "!" at the end*

^
Test failure looks like this:

---
[.background-color: #191918]

## Unit Testing Framework - _ExUnit_
![inline](images/exunit-test-failure.png)

^
Tells us about the code, the left value, the right value etc.

^
"Knows" we used `==`: How?
Syntactic Macro System - `assert` is a macro

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