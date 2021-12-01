(import [pandas :as pd])
(import [numpy :as np])

(setv path "data.csv")
(setv data (pd.read_csv path))

(setv score (get data "score"))
(print "Disperssion score:" (.var score))

(setv time (get data "time"))
(print "<Time>:" (.mean time))