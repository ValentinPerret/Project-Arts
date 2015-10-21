puts 'Hello-World'


puts "What's the video name"
code = gets.chomp
code = '8jZ3h6lbjDw'

system("omxplayer -b `youtube-dl -g #{code}`")