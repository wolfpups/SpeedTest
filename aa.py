import speedtest

servers = []
threads = None
s = speedtest.Speedtest()
#s = Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()
results_dict = s.results.dict()
download_result = results_dict["download"]
upload_result = results_dict["upload"]
download_result = str(int(round(download_result / 1000.0 / 1000.0, 0)))
upload_result = str(int(round(results_dict["upload"] / 1000.0 / 1000.0, 0)))
ping = str(int(round(results_dict["ping"], 0)))
your_isp = results_dict["client"]["isp"]
share_link = results_dict["share"]
text = "Download Speed: " + download_result + "Mbs\nUpload Speed: " + upload_result + "Mbs\nPing: " + ping + "ms\nYour ISP: " + your_isp
print(text)