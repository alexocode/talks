theme: Poster, 1

# Getting Started
# with *Elixir*
#### Slides on GitHub[^1]

[^1]: https://github.com/sascha-wolf/talks

---

## What is *Elixir*?

---

> Elixir is a dynamic, functional language designed for building scalable and maintainable applications.
-- elixir-lang.org

^
Great sales pitch, right?

---

> Elixir is young and immature!
-- Some grumpy old programmer

^
It was released in 2011

---

## *Elixir* is running
## on the Erlang VM
#### Also called *BEAM*

---

## Why is that important?

^
In Elixir you can directly interact with Erlang modules. AND ...

---

## Erlang is 32 years old
### *OpenSource for 20 years*

^
If you know about Erlang you might have heard about OTP

---

# Erlang/*OTP*
### *O*pen *T*elecom *P*latform

---

> OTP is a collection of useful middleware, libraries, and tools written in the Erlang programming language.
-- Wikipedia on OTP

---
[.build-lists: true]

# *OTP* is well suited for

- Distributed
- Fault-tolerant
- Highly available

# systems

---

## *O*f course you get all of
## *t*his "for free" when
## *p*rogramming *Elixir*

---

## What else?

---

## Immutable data

---

## Pattern matching

---

## Easy concurrency
#### Using the Actor Model

---

## Topics for today?

---

- Syntax
- Functional paradigms
- Immutable data
- Pattern matching

---

# Let's get started!
#### Unless you have some questions

---

# Fancy new startup

---

# E-Commerce shop

---

## A wild customer
## comes along
# 👨‍💼

---

## He has some
# requirements

---

# 1.

---

> We need a way of adding products to a shopping cart!
-- The wild customer

---

# 2.

---

> We need to calculate the overall sum of money to be paid
-- The wild customer

---

# 3.

---

> We have premium customers that pay 10% less!
-- The wild customer

---

# 3.

---

> We need shipping costs that are dependent on the weight of the shipment!
-- The wild customer

---

# 4.

---

> Free shipping over 100€!
-- The wild customer

---

# 5.

---

> When you select PayPal as your payment method, we charge 5% more because of fees that we have to pay!
-- The wild customer

---

# Bonus!

---

# B1.

---

> We want to know the CLVs (revenue generated per customer) to support our most valuable customers!
-- The wild customer

---

# B2.

---

> We need to exclude the shipping costs from the CLVs!
-- The wild customer

---

#### *Follow us on Twitter @wolf4earth, @JanFornoff*
# Coding
# Dojo
#### <br/> *`git clone https://github.com/jfornoff/elixir-ug-rover`*
