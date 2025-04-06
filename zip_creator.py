import zipfile

def make_archive(filepaths, directory):
    with zipfile.ZipFile(directory + '/archive.zip', 'w') as zipf:
        for file in filepaths:
            zipf.write(file, arcname=file.split('/')[-1])
            # zipf.write(file)