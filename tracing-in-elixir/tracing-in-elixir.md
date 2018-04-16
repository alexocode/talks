theme: Poster, 1

# Tracing
### *In Elixir*

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

^
1. "random" backend developer in a "random" company using Elixir
2. "We need more diagnostics in the backend!"
  - event sourced, cqrs (commanded), phoenix
3. What options are there? What can I use?
4. "Look into OpenTracing, you must"
5. OpenTracing: Vendor-neutral APIs and instrumentation for distributed tracing
6. Otter, ExRay more?
7. "Woho! Working Prove of Concept!"
8. Integrate tracing without much code changes?
  - Carriers in OpenTracing, no support in Otter
  - Global State? ets table? When to clean
  - Solution: Per-Process Span stack
9. Request -> Command
10. "What about Command -> Command and Command -> Projection?"
11. "Carrier"-like: Injected trace IDs into command/event metadata
12. Trace: Request -> Command -> Projections / Commands (?)

---

# Let's meet *Alexander*

---

# 👨‍💻

^
Backend Developer at a random compomany, let's say

---

# **Smallcentrix**

---

> We need more diagnostics!
-- Pretty much everybody

---

![100%](images/google.png)

^
- elixir diagnostics (Healthcare)
- elixir tracing

---

# 🤷‍♂️

^
- No idea where to start, what makes sense
- Ask experienced colleague, Senior Developer, if you want

---

# 🧙‍♂️

---

> Look at OpenTracing, you scrub!
-- 🧙‍♂️

^
Pretty much the exchange

---

![](images/open-tracing.png)

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