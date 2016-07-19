---
layout: post
title: "Improve Accessibility for your iOS Apps Without Sacrificing UI Design"
---
Shortly after releasing Speaker Alert v2.2.0, a user emailed me to let me know that this version was harder to use for blind people such as herself, who use VoiceOver to navigate iOS apps. This post outlines how this was improved for v2.2.1, and some things I'm working on to better support other accessibility features.

The main issue highlighted was that the simplified in-speech view removed the pause and stop buttons from the screen, so it's not possible to discover such controls using VoiceOver. For those unfamiliar with this feature, when enabled, VoiceOver will speak the name of a UI control on a first touch, and a double-tap will activate the control. A typical usage pattern would be to sweep your finger across the screen until you find the control (or information) you want. When using VoiceOver, it will therefore be hard to determine that the entire screen is a tappable area - with VoiceOver disabled the first tap performs the action, so is easily discoverable, with VoiceOver enabled, the first tap provides no hints whatsoever.

TODO: Image illustrating changes

I was, in all honesty, embarrassed that I hadn't considered this use case, and was determined to improve the situation as quickly as possible. However, being quite pleased with the streamlining of the UI, I didn't want to immediately revert the changes.

I considered adding a setting to display the controls during a speech for users that needed it, but it seemed unfair that the app wouldn't be usable until a blind user discovered the setting. Luckily, UIKit provides an easy way to check if VoiceOver was enabled (UIAccessibilityIsVoiceOverRunning()), so I could add the controls back exactly when needed. Not only that, but I could also add a label that gave the current color of the display in text, so users who are unable to discern color would still be able to identify where they were in their time.

TODO: Add image showing controls

VoiceOver is not the only accessibility setting provided in iOS, so let's take a closer look at the accessibility settings available.

A look at accessibility settings

The accessibility options in iOS can be reached in the Preferences app under General->Accessibility.

TODO: Add image of Accessibility screen

Accessibility options are divided into several sections:

Vision

