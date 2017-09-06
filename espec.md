# [fit] ESpec

---

# ESpec

- BDD testing framework
- Inspired by Rubys RSpec
- Not based on ExUnit

^ExUnit is Elixirs baked-in testing framework
^What does BDD mean?

---

# [fit] BDD

*b*ehaviour-*d*riven *d*evelopment

---

# BDD
#### A brief overview

- Extension of *t*est-*d*riven *d*evelopment (*TDD*)
- Simple, *d*omain-*s*pecific *l*anguage (*DSL*)
- Tests describe the behaviour of components
- Tests are derived from the acceptance criteria

^
Tests written as User Stories
For example: Cucumber

---

# BDD
#### Spec-based testing

- A more technical approach
- Alternative to free-form unit testing
- Describe components in an english-like DSL

---

# ESpec
#### An overview

- Organization with `describe`, `context` and `it` blocks
- `before` and `finally` blocks
- Wide variety of matchers (`eq`, `be_integer`, `have`)
- `let` to define memoizable functions

^
*memoizable* means that it only evaluates once when first called

---

# [fit] Example

---

# Roman Numerals
#### ExUnit

```elixir
defmodule RomanNumeralsTest do
  use ExUnit.Test

  test "1 is converted to I" do
    assert RomanNumerals.convert(1) == "I"
  end
end
```

---

# Roman Numerals
#### ESpec

```elixir
defmodule RomanNumeralsSpec do
  use ESpec

  describe ".convert" do
    it "should convert 1 to I" do
      expect(RomanNumerals.convert(1)).to eq("I")
    end
  end
end
```

---

# Roman Numerals
#### ESpec

ESpec allows us to write expectations in __three__ ways:

```elixir, [.highlight: 6, 10, 14]
defmodule RomanNumeralsSpec do
  use ESpec

  describe ".convert" do
    it "should convert 1 to I" do
      expect(RomanNumerals.convert(1)).to eq("I")
    end

    it "should convert 7 to VII" do
      expect RomanNumerals.convert(7) |> to(eq "VII")
    end

    it "should convert 10 to X" do
      RomanNumerals.convert(10) |> should(eq "X")
    end
  end
end
```

^
1. identical to RSpec
2. Elixir version
3. Shortcut

---

# [fit] Increase the complexity

---

# Blog

- Can have multiple articles
- Each article can have comments

*Let's focus on comments*

---

```elixir
defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end
```

^
Let's assume we have the `create` functions defined somewhere

---

# [fit] What is going on here?

---

```elixir, [.highlight: 5-7]
defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end
```

---

```elixir, [.highlight: 9-15]
defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end
```

---

```elixir, [.highlight:17-23]
defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end
```

---

```elixir, [.highlight:25-35]
defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end
```

---