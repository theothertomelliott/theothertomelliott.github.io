require "stringex"
require "fileutils"

class Jekyll < Thor
  desc "new", "create a new draft"
  method_option :editor, :default => "subl"
  def new(*title)
    title = title.join(" ")
    filename = "_drafts/#{title.to_url}.md"

    if File.exist?(filename)
      abort("#{filename} already exists!")
    end

    puts "Creating new post: #{filename}"
    open(filename, 'w') do |post|
      post.puts "---"
      post.puts "layout: post"
      post.puts "title: \"#{title.gsub(/&/,'&amp;')}\""
      post.puts "tags:"
      post.puts " -"
      post.puts "---"
    end

    system(options[:editor], filename)
  end

  desc "publish", "Publish a post from a draft"
  def publish(*draft_filename)
    draft_filename = draft_filename.join(" ")
    draft_basename = File.basename(draft_filename, ".md")
    date = Time.now.strftime('%Y-%m-%d')
    filename = "_posts/#{date}-#{draft_basename}.md"

    if !File.exist?(draft_filename)
      abort("The draft _drafts/#{filename}.md doesn't exist!")
    end

    if File.exist?(filename)
      abort("#{filename} already exists!")
    end

    FileUtils.mv(draft_filename, filename)

    puts "Moved #{draft_filename} to #{filename}"

  end
end
