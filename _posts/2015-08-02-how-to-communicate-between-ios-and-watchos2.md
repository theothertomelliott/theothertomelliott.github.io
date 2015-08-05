---
layout: post
title: "Keeping iOS and watchOS2 apps synchronized with WatchConnectivity"
published: false
tags:
 -
---

Quick tutorial: Sending state data between your watchOS and iOS device using the WatchConnectivity framework.

Will assume familiarity with XCode and Interface Builder.

This example is in Swift, but there is an Objective-C version in the GitHub repository.

# Instructions

1. Create a new project with WatchKit
2. Add the WatchConnectivity framework
3. Set up your iOS UIView and UIViewController (add a text field and hook it up)
4. Set up your WatchKit App Interface and WatchKit Extension InterfaceController (add a label and hook it up)
5. Add a WCSession to your UIViewController
6. Add a WCSession to your InterfaceController
7. Update application state when the text field changes to change the label

# Running the Project

* Starting up the watch and iPhone simulators together may not work

May need to add the app to the Watch through the Watch App.

In order to get a console for both apps at the same time, you will have to launch the Watch App first, then switch to your iOS target to launch the iOS App.

You may see that your single-character updates lag a little in getting to the watch. This is a pretty good indicator that you should be careful about how frequently you send these updates!

# Further Examples

Works both ways (check this)

Example project. Swift and Objective-C versions. Also included some additional examples to show what else you can do with WatchConnectivity.

# Possible Problems

* Starting up the watch and iPhone simulators together may not work
* May get an error if one is not running?