theme: Ostrich, 3
footer: `🐦 wolf4earth | saschawolf.me`

# [fit] Beyond the SPA
## [fit] __Interactive web apps without writing JS__

---

<!-- ## In the
# __distant__
## past -->
## A __long__ time ago ...

---

# [fit] <picture: static web pages>
# Web __1.0__

^
- everything was static
- nothing reacted
- nothing happened

---

# [fit] <picture: early earth lifeforms>

^
real footage of users

---

# [fit] <gif: interactive web page>
# Web __2.0__

^
- suddenly things get moving!
- interactivity!!!

---

# [fit] <picture: web 3.0 - machine interaction>
# Web __3.0__

^
Machines understand the data? TODO: VERIFY
not relevant for us

---

```js
$("#submit").onClick(...)
```

<look for funny jQuery snippet>

---

# [fit] <screenshot: jQuery for addition screen from SO>

---

# [fit] <logos: angular, react, vue, etc. - each slide one more>

---

# [fit] <screenshot: the help-me-choose-my-framework website>

^
And that's not even considering:

---

# [fit] <video: number of packages on npm growing over the years>

^
- state handling
- routing (if SPA)
- thousands of other packages

^
Hashtag: JS Fatigue
Slide on Webpack?

---

## What about the
# __backend__?

^
- API documentation
- Websockets for server-triggered updates

---

> Is all of this *really* necessary?
-- An overwealmed dev

<!-- TODO: Check if spelling correct! -->

^
- Huge additional tech stack
- Loads of complexity

---

# [fit] <quote on complexity?>

---

# [fit] <graph: static to dynamic>

---

# [fit] <graph: static to dynamic - annotated with static stuff>

---

# [fit] <graph: static to dynamic - annotated with static and dynamic stuff>

^
Sometimes it makes sense: Google Docs, Maps, Games, etc.

---

# [fit] <graph: static to dynamic - what about the middle?>

^
Examples:
- Dashboards
- Trello, Fun Retro
- Pushing updates from the server

---

## Isn't there an __alternative__?

---

# [fit] <picture: phoenix live view>

---

# [fit] <gif: demo time>

^
- LiveRetro
- Flappy Bird
- TODO: More demos

---

> How does this work?
-- Probably you right now

---

# [fit] <graph: lifecycle - request, render, socket>

^
Initial render means it's super SEO friendly

---

# [fit] <graph: lifecycle - highlight socket>

---

# __Change__ Tracking

---

# [fit] <screenshot: card of LiveView>

---
[.code-highlight: 1-11]
[.code-highlight: 2, 5, 7]
[.code-highlight: 1, 3-4, 6, 8-11]

<!-- TODO: Check if there is highlighting for eex -->

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

# [fit] <screenshot: card with changed text>

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

## [fit] What about updating
# __the DOM__

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

## What about
# __nested__
## views?

---

```javascript
{
  0: {
    0: "foo",
    1: "bar",
    // ...
  }
}
```

---

### Thank you for
## __listening__

---

# __Questions?__