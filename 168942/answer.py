def data_recovery(data):
    my_dict = {"PNG" : b'\x89PNG\r\n\x1a\n', "JPEG" : b'\xff\xd8\xff', "BMP" : b'\x42\x4d',
               "TIFF" : b'\x49\x49\x2a\x00', "GIF" : b'\x47\x49\x46\x38', "ZIP" : b'\x50\x4b\x03\x04',
               "ELF" : b'\x7fELF', "PDF" : b'\x25\x50\x44\x46', "MP3" : b'\x49\x44\x33',
               "MPEG" : b'\xff\xfb', "PDDF" : b'\x00\x00\x01\x00', "ICO" : b'\x00\x01\x00\x00'}
    res = list()
    for i,j in my_dict.items():
        if data.find(j) != -1:
            res.append(i)
    return res

print(data_recovery(b'\x89PNG\r\n\x1a\nBMII*\x00\xff\xd8\xff\xff\xd8\xff\x00\x00\x01\x00\x00'))