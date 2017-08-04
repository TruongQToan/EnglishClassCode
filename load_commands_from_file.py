import xlrd
import sys
import subprocess

def encode(s):
    if isinstance(s, float) or isinstance(s, int):
        s = str(int(s))
    return s.encode("ascii", "ignore").decode('utf-8')

if __name__ == "__main__":

    book = xlrd.open_workbook(sys.argv[1])
    sheet = book.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        cmd = encode(sheet.cell(row, 0).value).strip()
        num_files_per_group = encode(sheet.cell(row, 1).value).strip()
        num_plays = encode(sheet.cell(row, 2).value).strip()
        num_copies = encode(sheet.cell(row, 3).value).strip()
        to_mp3 = encode(sheet.cell(row, 4).value).strip() if sheet.cell(row, 4) else ''
        name = encode(sheet.cell(row, 5).value).strip() if sheet.cell(row, 5) else ''
        shuffled = encode(sheet.cell(row, 6).value).strip()
        list_of_tracks = encode(sheet.cell(row, 7).value).strip()
        type_overview = encode(sheet.cell(row, 8).value).strip()

        if cmd == "reviewglossika.py":
            list_of_args = ["python3", "reviewglossika.py",
                '-f',
                num_files_per_group,
                '-p', num_plays,
                '-c', num_copies,
                '-n', name,
                '-s', shuffled,
                '-l']
            for u in list_of_tracks.split(' '):
                list_of_args.append(u)
            if not to_mp3 == '': list_of_args.append(to_mp3)
            subprocess.call(list_of_args)
        elif cmd == "mixaccent.py" or cmd == "mixgrammar.py":
            list_of_args = ["python3", cmd,
                num_files_per_group,
                num_plays,
                num_copies,
                '-n', name,
                '-s', shuffled, '-l']
            for u in list_of_tracks.split(' '):
                list_of_args.append(u)
            if not to_mp3 == '': list_of_args.append(to_mp3)
            subprocess.call(list_of_args)
        elif cmd == "overviewglossika.py":
            #print ("LIST OF TRACKS " + str(list_of_tracks))
            start = list_of_tracks.split('-')[0]
            #print ("START " + str(start))
            end = list_of_tracks.split('-')[1]
            #print ("END " + str(end))
            list_of_args = ["python3", "overviewglossika.py",
                start, end,
                '-f', num_files_per_group,
                '-t', type_overview]
            if not to_mp3 == '': list_of_args.append(to_mp3)
            subprocess.call(list_of_args)
