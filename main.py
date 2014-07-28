import track
import fresh_tomatoes

ma_vmv = track.Track("Vivir mi vida by Marc Anthony",
                     "Latin - United States",
                     "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/GClef.svg/175px-GClef.svg.png",
                     "http://www.youtube.com/watch?v=YXnjy5YlDwk")

ls_sc = track.Track("Sograo Caprichou by Luan Santana",
                   "Sertanejo - Brazil",
                   "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/GClef.svg/175px-GClef.svg.png",
                   "http://www.youtube.com/watch?v=HtpPvt1wyzU")

jc_bl = track.Track("Baghdad (live) by Jesse Cook",
                    "Undefined - Canada",
                   "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/GClef.svg/175px-GClef.svg.png",
                   "http://www.youtube.com/watch?v=bWjgyFvZ2OA")

me_syb = track.Track("Salam Ya Baladi by Mahmoud el Esseily",
                     "Arab - Egypt",
                     "http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/GClef.svg/175px-GClef.svg.png",
                     "http://www.youtube.com/watch?v=IosvWLVJKOo")




tracks = [me_syb, ls_sc, jc_bl, ma_vmv]
fresh_tomatoes.open_tracks_page(tracks)
