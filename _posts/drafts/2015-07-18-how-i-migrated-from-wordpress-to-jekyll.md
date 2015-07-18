---
layout: post
title: "How I Migrated From Wordpress To Jekyll"
published: false
tags:
 -
---

## Exporting and Backing Up

Export data using the built-in Export. Works just as well on self-hosted Wordpress sites as it does on Wordpress.com.
https://en.support.wordpress.com/export/

Took a backup using BackWPup:
https://wordpress.org/plugins/backwpup/

## Importing

Important to note that posts are imported as HTML.

## Fixing the Import

### Front Matter Formatting

Added newlines to an except directive:

{% highlight ruby %}
excerpt: !ruby/object:Hpricot::Doc
  options: {}
{% endhighlight %}

Was easy to remove this with a search and replace in Sublime Text 2.

### Fixing Post Permalinks

Permalinks were a problem, as I was previously using a permalink structure from Drupal, which included the node number (specifically */node/[n]*), and node numbers don't really exist in Jekyll. Not only this, but due to all content types having shared the same incrementer, the posts weren't necessarily numbered continuously. So there would be posts at */node/123* and */node/234*, but nothing in between.

This was fixed with a Python script that iterated over all the posts and mapped them to the appropriate permalink by finding a live URL with a corresponding title.

Full script here: [permalinks.py](https://github.com/theothertomelliott/theothertomelliott.github.io/blob/master/_script/permalinks.py)

The upshot of this is that I can use the default Jekyll permalink format (which is more human friendly) without affecting my older posts.

### Caption Formatting

A few of my posts used captioned images, which weren't processed very well 

### A Final Scan

To make sure that all my old posts were now rendering correctly, I made a final visual pass over them by creating a single page that listed all posts and their entire contents.

// TODO: Include a code sample for this

Then I just had to scroll through the posts and keep an eye out for missing images or anything that looked odd.

A few images that weren't under the standard wp-content folders had been missed out, and image names with brackets in them had, for some reason, been modified during the import to remove the brackets. This was pretty quick to correct manually, pulling any missing images from the original live site.