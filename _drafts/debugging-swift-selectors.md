---
layout: post
title: "Debugging Swift Selectors"
published: false
tags:
 -
---

Selectors are an Objective-C construct that don't really carry over to Swift. As such, a lot of detail can be lost in the abstraction, resulting in unclear errors.

Application crashes with an error that a method cannot be found for a selector can mean that the method doesn't exist, or that it cannot be effectively translated to Objective-C. For example, including an enum type in a method signature means it will not be visible as a selector.