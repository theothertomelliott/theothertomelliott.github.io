# telliott.io

This is a [Jekyll site](http://jekyllrb.com/) running my [personal blog](http://telliott.io).

## Dependencies

The site requires Jekyll:

`sudo gem install jekyll`

And Bundler:

`sudo gem install bundler`

Additional dependencies can be installed using Bundler in the projects root dir:

`bundle install`

## Running Locally

If you have the Jekyll gem installed, a local copy of the site can be launched using the jekyll command:

`jekyll serve`

This will be accessible from [http://localhost:4000](http://localhost:4000)

## Adding a Post

A new post can be generated using a Thor command:

`thor jekyll:new [POST TITLE]`

Which will create a new post and open the file in Sublime Text 2.

Thanks to [Jonas Brusman](http://jonas.brusman.se/2012/12/28/create-jekyll-posts-from-the-command-line/) for this tip.