The vision settings can be divided into several types that may affect app UI: screen reading, color alteration, font scaling and (a category all it's own) button shapes.

Screen reading settings include the previously mentioned VoiceOver, but also under Speech there are the Speak Selection, Speak Screen and Speak Auto-text settings. The key settings here are VoiceOver and Speak Screen, which change the manner in which a user would interact with your app. VoiceOver is used as described in the introduction, Speak Screen provides on demand reading of on-screen components. This does not require double-tapping to activate buttons.

TODO: Determine if Speak Screen is always shown as active.

Colors can be altered by the Invert Colors, Grayscale and Increase Contrast settings. The first two will drastically alter the colours displayed, and highlight that is important not to rely solely on colour to provide information. Increase Contrast makes smaller changes to colour displayed in an app, but it is advisable to test your app with this setting on to make sure you're happy with how it appears.

The Larger Text and Bold Text settings, as would be expected, only affect the display of text. Any UI layout should be viewed with these settings to ensure it is still usable and nothing is pushed off the screen.

Finally, Button Shapes is a setting that provides an underline or outline to buttons to make them more clearly visible. This should not have a huge effect on layout, but it is worth taking a look at your UI with this setting to have a feel for how it looks.

Some settings have not been mentioned, but these are on the whole tools and tweaks to built-in UI elements that shouldn't have an effect on UI design or experience.

Interaction

Most significant among the Interaction settings is Switch Control, which highlights UI elements one at a time, so they can be selected by a separate accessory. Again, this means that only visible components can be interacted with, so full screen taps may be difficult, and shake or complex on-screen gestures are likely not an option.

Similarly Touch Accommodations changes the way in which touch gestures are handled, and may make it difficult to use specific gestures on-screen.

Assistive Touch provides an on-screen button to replace certain OS-wide gestures (like swiping from the bottom of the screen for the Control Center), it shouldn't have an affect on your app directly. However, users with this feature turned on may have difficulty with some gestures, or be using a separate accessory to control their device.

The remaining interaction settings primarily revolve around the keyboard and home button behaviours. Most of these will not affect your UI, but it is important to note that users can disable vibration entirely if they wish.

Hearing

The hearing section contains settings for hearing aids, audio balance (and mono mode) and providing an LED flash when an alert is received. The LED flash only takes effect when the phone is locked, so will not have an impact on the experience in your app. Hearing aid controls affect audio output and should provide benefits to your app "for free" if you use audio.

Left-right balance, however, may affect your app if you make use of stereo audio. As such, you should consider if your features are still usable should the balance be changed, or mono mode engaged.

My personal view is that apps should be usable without sound anyway, as I usually have my phone in silent mode to avoid bothering anyone around me. Sound can add a lot to an app, but I believe it shouldn't be a required part of your user experience.

Media

The media section provides settings primarily for video content, namely subtitles and audio descriptions. If your app plays your own video content, you should make sure that the videos you use support these features appropriately.

Learning

Learning contains Guided Access, which simply restricts access to a particular app for a set duration of time. While this feature should not affect UI design, this may have implications for switching apps (such as launching browsers and companion applications) and should feature in testing.

Some inaccessible UI choices

We've hinted at some of these already, but there are a number of sure-fire ways to make your app inaccessible.

Image buttons without accessibility labels will be described with just the image file name in VoiceOver, which will more than likely be unclear to the user.

Imparting information with color alone means that such information is unavailable to users with grayscale or possibly even reversed colors. This is an issue that was core to Speaker Alert, as alerts were given entirely using the background color of the speech view.

Shake gestures as the only means of performing an action exclude users who rely on accessories to interact with the UI, similar for complex touch gestures.

Full screen tap interactions without a visible button can be difficult to discover with VoiceOver and other accessibility modes.

Making the inaccessible accessible

Key to making a UI accessible are accessibility attributes. These are attributes that can be applied to a UIView in order to give a text description that can be spoken in VoiceOver, etc. Chief amongst these is accessibilityLabel, which provides a localized name for a view. If no accessibility label is provided, the title of the view is used (such as the text of a label or text button).

Accessibility attributes can be set either in code, or in Interface Builder under the Identity Inspector.

TODO: Add image of identity inspector

TODO: Add example code

TODO: Describe Displaying extra attributes when VoiceOver or other visual helpers are enabled.

TODO: Describe adding buttons for gestures and full screen taps

State	Notification	Comments
UIAccessibilityIsVoiceOverRunning()	UIAccessibilityVoiceOverStatusChanged	
UIAccessibilityIsMonoAudioEnabled()	UIAccessibilityMonoAudioStatusDidChangeNotification	
UIAccessibilityIsInvertColorsEnabled()	UIAccessibilityInvertColorsStatusDidChangeNotification	
UIAccessibilityIsBoldTextEnabled()	UIAccessibilityBoldTextStatusDidChangeNotification	
UIAccessibilityIsGrayscaleEnabled()	UIAccessibilityGrayscaleStatusDidChangeNotification	
UIAccessibilityDarkerSystemColorsEnabled()	UIAccessibilityDarkerSystemColorsStatusDidChangeNotification	
UIAccessibilityIsSwitchControlRunning()	UIAccessibilitySwitchControlStatusDidChangeNotification	
UIAccessibilityIsSpeakScreenEnabled()	UIAccessibilitySpeakScreenStatusDidChangeNotification	
Testing accessibility

Due to the wide array of accessibility modes available in iOS, it is crucial that you are able to effectively test your app under these conditions, or demonstrate that it will support these modes adequately.

The Simulator

Unfortunately, the simulator does not provide all the accessibility modes available on a physical iOS device. While some of the layout-affecting settings can be applied (such as Larger Text), accessibility modes such as VoiceOver are not available. Instead, an Accessibility Inspector tool is provided that displays accessibility information about individual controls.

TODO: Add screenshot of accessibility inspector

This can be useful for validating that settings have been applied to all controls once you have an effective accessibility strategy in place, but you will need to do some testing on a physical device to ensure your app is usable with accessibility settings on.

On device

There can be no substitute for testing on device to get a good feel for how accessibility settings affect your app. Try using your app with VoiceOver or inverted colors to identify any pain points, or better yet, give your device to someone who hasn't used your UI before and see if they can navigate the app effectively.

UI Testing

Apple introduced UI Testing in XCode 7, which allows for black-box testing of an app's UI. This form of testing is touted as requiring an app to be accessible, as it uses the accessibility id of a UIView to allow for identification of buttons and other controls. This does not, however, guarantee an app that is UI testable is also accessible.

An important caveat to note is that there are several accessibility attributes associated with UIView, and which one is used will depend on exactly which are set. For example, the accessibilityIdentifier is not shown by the Accessibility Inspector, instead showing accessibilityLabel. For practical applications, the label will be used if set, and localized as appropriate, but the identifier may be used as fallback. You can use the label to reference UI elements in test code, but for localized applications, the label may change depending on locale. Regardless, when putting together UI tests, it is advisable to test the UI for accessibility manually at the same time to ensure you're testing the correct attributes.
