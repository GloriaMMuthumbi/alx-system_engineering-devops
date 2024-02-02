#!/usr/bin/env ruby
#ruby script that outputs: [SENDER], [RECIEVER], [FLAGS]
puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
