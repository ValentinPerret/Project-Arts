puts 'Hello-World'


puts "What's the video name"
code = gets.chomp
code = '8jZ3h6lbjDw'
video = `youtube-dl -g #{code}`
puts video + " attention c'est parti"

system("omxplayer -b #{video}")