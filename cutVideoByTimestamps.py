import os, argparse

parser = argparse.ArgumentParser(description='Cut video based on provided time segments.')
parser.add_argument('input', metavar='input', type=str, help='input video')
parser.add_argument('timestamps', metavar='timefile', type=str, help='timestamps file')
parser.add_argument('--output', '-o', metavar='output', type=str, default='out.mp4', help='output video')

'''
Sample command
ffmpeg -i test.mp4 -vf "select='between(t,1,2)+between(t,4,5)',setpts=N/FRAME_RATE/TB" -af "aselect='between(t,1,2)+between(t,4,5)',asetpts=N/SR/TB" out.mp4
'''

def main():
	args = parser.parse_args()
	segments_str = ''
	
	with open(args.timestamps) as f:
		lines = f.readlines()
		segments_str = 'between(t,' + lines[0].strip() + ')'
		for l in lines[1:]:
			segments_str = segments_str + '+between(t,' + l.strip() + ')'

	print(segments_str)
	ffmpeg_cmd = 'ffmpeg -i "' + args.input + '" -vf "select=\'' + segments_str + '\',setpts=N/FRAME_RATE/TB" -af "aselect=\'' + segments_str + '\',asetpts=N/SR/TB" "' + args.output + '"'

	os.system(ffmpeg_cmd)


if __name__ == '__main__':
	main()