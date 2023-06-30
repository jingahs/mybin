import json
import sys

#Converts the exported mappings.json from Stash to a playlist

mappings = str(sys.argv[1])
if mappings:
	converted_mappings = json.load(open(mappings,encoding='UTF-8'))
	if converted_mappings and "scenes" in converted_mappings:
		with open('playlist.m3u8', 'w',encoding='UTF-8') as f: #Use m3u8 to include foreign languages
			for scene in converted_mappings["scenes"]:
				f.write(scene["path"])
				f.write('\n')