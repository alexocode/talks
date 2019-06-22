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
[.code-highlight: 1-10]
[.code-highlight: 2-3, 5]
[.code-highlight: 1, 4, 6-10]

<!-- TODO: Check if there is highlighting for eex -->

```html
<item>
  <div class="card <%= color_for(@type) %> darken-1">
    <a href="#" phx-click="edit" phx-value="<%= @id %>">
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

<!-- TODO: Verify data structure -->

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

<!-- TODO: Verify data structure -->

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

---

### Thank you for
## __listening__

---

# __Questions?__