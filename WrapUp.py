from RecupFromYoutubePy3V2 import youtube_search

def write_that(nomFichier,ligneAjoutee):

	target = open(nomFichier, 'w')

	target.truncate()

	target.write(ligneAjoutee)

	target.close()

def read_n_play(nomFichier,maxPlay = 2):
	import os

	lines ={}
	target = open(nomFichier)

	lines=target.readlines()

	for i in range(0, maxPlay):
		#print(lines[0])
		recupYoutube = "youtube-dl -g %s" % lines[i]
		os.system(recupYoutube) #test line 
		#os.system("omxplayer -o `recupYoutube`") #Raspi line

	target.close()

#from ListTraitment import read_n_play
#add omxplayer -b `youtube-dl` for integration


if __name__ =="__main__":

	class Option:
		q="Torlk et Marmotte"
		o="date"
		max_results=30


	write_that('VideoList.txt',youtube_search(Option))
	read_n_play('VideoList.txt',2 )
