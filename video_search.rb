puts 'Hello-World'


puts "What's the video name"
code = gets.chomp
code = '8jZ3h6lbjDw'
code2 = '_NWmuRZm85E'

system("omxplayer -b `youtube-dl -f bestvideo -g #{code}`")

system("omxplayer -b `youtube-dl -f bestvideo -g #{code2}`")