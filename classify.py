import struct

#Assumptions: file buf starts at the beginning of the vlr
def classify(file_buf, index):
    end_index = index
    # make sure this is not header MThd chunk (first chunk in file, 14 bytes total including 8 byte header)

    # find status byte--first byte of event data (bit 7 set)

    # once determined event type, must process accordingly and parse to next point in time of the status byte
    # if midi event (hex 80-8F to 140-14F)

    # if sys event (hex F0 and F7)

    # if meta event (hex FF)

