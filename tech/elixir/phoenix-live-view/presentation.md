theme: Ostrich, 3
build-lists: true
footer: `BetterDoc | 🐦 wolf4earth | saschawolf.me`

# [fit] Beyond the SPA
## [fit] __Interactive web apps without writing JS__

---

<!-- ## In the
# __distant__
## past -->
## A __long__ time ago ...

^
In an web far away ...

---

![](images/early-lifeforms.jpeg)

^
The early lifeforms on earth were using something called:

---
[.background-color: #476DA1]

![inline](images/web1.png)

^
WEB 1.0:
- everything was static
- read some text, clicked some links
- nothing happened

---

![inline](images/interactivity.gif)

---

![inline](images/jquery-animation.gif)

^
Things got moving!

---

```javascript
$("#search-submit").click(function() {
  $("#search form").submit()
});
```

^
And some awesome code was written!

^
We used jQuery for everything!

---
[.background-color: #FFFFFF]
[.footer-style: #000000]

![inline](images/so-jquery.gif)

^
From here web development evolved further

---
[.background-color: #FFFFFF]
[.footer-style: #000000]

![inline](images/evolving-no-loop.gif)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/1.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/2.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/3.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/4.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/5.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/6.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/7.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/8.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/9.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/frameworks/10.png)

^
There is even a website to help you decide

---
[.footer: ]

![](images/frameworks/website-decision-help.png)

^
And that's not even considering:

---
[.background-color: #ffffff]
[.footer-style: #000000]
[.footer: `source: http://www.modulecounts.com/`]

![inline](images/packages-over-time.png)

^
- state handling
- routing (if SPA)
- thousands of other packages

---
# #__JS__Fatigue

^
And the fun only began:

---

## What about the
# __backend__?

^
- API documentation
- Websockets for server-triggered updates

---

> Is all of this *really* necessary?
-- An overwhelmed dev

^
- Huge additional tech stack
- Loads of complexity

---

> Simplicity is prerequisite for reliability.
-- E. W. Dijkstra

---

> I hate code, and I want as little of it as possible in our product.
-- Jack Diederich

---
[.background-color: #ffffff]
[.footer-style: #000000]

![](images/static-to-dynamic/1.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![](images/static-to-dynamic/2.png)

---
[.background-color: #ffffff]
[.footer-style: #000000]

![](images/static-to-dynamic/3.png)

^
Games too

---
[.background-color: #ffffff]
[.footer-style: #000000]

![](images/static-to-dynamic/4.png)

^
Throw jQuery on it

---
[.background-color: #ffffff]
[.footer-style: #000000]

![](images/static-to-dynamic/5.png)

^
Examples:
- Dashboards
- Trello, Fun Retro
- Pushing updates from the server

^
Do you really wanna use React for this?

---

## Isn't there an __alternative__?

^
There might be ...

---
[.background-color: #000000]

![](images/phoenix-live-view.png)

# __Phoenix__
# Live View

---
[.background-color: #000000]

# Demo

![](images/excited.gif)

^
- LiveRetro (pj \_learning\_/live_retro)
- Flappy Bird
- LiveView Examples (pg elixir/phoenix_live_view_example)

---

```
$ wc -l ...
 37 lib/live_retro/board/board.ex
 13 lib/live_retro/board/card.ex
 39 lib/live_retro/board/registry.ex
 15 lib/live_retro/board/storage.ex
 20 lib/live_retro_web/controllers/board_controller.ex
 44 lib/live_retro_web/views/board_view.ex
 81 lib/live_retro_web/live/board_live.ex
249 total
```

^
The code I've actually written!

^
Other code: generated boilerplate, config ...

---

> How does this work?
-- Probably you right now

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/live-view/livecycle.png)

^
Initial render means it's super SEO friendly
Static is indexed faster, easier to control SEO

^
static/dynamic: we'll see what that means

---

# __Change__ Tracking

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/live-retro/card.png)

---
[.code-highlight: 1-11]
[.code-highlight: 2, 5, 7]
[.code-highlight: 1, 3-4, 6, 8-11]

```html
<item>
  <div class="card <%= color_for(@type) %> darken-1">
    <a href="#"
       phx-click="edit"
       phx-value="<%= @id %>">
      <div class="card-content white-text">
        <%= @text %>
      </div>
    </a>
  </div>
</item>
```

---
[.code-highlight: 1-11]
[.code-highlight: 2-4]

```javascript
{
  0: "red",
  1: "A0202252-7778-440A-A117-9C2476D418AF",
  2: "My great card!",
  "static": [
    "<item><div class=\"card ",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "\"><div class=\"card-content white-text\">",
    "</div></a></div></item>"
  ]
}
```

---
[.code-highlight: 2-4]
[.code-highlight: 5-10]

```javascript
{
  0: "red", // color_for(@type)
  1: "A0202252-7778-440A-A117-9C2476D418AF", // @id
  2: "My great card!", // @text
  "static": [
    "<item><div class=\"card ",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "\"><div class=\"card-content white-text\">",
    "</div></a></div></item>"
  ]
}
```

^
What happens when somebody changes the text of the card?

---
<!-- TODO: Verify data structure -->

```javascript
{ 2: "My changed card!" }
```

^
What happens on the client?

---
[.code-highlight: 4]

```javascript
{
  0: "red",
  1: "A0202252-7778-440A-A117-9C2476D418AF",
  2: "My changed card!",
  "static": [
    "<item><div class=\"card ",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "\"><div class=\"card-content white-text\">",
    "</div></a></div></item>"
  ]
}
```

^
Okay but how do we get from here to there:

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/live-retro/card-changed.png)

^
Surprisingly simple! It taskes this:

---
[.code-highlight: 1-11]
[.code-highlight: 2-4]
[.code-highlight: 5-10]

```javascript
{
  0: "red",
  1: "A0202252-7778-440A-A117-9C2476D418AF",
  2: "My changed card!",
  "static": [
    "<item><div class=\"card ",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "\"><div class=\"card-content white-text\">",
    "</div></a></div></item>"
  ]
}
```

^
Zips dynamic with static

---

```javascript
[
    "<item><div class=\"card ",
    "red",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "A0202252-7778-440A-A117-9C2476D418AF",
    "\"><div class=\"card-content white-text\">",
    "My great card!",
    "</div></a></div></item>"
]
```

---
[.code-highlight: 3, 5, 7]
[.code-highlight: 2, 4, 6, 8]

```javascript
[
    "<item><div class=\"card ",
    "red", // Index 0
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "A0202252-7778-440A-A117-9C2476D418AF", // Index 1
    "\"><div class=\"card-content white-text\">",
    "My great card!", // Index 2
    "</div></a></div></item>"
]
```

^
And now just "join"

---
[.code-highlight: 9]

```javascript
[
    "<item><div class=\"card ",
    "red",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "A0202252-7778-440A-A117-9C2476D418AF",
    "\"><div class=\"card-content white-text\">",
    "My great card!",
    "</div></a></div></item>"
].join("")
```

---

```html
<item>
  <div class="card red darken-1">
    <a href="#"
       phx-click="edit"
       phx-value="A0202252-7778-440A-A117-9C2476D418AF">
      <div class="card-content white-text">
        My changed card!
      </div>
    </a>
  </div>
</item>
```

---

## Isn't this __slow__?

^
This must be slow, right?

---

# `morph`__`dom`__ [^1]

[^1]: https://github.com/patrick-steele-idem/morphdom

^
morphdom updates the DOM smartly

---
[.code-highlight: 1-11]
[.code-highlight: 7]

```html
<item>
  <div class="card red darken-1">
    <a href="#"
       phx-click="edit"
       phx-value="A0202252-7778-440A-A117-9C2476D418AF">
      <div class="card-content white-text">
        My great card!
      </div>
    </a>
  </div>
</item>
```

---
[.code-highlight: 7]

```html
<item>
  <div class="card red darken-1">
    <a href="#"
       phx-click="edit"
       phx-value="A0202252-7778-440A-A117-9C2476D418AF">
      <div class="card-content white-text">
        My changed card!
      </div>
    </a>
  </div>
</item>
```

---

- Efficent change tracking
- SEO-friendly initial render
- Very small payloads
- Fast and simple DOM updates

^
Efficient on the: server, wire, client

^
A question might remain though

---

## But why
# __Elixir__?

^
Couldn't we just build this with X?
Yes we could, but Elixir is uniquely suited!

---

#### Why Elixir?
# Reason __1__

---

# __Phoenix__
# is _fast_

---
[.background-color: #ffffff]
[.footer-style: #000000]

![fit](images/live-retro/board.png)

---

```
[info] GET /board/decline-crouch-ordinary-sea-brain-round
[info] Sent 200 in 627µs
```

---

# `627`__`µs`__

---

# `0.627`__`ms`__

---

#### Why Elixir?
# Reason __2__

---

# __Phoenix__
# scales

---
[.background-color: #000000]
[.footer: ]

![](images/phoenix-2-million.png)

# Vertically*[^2]*

[^2]: https://phoenixframework.org/blog/the-road-to-2-million-websocket-connections

---
[.footer: ]

# Horizontally*[^3]*

[^3]: http://erlang.org/doc/reference_manual/distributed.html

^
Built-in distribution in the VM

^
To explain a little detour ...

^
You see, Elixir is ...

---

## __Standing__ on
## the __shoulders__
## of __giants__

---
# __BEAM__
##### <br/>

---
# __BEAM__
##### Erlang VM

---

![inline](images/beam-me-up.gif)

^
Let's BEAM some knowledge in our heads

---

## __Erlang__ was created
## at __Ericsson__ for
## __telephony switches__

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
## __Erlang__ started
## in __1987__

---

## It went
## __open-source__
## in __1998__

---

## __Battle-tested__
## in over __30 years__
## of __usage__

---

# __Actor__ Model

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

## Each __Live View__
## is a __separate__
## __process__

^
Processes:
- Websocket
- Web Request
- DB Connections
- State Machines

---

#### Why Elixir?
# Reason __3__

^
One huge benefit this brings is:

---

# __Isolation__

^
Okay, what do I mean by that

---

> Let it crash!
-- Old Erlang Wisdom

^
DEMO

---

# __Supervison__
# Trees

---
[.background-color: #ffffff]
[.footer-style: #000000]

![inline](images/live-retro/supervision-tree.png)

^
Actual screenshot: 5 tabs open

^
Other benefits - too much for this talk

---

![](images/tip-of-the-iceberg.jpeg)

^
- for-comprehensions: Static data only sent once
- Not limited to JSON
- Of course only one TechStack

---
## When to use __LiveView__?

- "Real-time" collaboration
- Admin Dashboards
- Autocompletion
- Multi-step forms
- And probably more

---
## When to __not__ use __LiveView__?

- Desktop-like (Google Docs, Maps ...)
- Offload Heavy computing
- Offline capabilities
- Zero latency
- And probably more

---

### Thank you for
## __listening__

---

# __Questions?__