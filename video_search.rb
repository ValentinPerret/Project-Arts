puts 'Hello-World'


puts "What's the video name"
code = gets.chomp
video = `youtube-dl -g #{code}`