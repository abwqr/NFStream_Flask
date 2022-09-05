from nfstream import NFStreamer
import sys
path = sys.argv[1]

if __name__ == '__main__':
    my_streamer = NFStreamer(source=path).to_csv()
    print(my_streamer)
    
# def pcapTocsv(path):
#     if __name__ == '__main__':
#         my_streamer = NFStreamer(source=path).to_csv()
#         return my_streamer
#         # for flow in my_streamer:
#         #     print(flow)

# func = pcapTocsv('F:/CyberSec/Data/Scripts/test1.pcap')