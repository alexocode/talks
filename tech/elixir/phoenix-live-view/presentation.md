theme: Ostrich, 3
footer: `🐦 wolf4earth | saschawolf.me`

# [fit] Beyond the SPA
## [fit] __Interactive web apps without writing JS__

<!--
- Static vs dynamic web sites (left static, right google maps)
- "So we have to write JS"
- What technology to chose? React, Vue, Angular, Svelte ...
- There is even a website to help you choose
- What else to consider? State handling, routing etc.
- Webpack ...
- Communication between front- and backend: API definitions, websockets for realtime etc.
- Sometimes this complexity makes sense but sometimes ... (Admin Dashboard, Fun Retro)
- Enter Phoenix LiveView
- DEMO
- How does it work?
- Initial full render (SEO-friendly), socket connection afterwards
- Change Tracking via Live EEX, tech agnostic (static and dynamic)
- Efficient DOM updates (morphdom)
- Phoenix Sockets scale very well (2 mio connections, link to blogpost)
- OTP's actor model uniquely suited
- When to use: Anything with simple interactivity and realtime updates, MVPs, reduction of complexity
- When not to use: offline capability, lots of "client-side" logic
- Conclusion: Phoenix LiveView fills a gap between static and full blown SPA
-->

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
[.code-highlight: 2-3, 6]
[.code-highlight: 1, 4-5, 7-11]

<!-- TODO: Check if there is highlighting for eex -->

```html
<item>
  <div class="card <%= color_for(@type) %> darken-1">
    <a href="#" phx-click="edit" phx-value="<%= @id %>">
      <div class="card-content white-text">
        <p style="white-space: pre;">
          <%= @text %>
        </p>
      </div>
    </a>
  </div>
</item>
```

---

```javascript
{
  "static": [
    "<item><div class=\"card ",
    " darken-1\"><a href=\"#\" phx-click=\"edit\" phx-value=\"",
    "\"><div class=\"card-content white-text\"><p style=\"white-space: pre;\">",
    "</p></div></a></div></item>"
  ],
  0: "red",
  1: "A0202252-7778-440A-A117-9C2476D418AF",
  2: "My great card!"
}
```

---

### Thank you for
## __listening__

---

# __Questions?__